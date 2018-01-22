"""
Module docstring
"""
import random
from noelclasses import DeribitAccount, OpenPosition, OpenOrder
from noellogging import to_log

# TODO move to config
KILL_OPEN_ORDERS_ON_INIT = True
PROBABILITY_LONG = 0.5
DEFAULT_LOT_SIZE = 10
DEFAULT_TRADING_TICKET = 'BTC-26JAN18'

def position_aggregate(position_object, open_orders):
    """
    Scans opened orders for instruments with positions already opened
    and mutates positionObject.status: -2,-1,0,1,+2
    # status:
        # - 2: in short position with all orders executed, -1: short order
        #  position where orders sent to exchange, 0: - out of position,
        #  +1: long order position where orders sent to exchange
        #  +2: in long position, all orders executed
    """
    instrument = position_object.instrument
    pos_size = 0
    order_size = 0
    pos_size = int(position_object.size)
    for open_order in open_orders:
        if open_order.instrument == instrument:
            if open_order.type == "sell":
                order_size = int(open_order.size) * (-1)
            else:
                order_size = int(open_order.size)
            order_size += order_size

    # Now based on order_size and pos_size set object OpenPosition
    # size_status - in position type: -2,-1,0,+1,0: -2 short executed,
    #  -1 short orders placed, 0 out position, +1 long placed, +2 buy executed
    # position_status - in open / closing mode -
    # if openpositions and placed orders in one direction => opening position : +1
    # if opened and placed orders are in different directions => closing position: -1
    # all other = 0
    #

    position_object.total_size = pos_size + order_size
    if order_size == 0 and pos_size > 0:
        setattr(position_object, 'size_status', +2)
        setattr(position_object, 'position_status', 0)
    elif order_size == 0 and pos_size < 0:
        setattr(position_object, 'size_status', -2)
        setattr(position_object, 'position_status', 0)
    elif pos_size == 0 and pos_size == 0:
        setattr(position_object, 'size_status', 0)
        setattr(position_object, 'position_status', 0)
    elif order_size > 0 and pos_size > 0:
        setattr(position_object, 'size_status', +1)
        setattr(position_object, 'position_status', +1)
    elif order_size > 0 and pos_size < 0:
        setattr(position_object, 'size_status', +1)
        setattr(position_object, 'position_status', -1)
    elif order_size < 0 and pos_size < 0:
        setattr(position_object, 'size_status', -1)
        setattr(position_object, 'position_status', +1)
    elif order_size < 0 and pos_size > 0:
        setattr(position_object, 'size_status', -1)
        setattr(position_object, 'position_status', -1)
    position_object.aggregate_size = pos_size + order_size
    # debug print
    to_log(30*'x')
    to_log(instrument)
    to_log('pos_size:' + str(pos_size))
    to_log('order_size:' + str(order_size))
    # debug print end
def generate_order():
    """
    Generate random number and trigger order
    """
    random.seed()
    if random.random() > PROBABILITY_LONG: # go long
        return 'buy'
    else:
        return 'sell'

def send_order(instrument,size,direction, price,account):
    """
    aggregate function to send order
    """
    _string = 'Sending order: direction:{}\ninstrument:{}\nsize:{}\nprice:{}'.format(
               direction, size, instrument, price)
    to_log(_string)    
    if direction == 'buy':
        result = account.buy_order(instrument, size, price)
    elif direction == 'sell':
        result = account.sell_order(instrument,size, price)
    else:
        to_log('Wrong direction. Returning None')
        return None
    to_log('Result of the transaction')
    to_log(result['order'])
    return result

def main_loop(*accounts):
    """
    Main body loop
    """
    keep_running = True
    while keep_running:
        for account in accounts:
            for _p in account.current_positions:
                # First of all check flags and based on that define the logic
                # Possible combinations
                if _p.size_status == 0: # if we are out of position
                    # generate order might return +1 - long, -1 sell
                    # 0 - no signal (reserved for future use)
                    _direction = generate_order()
                    _price = account.get_price()['midPrice']
                    try:
                        result = send_order(DEFAULT_TRADING_TICKET,
                                            DEFAULT_LOT_SIZE, _direction,
                                            _price, account)
                        result = result['order']
                        new_order = OpenOrder(result['orderId'], result['instrument'],
                                              result['direction'], result['price'],
                                              account, result['filledQuantity'],
                                              result['created'])
                        account.open_order.append(new_order)
                        if result['direction'] == 'sell':
                            _p.size_status = -1
                        elif result['direction'] == 'buy':
                            _p.size_status = +1
                        _p.position_status = 1
                        to_log('New position status' + str(_p.position_status))
                        to_log('New size status' + str(_p.size_status))
                    except:
                        to_log('Failed to send order. Exception raised')
                elif _p.size_status == 2 or _p.size_status == -2:
                     #if we are in full position
                    # call check profitability status and probably send close signal
                    pass
                elif _p.size_status == 1 or _p.size_status == -1:
                    #if we are still have some orders placed
                    # call determine what to do with the orders
                    pass


def initialize(account):
    """
    Is launched once
    """
    if KILL_OPEN_ORDERS_ON_INIT:
        account.kill_open_orders('futures')
        to_log('killing all opened orders')
    # Find all opened positions
    #account.current_position_orders = account.get_current_positions()
    _current_open_orders = []
    _current_positions = []
    # scan opened orders and add OpenOrder object to Account
    for _p in account.get_current_positions():
        newposition = OpenPosition(account, _p['instrument'], _p['averagePrice'],
                                   _p['direction'], _p['size'], _p['kind'])
        _current_positions.append(newposition)
    setattr(account, 'current_positions', _current_positions)
    for _o in account.get_open_orders():
        newopenorder = OpenOrder(_o['orderId'], _o['instrument'], _o['direction'],
                                 _o['price'], _o['quantity'], account,
                                 _o['filledQuantity'], _o['lastUpdate'])
        _current_open_orders.append(newopenorder)
    setattr(account, 'open_orders', _current_open_orders)
    to_log(('Initialized account "%s" successfully:') % (account.name))
    to_log('**********************************************************')
    to_log('now print account property after init')
    for key, value in account.account_info.items():
        to_log((str(key) + ":" + str(value)))
    to_log('Current opened positioned:')
    for _positionobject in account.current_positions:
        # aggregate current and opened positions by instrument name
        position_aggregate(_positionobject, account.open_orders)
        to_log('**********************************************************')
        for _k, _v in _positionobject.__dict__.items():
            to_log(_k, _v)
    to_log(30 * "*")
    to_log('Current opened orders:')
    for _orderobject in account.open_orders:
        to_log('**********************************************************')
        for _k, _v in _orderobject.__dict__.items():
            to_log(_k, _v)

def main():
    """
    main function
    """
    account_deribit = DeribitAccount('main_account', 'BTC')
    initialize(account_deribit)



if __name__ == "__main__":
    main()
