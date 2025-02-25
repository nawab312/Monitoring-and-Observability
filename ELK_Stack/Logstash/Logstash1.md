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
    stdout{ codec => rubydebug }
}
```

Go to path `/home/siddharth312/ELK_Stack/logstash-8.17.1/bin`
```bash
./logstash -f /home/siddharth312/ELK_Stack/logstash.conf
```

After Logstash starts running, type some input in the terminal (such as Hello, Logstash!) and press Enter. Logstash will process this input and output the data along with the added field `added_field`.
```bash
Hello, Logstash!
{
    "added_field" => "Test field added",
       "@version" => "1",
        "message" => "Hello, Logstash!",
     "@timestamp" => 2025-02-25T05:32:35.993492407Z,
          "event" => {
        "original" => "Hello, Logstash!"
    },
           "host" => {
        "hostname" => "siddharth312-GF65-Thin-9SD"
    }
}
```

