
exports.up = function(knex, Promise) {
    return removeForeignKeyChecks()
        .then(createClientTable)

    function removeForeignKeyChecks() {
        return knex.raw('SET foreign_key_checks = 0;');
    }

    function addForeignKeyChecks() {
        return knex.raw('SET foreign_key_checks = 1;');
    }

    function createClientTable() {
        return knex.schema.createTable('Client', function (table) {
            table.increments('id').primary().unsigned();
            table.text('client_name').notNullable();
        });
    }
};

exports.down = function(knex, Promise) {
    knex.raw('SET foreign_key_checks = 0;'),

    knex.schema.dropTable('Client'),

    knex.raw('SET foreign_key_checks = 1;')
};