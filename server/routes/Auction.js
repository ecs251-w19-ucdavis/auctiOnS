import express from 'express';
import queries from '../db/queries';
const router = express.Router();

router.post('/register', (req, res) => {
    queries.Auction.register(req.body.username).then(data => {
        const d = {'op': 'register', 'server_id': 0}
        res.json(d)
    })
})
router.get('/getItemInfo', (req, res) => {
    queries.Auction.getItemInfo().then(data => {
        res.json(data)
    })
})

module.exports = router;