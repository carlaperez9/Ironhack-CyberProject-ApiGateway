const mysql = require('mysql');

// Configuration for MySQL connection
const dbConfig = {
  host: 'YOUR_MYSQL_HOST',
  user: 'YOUR_MYSQL_USER',
  password: 'YOUR_MYSQL_PASSWORD',
  database: 'YOUR_DATABASE_NAME'
};

// Create a connection pool
const pool = mysql.createPool(dbConfig);

exports.handler = async (event, context) => {
  // Define your API response headers
  const headers = {
    'Content-Type': 'application/json',
    'Access-Control-Allow-Origin': '*'
  };

  try {
    // Retrieve data from MySQL database
    const customers = await queryDatabase('SELECT * FROM customers');

    // Return the retrieved data as a response
    return {
      statusCode: 200,
      headers,
      body: JSON.stringify(customers)
    };
  } catch (error) {
    // If an error occurs, return an error response
    return {
      statusCode: 500,
      headers,
      body: JSON.stringify({ message: 'Internal server error' })
    };
  }
};

// Function to query the MySQL database
function queryDatabase(query) {
  return new Promise((resolve, reject) => {
    pool.query(query, (error, results) => {
      if (error) {
        reject(error);
      } else {
        resolve(results);
      }
    });
  });
}
