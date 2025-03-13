### NodeJS App for Generating Logs ###

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
- Create **Dockefile** https://github.com/nawab312/Monitoring-and-Observability/blob/main/ELK_Stack/Projects/Project2/Dockerfile
  ```bash
  docker build -t sid3121997/log-generator-app:nodeJS_v3 .
  docker push sid3121997/log-generator-app:nodeJS_v3
  ```




