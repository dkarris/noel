"""
Module docstring
"""

from noelclasses import Account, Position, Transaction

global in_trade_position
global balance
def initialize(account):
    """
    Is launched once
    """
    # Get account details
    account_details = account.get_account_info()
    


    # Find all opened positions
    current_position_orders = account_deribit.get_current_positions()
    current_open_orders = account_deribit.get_open_orders()
    # move to config
    kill_open_orders_on_init = True
    if kill_open_orders_on_init:
        # kill open orders
        pass
    # set flag if we are in trade position
    if (current_position_orders>0) or (current_open_orders>0):
        account.in_trade_position = True
    else:
        account.in_trade_position = False

    print ('Initialized account "%s" successfully:') % (account.name)
    print ('Current opened positioned:')
    for index,obj in enumerate(current_position_orders):
        print ("Position:" + str(index+1))
        for key,value in obj.items():
            print (str(key) + ":" + str(value))





    # print ('current open orders: %s') % (current_open_orders)
    print ('**********************************************************')
def main(account):
    """
    Main body loop
    """
    keep_running = True
    while keep_running:
        pass

account_deribit = Account('main_account','BTC')

initialize(account_deribit)
main(account_deribit)
