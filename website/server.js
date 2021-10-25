const express = require("express");
const next = require("next");

const dev = process.env.NODE_ENV !== "production";
const port = dev ? 3000 : 80;
const app = next({
  dev
});
const handle = app.getRequestHandler();

const fetch = require('node-fetch');

app.prepare().then(async () => {
  const server = express();

  // Parse JSON Data for API request body.
  server.use(express.json())

  server.post("/api/calculatecourses", async (req, res) => {

    if (!req.body) {
      res.json({
        success: false,
        errorMsg: "Invalid request body."
      });
    }

    var tracks = req.body;
    if (!tracks || !Array.isArray(tracks)) {
      res.json({
        success: false,
        errorMsg: "Invalid tracks given."
      });
      return;
    }

    await fetch("http://localhost:8081/calculatecourses", {
        method: "POST",
        body: JSON.stringify(tracks),
        headers: {
          'Content-Type': 'application/json'
        }
      })
      .then((response) => response.json())
      .then((jsonData) => {
        res.json({
          success: true,
          data: jsonData
        });
      }).catch((e) => {
        res.json({
          success: false,
          errorMsg: e.toString()
        });
      });

  });

  server.get("*", (req, res) => {
    return handle(req, res, "/");
  });

  server.listen(port, () => {
    console.log(`Success! Your application is running on port ${port}.`);
  });
});
