import os, sys, time
import requests as req

class client(object):
    def __init__(self, name):
        self.username           = name          # username for this client
        self.server_id          = None          # which server the client is connect to
        self.account_balance    = 10000.0       # current balance of the client, part of bidding decision factor
        self.current_item       = None          # current item id that's in auction
        self.current_price      = None           # current bid amount
        self.current_bid_owner  = None          # current highest bid holder, a client id d
        self.minimum_increment  = 0.0           # current minimum increment of the item under auction
        self.register()
        

    def show(self):
        # show client status
        print(f'''
        	client id: 		{self.username}
        	account balance:	{self.account_balance}
        	current server: 	{self.server_id}
        	current item: 		{self.current_item}
        	current price: 		{self.current_price}
        	current bid owner: 	{self.current_bid_owner}
        	current MI: 		{self.minimum_increment}
        	''')
    # Registers this user to server.
    def register(self):
        self.receive(req.post('http://localhost:3001/register', data={'username' : self.username}).json())

    def check(self):
        # send chk request, receive
        r = requests.get('https://google.com/')
        # self.receive(r)
        self.receive('check')

    # (TODO) Decides whether to bid.
    def bid(self):
        return

    # (TODO) Executes the loop to decide to bid or go to sleep. 
    def bidding(self):
        #while self.current_price < self.account_balance:
        #    self.update_info()
        #    payload = self.bid()
        #    if payload is not None:
        #        r = requests.get('server.com/', params=payload)
        #    else:
        #        print(self.current_price, self.account_balance)
        #        time.sleep(5)
        #self.show()
        return

    # (TODO) Updates local information according to server response.
    def receive(self, response):
        # parse response
        if not response:
            print('Error response received.')
            return
        op = response['op']
        # registration confirmation
        if op == 'register':
            self.server_id = response['server_id']
        # check listings, update internal information
        #elif op == 'check':
        #    self.current_price = response['cur_price']
        #    self.current_bid_owner = response['cur_bid_owner']
        #    self.minimum_increment = response['MI']
    	## bid accept
        #elif op == 'bid':
        #    self.current_item_owner = response['cur_item_owner']
        #    self.current_price = response['cur_item_price'] # my_price should be parse from http response
    	## new item notification
        #elif op == 'new':
        #    self.current_item = 'new_item'
        #    self.current_price = 1000
        #    self.current_bid_owner = 'current_bid_owner'
        #    self.minimum_increment = 'MI'
        #    # update account balance if won the bid
        #    self.account_balance = 900

if __name__ == '__main__':
    c = client('test_name')
    c.register()
    #c.bidding()
