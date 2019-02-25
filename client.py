import os, sys, time
import requests

class client(object):
    def __init__(self):
        self.client_id          = None          # id for this client
        self.server_id          = None          # which server the client is connect to
        self.account_balance    = 10000.0       # current balance of the client, part of bidding decision factor
        self.current_item       = None          # current item id that's in auction
        self.current_price      = 0.0           # current bid amount
        self.current_bid_owner  = None          # current highest bid holder, a client id d
        self.minimum_increment  = 0.0           # current minimum increment of the item under auction

        self.register()
        

    def show(self):
        # show client status
        print(f'''
        	client id: 			{self.client_id}
        	account balance:	{self.account_balance}
        	current server: 	{self.server_id}
        	current item: 		{self.current_item}
        	current price: 		{self.current_price}
        	current bid owner: 	{self.current_bid_owner}
        	current MI: 		{self.minimum_increment}
        	''')

    def set_balance(self, amount):
        self.account_balance = amount

    def check(self):
        # send chk request, receive
        r = requests.get('https://google.com/')
        # self.receive(r)
        self.receive('check')

    def register(self):
        # send register request (reg), wait for confirmation, set client_id
        r = requests.get('https://google.com/')
        # self.receive(r)
        self.receive('register')

    def bid(self):
        # decide whether to bid or not, send bid request (bid) with [item#, price, client_id], receive succ/fail from server
        if True:
            should_bid = True
        if should_bid:
            r = requests.get('https://google.com/')
            # self.receive(r)
            self.receive('accpet')

    def update(self):
        '''main loop, check listing, and try to bid'''
        count = 0
        while True:
            self.check()
            if self.current_price < self.account_balance:
                self.bid()
            else:
                print(self.current_price, self.account_balance)
                time.sleep(5)

            count += 1
            if count > 1:
                break
        self.show()

    def receive(self, response):
        # parse response
        mode = response
        my_price = 1001
        # registration confirmation
        if mode == 'register':
            self.client_id = 'temp_id'
            self.server_id = 'temp_server'
        # check listings, update internal information
        elif mode == 'check':
            self.current_price = 1000
            self.current_bid_owner = 'current_bid_owner'
            self.minimum_increment = 'MI'
    	# bid accept
        elif mode == 'accept':
            self.current_bid_owner = self.client_id
            self.current_price = my_price # my_price should be parse from http response
    	# new item notification
        elif mode == 'new':
            self.current_item = 'new_item'
            self.current_price = 1000
            self.current_bid_owner = 'current_bid_owner'
            self.minimum_increment = 'MI'
            # update account balance if won the bid
            self.account_balance = 900

if __name__ == '__main__':
    c = client()
    c.register()
    c.update()
