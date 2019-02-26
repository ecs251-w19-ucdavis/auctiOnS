import express from 'express';
import queries from '../db/queries';
const router = express.Router();

router.get('/getItemInfo', (req, res) => {
    queries.Auction.getItemInfo().then(data =>{
        res.json(data);
    })
});

module.exports = router;