import knex from './knex';
import moment from 'moment'

module.exports = {
    Auction: {
        checkClientName: function(name){
            const client = knex('Client').where({client_name: name})
            return client
        },
        register: function(name) {
            return knex('Client').insert({client_name: name})
        },
        getItemInfo: function() {
            // const curDate =  moment().add(1, 'day').format('YYYY-MM_DD')
            // const nextMonDate = moment().add(1, 'month').format('YYYY-MM_DD')
            const item = knex('Item').where({id: 1})
            return item
        }    
    }
}