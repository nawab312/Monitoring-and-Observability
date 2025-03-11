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
