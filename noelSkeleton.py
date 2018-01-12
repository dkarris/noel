"""
Module docstring
"""

from noelclasses import DeribitAccount, OpenPosition, OpenOrder
from noellogging import to_log
import random

# TODO move to config
DERIBIT_INSTRUMENT = ['BTC-26JAN18']
KILL_OPEN_ORDERS_ON_INIT = True
PROBABILITY_LONG = 0.5
LOT_SIZE = 10


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
    print 30*'x'
    print instrument
    print 'pos_size:' + str(pos_size)
    print 'order_size:' + str(order_size)
    # debug print end
def generate_random():
    """
    Generate random number and trigger order
    """
    random.seed()
    if random.random() > PROBABILITY_LONG: # go long

    else: # go short


def initialize(account):
    """
    Is launched once
    """
    if KILL_OPEN_ORDERS_ON_INIT:
        account.kill_open_orders('futures')
        print ('killing all opened orders')
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
    print ('Initialized account "%s" successfully:') % (account.name)
    print ('**********************************************************')
    print ('now print account property after init')
    for key, value in account.account_info.items():
        print (str(key) + ":" + str(value))
    print ('Current opened positioned:')
    for _positionobject in account.current_positions:
        # aggregate current and opened positions by instrument name
        position_aggregate(_positionobject, account.open_orders)
        # Code below might be changed to logging
        print ('**********************************************************')
        for _k, _v in _positionobject.__dict__.items():
            print _k, _v
    print (30*"*")
    print ('Current opened orders:')
    for _orderobject in account.open_orders:
        print ('**********************************************************')
        for _k, _v in _orderobject.__dict__.items():
            print _k, _v

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
                    # call generate order
                    pass
                elif _p.size_status == 2 or _p.size_status == -2:
                     #if we are in full position
                    # call check profitability status and probably send close signal
                    pass
                elif _p.size_status == 1 or _p.size_status == -1:
                    #if we are still have some orders placed
                    # call determine what to do with the orders
                    pass
def main():
    """
    main function
    """
    account_deribit = DeribitAccount('main_account', 'BTC')
    initialize(account_deribit)



if __name__ == "__main__":
    main()
