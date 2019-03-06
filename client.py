import os, sys, time
import requests as req
import argparse
from random import randint

class client(object):
    def __init__(self, username, budget, server):
        self.username           = username          # username for this client
        self.budget             = budget            # current budget of the client, part of bidding decision factor
        self.item_name          = None              # current item id that's in auction
        self.current_price      = None              # current bid amount
        self.current_owner      = None          # current highest bid holder, a client id d
        self.increment          = None           # current increment of the item under auction
        self.n_increment        = None          # number of increment
        self.bin_price          = None
        self.SERVER             = server
        print(f'''
                Username:{self.username}
                Budget: {self.budget}
                Server: {self.SERVER}
                ''')
        

    def show(self):
        # show client status
        print(f'''
        	Item: 		        {self.item_name}
        	Current price: 		{self.current_price}
        	Current bid owner: 	{self.current_owner}
        	Current increment: 	{self.increment}
        	''')
    # Registers this user to server.
    def register(self):
        self.receive(req.post(self.SERVER + '/register', data={'username' : self.username}).json())

    # (TODO) Decides whether to bid.
    def bid(self):
        if self.current_owner == self.username or \
                self.budget < self.current_price + self.increment:
            return False
        else:
            return True

    # (TODO) Executes the loop to decide to bid or go to sleep. 
    def bidding(self):
        while self.receive('update', req.get(self.SERVER + '/getItemInfo').json()) is not None:
            if self.bid():
                self.receive('bid', req.post(self.SERVER + '/bid', data={\
                        'username' : self.username, \
                        'current_price' : self.current_price, \
                        'num_mi' : self.num_mi}))
                print('Bid!') 
            else:
                time.sleep(3)
                print('No bid.')
        return

    # (TODO) Updates local information according to server response.
    def receive(self, operation, response):
        if not response:
            print('Error response received.')
            return None
        # Updates item information from server.
        else:
            print(response)
            self.current_price = response['current_price']
            self.current_owner = response['current_owner']
            if 'update' in operation:
                print('getItemInfo')
                self.bin_price = response['bin_price']
                self.increment = response['increment']
                self.show()
    	    ## Handles bidding response.
            elif 'bid' in operation:
                if response['accept']:
                    print('Bid accept')
                else:
                    print('Bid reject')
            else:
                print('Unknow operation.')

def process_commands():
    parser = argparse.ArgumentParser(description="Client of auctiOnS.")
    parser.add_argument('--username', '-u', help='Name of this client.', required=True)
    parser.add_argument('--budget', '-b', help='budget of this client', required=True)
    parser.add_argument('--address', '-a', help='IP address of the server.', required=True)
    return parser.parse_args()

if __name__ == '__main__':
    args = process_commands()
    c = client(args.username, args.budget, args.address)
    #c.bidding()
