
exports.up = function(knex, Promise) {
    return AddCurrentPriceColumn()

    function AddCurrentPriceColumn() {
        return knex.schema.table('Item', function (table) {
            table.integer('current_price').notNull().defaultTo(0);
        });
    }
};

exports.down = function(knex, Promise) {
    knex.schema.table('Item', function(t) {
        t.dropColumn('current_price');
    });
};
