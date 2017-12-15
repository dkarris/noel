"""
module class docstring
"""

# used for API class
import requests



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
    def __init__(self, name, currency, api, apisecret):
        """
        Init object instance
        """
        self.name = name
        self.currency = currency
        self.api = api
        self.apisecret = apisecret
        self.enabletrade = False  # can't trade by default

    @staticmethod
    def get_total_balance():
        """
        aaa
        """
        pass

    @staticmethod
    def get_available_balance():
        """
        aaa
        """
        pass

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


class DeribitAPI(object):
    """
    API docstring
    """
    # @classmethod
    # def __init__(cls):
    #     """
    #     DeribitAPI constructor
    #     """
    #     cls.baseurl = 'https://www.deribit.com'

    baseurl = 'https://www.deribit.com'

    # @classmethod
    
    @staticmethod
    def test_api():
        """
        test API. Returns API response in JSON
        """
        endpoint = DeribitAPI.baseurl + '/api/v1/public/test'
        print (endpoint)
        return requests.get(endpoint).json()

