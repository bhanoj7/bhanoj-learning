const express = require('express'); //import express framework
const app = express(); //create an instance of express
const PORT = 5000;
app.use(express.json()) //middleware to parse JSON
// app.get is used to define a route for GET requests
// (req, res) is the request and response object
// The callback function is executed when the route is accessed
// In this case, it sends a simple text response
//'/' is used for the root route
app.get('/', (req, res) => {
  res.send('Hi Bhanoj');
}); // Root route
// Start the server

app.post("/api/data", (req, res) => {
    const receivedData = req.body;
    console.log("Received data:", receivedData);
    res.json({
        message: "Data received successfully",
        data: receivedData
    });
    //res.status(201).json({ message: "Data received successfully", data: receivedData });
});

app.listen(PORT, () => {
  console.log(`Server is running on http://localhost:${PORT}`);
});
