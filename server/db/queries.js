import knex from './knex';
import moment from 'moment'

module.exports = {
    Auction: {
        register: function(name) {
            console.log(name)
            return name
        },
        getItemInfo: function() {
            // const curDate =  moment().add(1, 'day').format('YYYY-MM_DD')
            // const nextMonDate = moment().add(1, 'month').format('YYYY-MM_DD')
            const item = knex('Item').where({id: 2})
            return item
        }    
    }
}