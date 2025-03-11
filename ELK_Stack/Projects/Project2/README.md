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

- `app.js` https://github.com/nawab312/Monitoring-and-Observability/blob/main/ELK_Stack/Projects/Project2/app.js
- If you run app.js `node app.js`, It will store logs on path `logs/app.log`
- Type this in URL `http://localhost:3001/log?level=info&message=HelloSiddy`
- Go to `logs/app.log`
  ```bash
  {"level":"info","message":"Generated log at 2025-03-11T15:41:08.003Z","timestamp":"2025-03-11T15:41:08.004Z"}
  {"level":"info","message":"Generated log at 2025-03-11T15:41:13.004Z","timestamp":"2025-03-11T15:41:13.004Z"}
  {"level":"info","message":"HelloSiddy","timestamp":"2025-03-11T15:41:17.723Z"}
  {"level":"info","message":"Generated log at 2025-03-11T15:41:18.004Z","timestamp":"2025-03-11T15:41:18.004Z"}
  {"level":"info","message":"Generated log at 2025-03-11T15:41:23.005Z","timestamp":"2025-03-11T15:41:23.005Z"}
  {"level":"info","message":"Generated log at 2025-03-11T15:41:28.009Z","timestamp":"2025-03-11T15:41:28.009Z"}
  {"level":"info","message":"Generated log at 2025-03-11T15:41:33.013Z","timestamp":"2025-03-11T15:41:33.013Z"}
  ```

