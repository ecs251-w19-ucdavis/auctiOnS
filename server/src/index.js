import express from 'express';
import Auction from '../routes/Auction';
import bodyParser from 'body-parser';
import knex from 'knex';

const app = express();
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: false }));
app.use(Auction)


app.get('/', (req, res) => {
  res.status(200).json("Auction Backend" );
});

app.listen(process.env.PORT || 3001, () => console.log("Listening to port 3001"));