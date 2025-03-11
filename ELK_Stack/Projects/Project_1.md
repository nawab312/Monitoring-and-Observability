## Centralized Logging in Kubernetes with ELK and Fluentd ##

Centralized logging is crucial for monitoring and debugging applications running in Kubernetes. 
In a distributed system, logs from different services need to be collected, aggregated, and visualized efficiently.
The ELK stack (Elasticsearch, Logstash, Kibana) is a powerful solution for this purpose, and Fluentd is used as a log forwarder.

**Architecture Overview**
- Application Pod: A simple NodeJS Ap that generates structured JSON logs.
- Fluentd DaemonSet: Collects logs from all pods in the cluster.
- Logstash: Processes and transforms logs before sending them to Elasticsearch.
- Elasticsearch: Stores logs for querying and analysis.
- Kibana: Provides a UI to visualize logs in Elasticsearch.

### Creating the NodeJS App and the Deployment for it ###

```bash
npm init -y
touch app.js
```

```js
const express = require("express");
const winston = require("winston");
const fs = require("fs");
const path = require("path");

const app = express();
const port = 3001;

// Ensure the logs directory exists
const logDir = "logs";
if (!fs.existsSync(logDir)) {
    fs.mkdirSync(logDir);
}

// Configure Winston for structured JSON logs and file storage
const logger = winston.createLogger({
    level: "info",
    format: winston.format.combine(
        winston.format.timestamp(),
        winston.format.json()
    ),
    transports: [
        new winston.transports.Console(), // Logs to console
        new winston.transports.File({ filename: path.join(logDir, "app.log") }) // Logs to file
    ],
});

// API endpoint to generate logs
app.get("/log", (req, res) => {
    const level = req.query.level || "info";
    const message = req.query.message || "Default log message";

    switch (level.toLowerCase()) {
        case "error":
            logger.error(message);
            break;
        case "warn":
            logger.warn(message);
            break;
        case "debug":
            logger.debug(message);
            break;
        default:
            logger.info(message);
            break;
    }

    res.send(`Logged: ${message}`);
});

// Generate logs every 5 seconds
setInterval(() => {
    logger.info(`Generated log at ${new Date().toISOString()}`);
}, 5000);

// Start the server
app.listen(port, () => {
    console.log(`Log generator app listening at http://localhost:${port}`);
});
```
