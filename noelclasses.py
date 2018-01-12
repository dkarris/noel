"""
module class docstring
"""

# used for API class
from deribitapi import deribit_api

class Event(object):
    """
    Event class docstring
    """
    def __init__(self):
        pass

class Account(object):
    """
    Base account class docstring
    """
    def __init__(self, name, currency):
        """
        Init object instance
        """
        self.name = name
        self.currency = currency
        self.enabletrade = False  # can't trade by default
        self.in_position = False
        self.open_orders = None # will be set up by initialize function
        self.current_positions = None # will be set up by initialize function

class DeribitAccount(Account):
    """
    DeribitAccount inhereted from Account object
    Deribit API added
    """
    def __init__(self, name, currency):
        super(DeribitAccount, self).__init__(name, currency)
        self.account_info = self.get_account_info()

    @staticmethod
    def get_account_info():
        """
        execute API deribit call for account_details
        returns JSON with account details
        """
        # TODO build error handling if deribit_api.account returns error
        return deribit_api.account()

    @staticmethod
    def get_current_positions(*args, **kwargs):
        """
        Call deribit API and return current positions
        """
        return deribit_api.positions(*args, **kwargs)

    @staticmethod
    def get_open_orders(*args, **kwargs):
        """
        Call deribit API and reurn opened and reserved get_open_orders
        """
        return deribit_api.getopenorders(*args, **kwargs)

    @staticmethod
    def kill_open_orders(order=None):
        """
        Call deribit API and kill orders outstanding
        """
        if not order:
            return deribit_api.cancelall()
        else:
            if type(order) is int:
                try:
                    return deribit_api.cancel(order)
                except Exception:
                    print ('no order with id:' + str(order))
                return 
            else:
                try:
                    return deribit_api.cancelall(order)
                except Exception:
                    print ('caught exception when trying execute' + 
                           ' order cancel type:' + str(order)) 
    @staticmethod
    def deposit_money():
        """
        Transfer money from exchange to account
        """
        pass

    @staticmethod
    def withdraw_money():
        """
        Withdraw from account to exchange
        """
        pass

class BitMexAccount(Account):
    """
    Future subclass for BitMex
    """
    pass
    #raise NotImplementedError


class OpenPosition(object):
    """
    Base Position class
    """
    def __init__(self, account, instrument, price, pos_type,
                 size, kind=None, opentimedate=None):
        """
        pos_type = Long / Short
        account = class Account (object)
        required amount = maximum amount of contracts
        lot_size - send orders of that order size
        """
        # self.id_number = id_number
        self.kind = kind
        self.instrument = instrument
        self.account = account
        self.price = price
        self.type = pos_type
        self.opentimedate = opentimedate
        self.account = account
        self.size = size
        self.executed = False

class OpenOrder(object):
    """
    Order base class
    """

    def __init__(self, order_id, instrument, pos_type, price, size,
                 account, fullfilledsize, timestamp=None):
        """
        Method docstring
        """
        self.order_id = order_id
        self.timestamp = timestamp
        self.instrument = instrument
        self.type = pos_type
        self.price = price
        self.size = size
        self.fullfilledsize = fullfilledsize
        self.account = account
class Transaction(object):
    """
    Transaction base class docstring
    """
    def __init__(self):
        """
        Method docstring
        """
        pass
