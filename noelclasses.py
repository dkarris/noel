"""
module class docstring
"""

# used for API class
import requests
from deribit_api import RestClient

#import secret key stuff here
TEST_URL = 'https://test.deribit.com'
KEY = '45Sxzh7sa1vN'
KEY_SECRET = 'CPQEV33KLU3KJ2OC3FGI4LKTBEJAHJB4'

#...
#...

#commented as it is not good approach
#from deribitapi import deribit_api


class Event(object):
    """
    Event class docstring
    """
    def __init__(self):
        pass

class Account(object):
    """
    Account class docstring
    """
<<<<<<< HEAD


    #TODO implement api init method to replace external deribit_api setup


    def __init__(self, name, currency, api=None, apisecret = None):
=======
    def __init__(self, name, currency, api=None, apisecret=None):
>>>>>>> 0a718dbc668634f5ab443721bd26a038b5c32ce1
        """
        Init object instance
        """
        self.name = name
        self.currency = currency
        self.api = api
        self.apisecret = apisecret
        self.enabletrade = False  # can't trade by default
<<<<<<< HEAD
        # self.state can be:
        # -2 - in short position all orders executed
        # -1 -  in short position, orders replaced
        # 0 - out of position
        # +1 in long position, orders replaced
        # +2 in long position, all orders executed
        self.state = 0
        self.init_api()


    def init_api(self):
        self.api = RestClient(KEY, KEY_SECRET, TEST_URL)

    def get_account_info(self):
        """
        execute API call for account account_details
        returns object with account details
=======
        self.in_trade_position = True
        self.account_info = self.get_account_info() # get initial account parameters
    
    @staticmethod
    def get_account_info():
        """
        execute API deribit call for account_details
        returns JSON with account details
>>>>>>> 0a718dbc668634f5ab443721bd26a038b5c32ce1
        """
        return self.api.account()

<<<<<<< HEAD
    def get_current_positions(self):
=======
    @staticmethod
    def get_current_positions():
>>>>>>> 0a718dbc668634f5ab443721bd26a038b5c32ce1
        """
        Call deribit API and return current positions
        """
        # Call deribit API
        return self.api.positions()

    def get_open_orders(self):
        """
        Call deribit API and reurn opened and reserved get_open_orders
        """
        # call deribit api
        return self.api.getopenorders()

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


class Position(object):
    """
    aaa
    """
    def __init__(self, id_number, account, openprice, pos_type,
                 opentimedate, required_amount, lot_size):
        """
        pos_type = Long / Short
        account = class Account (object)
        required amount = maximum amount of contracts
        lot_size - send orders of that order size
        """
        self.id_number = id_number
        self.openprice = openprice
        self.type = pos_type
        self.opentimedate = opentimedate
        self.account = account
        self.lot_size = lot_size
        # This is amount we need to purchase/sell
        self.required_amount = required_amount
        # This is current amount we executed. required_amount - current_amount = amount to order
        self.current_amount = 0
        # flag to check that we still in opening position mode
        self.executed = False

    def amount_to_open_remaining(self):
        """
        returns amount of contacts still remaining to purchase
        """
        return self.required_amount-self.current_amount

    def check_execution(self):
        """
        if position is executed, set flag executed True and return True
        Else return False
        """
        print (self.amount_to_open_remaining())
        if self.amount_to_open_remaining() == 0:
            self.executed = True
            return True
        return False


class Transaction(object):
    """
    Class docstring
    """
    def __init__(self):
        """
        Method docstring
        """
        pass




# # this class is replaced with the original deribit_api client
# class DeribitAPI(object):
#     """
#     API docstring
#     """
#     # @classmethod
#     # def __init__(cls):
#     #     """
#     #     DeribitAPI constructor
#     #     """
#     #     cls.baseurl = 'https://www.deribit.com'
#
#     baseurl = 'https://www.deribit.com'
#
#     # @classmethod
#
#     @staticmethod
#     def test_api():
#         """
#         test API. Returns API response in JSON
#         """
#         endpoint = DeribitAPI.baseurl + '/api/v1/public/test'
#         print (endpoint)
#         return requests.get(endpoint).json()
