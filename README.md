# auctiOnS
Distributed Auction System

## meeting minutes
[2019 02 12](meetings/20190212.md)

[2019 02 19](meetings/20190219.md)

[2019 02 25](meetings/20190225.md) Design Document 
 
[2019 03 04](meetings/20190304.md) Design Document updates

## System Structure

## Implementations

### Server
The server is implemented using `Node.js`,`Express`, `Knex` and `MySQL` as the database.

The server provides 2 APIs for the client to call. These APIs are implemented in `server/db/queries`.

`/getItemInfo`: get the current item information

```javascript
getItemInfo: function() {
  const item = knex('Item').where({id: 1})
  return item
}
```

`/bidding`: Post a bid to the server, then the server will check whether the current price is matched with database,
if true, then compared the bidding price, otherwise reject the bidding request and send most updated infomation to
the client.

```javascript
bidding: function(name, client_current_price, num_mi) {
  return new Promise ((resolve, reject) => {
      knex.transaction( async function(t){
          try {
              const server_id = 0
              const item = await knex('Item').where({id: 1})
              const current_price = item[0].current_price
              const mi = item[0].min_increment
              const bid_price = parseInt(client_current_price) + parseInt(num_mi) * item[0].min_increment
              const data_from_client = {'type': 'request', 
                                        'username' : name , 
                                        'current_price' : client_current_price, 
                                        'mi': mi,'num_mi' : num_mi, 
                                        'server_id': server_id}
              await knex('Logs').insert({'logs': JSON.stringify(data_from_client)})

              if (bid_price > current_price && current_price < item[0].bin_price) {
                  console.log('Succesful bid')
                  const data = {'type': 'response', 
                                'current_price' : bid_price, 
                                'current_owner' : name, 
                                'mi': mi,'accept': true, 
                                'server_id': server_id}
                  await knex("Item").where({id: 1}).update({current_owner: name, current_price: bid_price})
                  await knex('Logs').insert({'logs': JSON.stringify(data)})
                  return resolve(data)
              }
              else {
                  console.log('Unsuccessful bid')
                  const data = {'type': 'response', 
                                'current_price' : current_price, 
                                'current_owner' : item[0].current_owner, 
                                'mi': mi,'accept': false, 
                                'server_id': server_id}
                  await knex('Logs').insert({'logs': JSON.stringify(data)})
                  return reject(data)
              }
          }
          }
      })
  })
} 
```

### Client

Client will have a username, budget, and the address of the server. The client will continuously update item info from the server. After received info, it will
decide whether to bid or not by the random algorithm with parameters like current price. If the client decided to bid, it sends a bidding request through /bidding route
and the server will repsonse whether the bidding is accepted or rejected.

#### Client functions

```bid {}``` : Used to decide thether to bid or not.

```bidding()``` : The loop which is executed untill the auction is closed or the client is run ot of money.


#### Client bidding algorithm
During bidding, after check and updating the local listing information with the server, the client will use a randomized algorithm to decide whether to make a higher bid or not. 

The current algorithm increases the bid by a weighted probability of 0x - 5x of minimum increment, among these, 1x has the highest probability, 2x next, then 3x, 4x, 5x, and 0x last, which means not to bid. This algorithm is implemented as `bid` and `select_num_mi` functions in `client.py`.

The bid amount is decided in discrete multiple of the minimum increment amount, however, this constrain is based on the current algorithm, in a different algorithm the client may choose to out-bid with any amount, as long as it's above the required minimum increment.





### Getting Started
In order to run the server, make sure that you have [Node](https://nodejs.org/en/) version 6.0.0 or higher.

First we have to go into the `server` directory to install all the dependencies.
```
$ cd server/
```
```
$ npm install
```
### Start the server
Inside the `server` directory simply run
```
$ npm start
```
The server will now run at `localhost:3001`


### Start the client
```
$ python3 client.py -u username -b budget -a server_url
```
## (Daniel) Result
