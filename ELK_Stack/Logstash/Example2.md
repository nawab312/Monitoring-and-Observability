### View Logs in a File ###

Create `logstash.conf` at path `/home/siddharth312/ELK_Stack`
```bash
#logstash.conf
input {
    stdin { }
}

filter {
    mutate {
        add_field => { "added_field" => "Test field added" }
    }
}

output {
    file {
        path => "/home/siddharth312/ELK_Stack/output.log"
    }
}
```

Go to path `/home/siddharth312/ELK_Stack/logstash-8.17.1/bin`
```bash
./logstash -f /home/siddharth312/ELK_Stack/logstash.conf
```

After Logstash starts running, type some input in the terminal (such as Siddharth or Singh). Logstash will process this input and save the output in output.log
```bash
#output.log
{"event":{"original":""},"@version":"1","message":"","host":{"hostname":"siddharth312-GF65-Thin-9SD"},"added_field":"Test field added","@timestamp":"2025-02-25T05:35:40.697756177Z"}
{"event":{"original":"Siddharth"},"@version":"1","message":"Siddharth","host":{"hostname":"siddharth312-GF65-Thin-9SD"},"added_field":"Test field added","@timestamp":"2025-02-25T05:35:46.526707895Z"}
{"event":{"original":"Singh"},"@version":"1","message":"Singh","host":{"hostname":"siddharth312-GF65-Thin-9SD"},"added_field":"Test field added","@timestamp":"2025-02-25T05:36:00.839776933Z"}
```
