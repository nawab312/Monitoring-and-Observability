**Fluentd Configuration (fluent.conf) Basics**

fluent.conf is the main configuration file for Fluentd. It defines how logs are collected, processed, and forwarded to different destinations. The configuration consists of three main sections:
- Input (`<source>`) – Defines where logs come from.
- Filter (`<filter>`) – Modifies or processes logs before sending them.
- Output (`<match>`) – Defines where logs should be sent.
