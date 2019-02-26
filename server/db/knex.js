import config from './../knexfile';
import knex from 'knex';
const environment = process.env.NODE_ENV || 'development';

const environmentConfig = config[environment];
// console.log(environmentConfig)
const connection = knex(environmentConfig);

module.exports = connection;