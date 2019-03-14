import knex from './knex';
import moment from 'moment'
import { rejects } from 'assert';

module.exports = {
    Auction: {
        register:  function(name) {
            return new Promise (async (resolve, reject)=>{
                try{
                    name = 'James'
                    const client = await knex('Client').where({client_name: name})
                    if(client.length) {
                        reject(null)
                    }
                    else {
                        await knex('Client').insert({client_name: name})
                        resolve()
                    }
                }
                catch(e){
                    console.log(e)
                }
            })
        },
        getItemInfo: function() {
            const item = knex('Item').where({id: 1})
            return item
        },
        getLogs: function() {
            const logs = knex.select().from('Logs')
            return logs
        },
        bidding: function(name, client_current_price, num_mi) {
            return new Promise ((resolve, reject) => {
                knex.transaction( async function(t){
                    try {
                        const server_id = 1
                        const item = await knex('Item').where({id: 1})
                        const current_price = item[0].current_price
                        const bid_price = parseInt(client_current_price) + parseInt(num_mi) * item[0].min_increment
                        const data_from_client = {'type': 'request', 'username' : name , 'current_price' : client_current_price, 'num_mi' : num_mi, 'server_id': server_id}
                        await knex('Logs').insert({'logs': JSON.stringify(data_from_client)})

                        if (bid_price > current_price && current_price < item[0].bin_price) {
                            console.log('Succesful bid')
                            const data = {'type': 'response', 'current_price' : bid_price, 'current_owner' : name, 'accept': true, 'server_id': server_id}
                            await knex("Item").where({id: 1}).update({current_owner: name, current_price: bid_price});
                            await knex('Logs').insert({'logs': JSON.stringify(data)})
                            return resolve(data)
                        }
                        else {
                            console.log('Unsuccessful bid')
                            const data = {'type': 'response', 'current_price' : current_price, 'current_owner' : item[0].current_owner, 'accept': false, 'server_id': server_id}
                            await knex('Logs').insert({'logs': JSON.stringify(data)})
                            return reject(data)
                        }
                    }
                    catch(e) {
                        console.log(e)
                    }
                })
            })
        }  
    }
}
