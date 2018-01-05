"""
Module docstring
"""

from noelclasses import Account, Position, Transaction

def initialize(account):
    """
    Is launched once
    """
    # TODO move to config
    kill_open_orders_on_init = True
    bet_amount = 4000 # in futures contracts where 1 contract = 10 usd
    # Get account details
<<<<<<< HEAD
    account_details = account.get_account_info()
    # Find all opened positions


    # TODO move retrieval of positions by instrument to Account Method
    # now the assumption is that only one instrument is traded and
    # all open posiitons are on one side and can't be sell and buy at the same
    # time
    current_position_orders = account_deribit.get_current_positions()[0]
    current_open_orders = account_deribit.get_open_orders()[0]

=======
    account_info = account.get_account_info()
    # Find all opened positions
    current_position_orders = account_deribit.get_current_positions()
    current_open_orders = account_deribit.get_open_orders()
    # move to config
    kill_open_orders_on_init = True
>>>>>>> 0a718dbc668634f5ab443721bd26a038b5c32ce1
    if kill_open_orders_on_init:
        # kill open orders
        pass

    # set flag if we are in trade position
<<<<<<< HEAD
    # assumption that if we are short then we
    if current_position_orders['direction'] == 'sell' and
        current_open_orders['direction']:
            account.state = -1






    if (current_position_orders>0) or (current_open_orders>0):
=======
    if (current_position_orders > 0) or (current_open_orders > 0):
>>>>>>> 0a718dbc668634f5ab443721bd26a038b5c32ce1
        account.in_trade_position = True
    else:
        account.in_trade_position = False

    print ('Initialized account "%s" successfully:') % (account.name)
    print ('Current opened positioned:')
    for index, obj in enumerate(current_position_orders):
        print ("Position:" + str(index+1))
        for key, value in obj.items():
          print (str(key) + ":" + str(value))
    # print ('current open orders: %s') % (current_open_orders)
    print ('**********************************************************')
    print ('now print account property after init')
    for key, value in account.account_info.items():
        print (str(key) + ":" + str(value))


def main(account):
    """
    Main body loop
    """
    keep_running = True
    while keep_running:
        pass

account_deribit = Account('main_account', 'BTC')
initialize(account_deribit)
<<<<<<< HEAD
#main(account_deribit)
=======
# main(account_deribit)
>>>>>>> 0a718dbc668634f5ab443721bd26a038b5c32ce1
