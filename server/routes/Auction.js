import express from 'express';
import queries from '../db/queries';
const router = express.Router();

router.post('/register', (req, res) => {
    queries.Auction.checkClientName(req.body.username).then(data => {
        if(data.length) {
            const d = {'op': 'register', 'success': false, 'server_id': 0}
            res.json(d)
        }
        else {
            queries.Auction.register(req.body.username).then(data => {
                const d = {'op': 'register', 'success': true ,'server_id': 0}
                res.json(d)
            })
        }
    })
})
router.get('/getItemInfo', (req, res) => {
    queries.Auction.getItemInfo().then(data => {
        res.json(data[0])
    })
})

module.exports = router;