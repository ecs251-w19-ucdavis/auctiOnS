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
`Node.js` `Express` `Knex` `MySQL`

### Client


#### (TODO: Daniel) Client functions

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
