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
        bidding: function(name, current_price, num_mi) {
            return new Promise ((resolve, reject) => {
                knex.transaction( async function(t){
                    try {
                        const item = await knex('Item').where({id: 1})
                        const current_price = item[0].current_price
                        const bid_price = current_price + num_mi * item[0].min_increment

                        if (bid_price > current_price && current_price < item[0].bin_price) {
                            console.log('Succesful bid')
                            await knex("Item").where({id: 1}).update({current_owner: name, current_price: bid_price});
                            return resolve({'current_price' : bid_price, 'current_owner' : name, 'accept': true})
                        }
                        else {
                            console.log('Unsuccessful bid')
                            const d = {'current_price' : current_price, 'current_owner' : item[0].current_owner, 'accept': false}
                            return reject(d)
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