import os, sys
import requests

class client(object):
    def __init__(self):
        self.client_id          = None
        self.account_balance    = 10000.0
        self.current_listing    = None

    def set_balance(self, amount):
        self.account_balance = amount

    def check_listing(self):
        # send chk request, receive
        pass

    def register(self):
        # send register request (reg), wait for confirmation, set client_id
        pass

    def bid(self):
        # check current listing, decide, send bid request (bid) with [item#, price, client_id], receive succ/fail from server
        pass

    def receive(self):
        # wait for http response
        # registration confirmation
        # check listings
        # bid accept
        # bid fail
        # new item notification
        pass