
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
        return knex.schema.createTable('Logs', function (table) {
            table.increments('id').primary().unsigned();
            table.timestamp('time').defaultTo(knex.fn.now());
            table.json('logs');
        });
    }
};

exports.down = function(knex, Promise) {
    knex.raw('SET foreign_key_checks = 0;'),

    knex.schema.dropTable('Logs'),

    knex.raw('SET foreign_key_checks = 1;')
};