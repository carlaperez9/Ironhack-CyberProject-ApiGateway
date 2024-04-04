const express = require('express'); 
const mysql   = require('mysql'); 
const app = express(); 

const pool = mysql.createPool({
    host: 'localhost', 
    user: 'project1', 
    password: 'Ironhack-2024-jmc!', 
    database: 'users'
})

app.use( express.json() )
 
// app.get('/tshirt', (req, res) => { 
//     res.status(200).send({
//         tshirt: 'tshirt',
//         size: 'large'
//     })
// }); 

// http://localhost:3306/our_endpoint

app.post('/:email', (req, res) => { 
    const { email }   = req.params; 
    const { input } = req.body;  
    // input = { 
    //     "input": "this is an input?"
    // }
    
    const query = `UPDATE customers SET input = ? WHERE email = ?`; 

    pool.query(query, [input, email], (error, results)=> { 
        if (error) {
            res.status(500).send({ message: 'Error updating input field' });
            return;
        }

        res.send({
            message: `Input field created for customer with email ${email}`
        });
    });
});