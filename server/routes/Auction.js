import express from 'express';
import queries from '../db/queries';
const router = express.Router();

router.post('/register', (req, res) => {
    // console.log(req)
    queries.Auction.register(req.query.user_name)
})
router.get('/getItemInfo', (req, res) => {
    queries.Auction.getItemInfo().then(data =>{
        res.json(data)
    })
})

module.exports = router;