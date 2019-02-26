
exports.up = function(knex, Promise) {
    return removeForeignKeyChecks()
        .then(createItemTable)

    function removeForeignKeyChecks() {
        return knex.raw('SET foreign_key_checks = 0;');
    }

    function addForeignKeyChecks() {
        return knex.raw('SET foreign_key_checks = 1;');
    }

    function createItemTable() {
        return knex.schema.createTable('Item', function (table) {
            table.increments('id').primary().unsigned();
            table.text('item_name').notNullable();
            table.text('current_owner').notNullable();
            table.integer('bin_price').notNullable();
            table.integer('min_increment').notNullable();
        });
    }
};

exports.down = function(knex, Promise) {
    knex.raw('SET foreign_key_checks = 0;'),

    knex.schema.dropTable('Auction'),

    knex.raw('SET foreign_key_checks = 1;')
};