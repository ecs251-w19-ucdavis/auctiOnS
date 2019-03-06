import os, sys, time
import requests as req
from random import randint

SERVER = 'http://localhost:3001'


class client(object):
    def __init__(self, name):
        self.username           = name          # username for this client
        self.server_id          = None          # which server the client is connect to
        self.balance            = 10000.0       # current balance of the client, part of bidding decision factor
        self.item_name          = None          # current item id that's in auction
        self.current_price      = None           # current bid amount
        self.current_owner      = None          # current highest bid holder, a client id d
        self.min_increment      = None           # current minimum increment of the item under auction
        self.num_mi             = None          # number of minimum increment
        self.bin_price          = None
        

    def show(self):
        # show client status
        print(f'''
        	client id: 		{self.username}
        	account balance:	{self.balance}
        	current server: 	{self.server_id}
        	current item: 		{self.item_name}
        	current price: 		{self.current_price}
        	current bid owner: 	{self.current_owner}
        	current MI: 		{self.min_increment}
        	''')
    # Registers this user to server.
    def register(self):
        self.receive(req.post(SERVER + '/register', data={'username' : self.username}).json())

    # (TODO) Decides whether to bid.
    def bid(self):
        if self.current_owner == self.username or \
                self.balance < self.current_price + self.min_increment:
            return False
        else:
            max_inc = max(self.balance - self.current_price)
            self.num_mi = randint(1, (self.balance - self.current_price) // self.min_increment)
            return True

    # (TODO) Executes the loop to decide to bid or go to sleep. 
    def bidding(self):
        while self.receive(req.get(SERVER + '/getItemInfo').json()) is not None:
            if self.bid():
                self.receive(req.post(SERVER + '/bid', data={\
                        'username' : self.usernemae, \
                        'current_price' : self.current_price, \
                        'num_mi' : self.num_mi}))
                print('Bid!') 
            else:
                time.sleep(3)
                print('No bid.')
        return

    # (TODO) Updates local information according to server response.
    def receive(self, response):
        # parse response
        if not response:
            print('Error response received.')
            return None
        # registration confirmation
        print(response)
        if 'op' in response and response['op'] == 'register':
            self.server_id = response['server_id']
        # check listings, update internal information
        elif 'current_price' in response:
            print('getItem')
            self.current_price = response['current_price']
            self.current_owner = response['current_owner']
            self.bin_price = response['bin_price']
            self.min_increment = response['min_increment']
            self.show()
    	## bid accept
        #elif op == 'bid':
        #    self.current_item_owner = response['cur_item_owner']
        #    self.current_price = response['cur_item_price'] # my_price should be parse from http response
    	## new item notification
        #elif op == 'new':
        #    self.current_item = 'new_item'
        #    self.current_price = 1000
        #    self.cur_owner = 'cur_owner'
        #    self.minimum_increment = 'MI'
        #    # update account balance if won the bid
        #    self.account_balance = 900
        return True

if __name__ == '__main__':
    c = client('testname')
    c.register()
    #c.bidding()
