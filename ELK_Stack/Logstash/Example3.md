### Parsing Apache Logs with GROK ###

Create `logstash.conf` at path `/home/siddharth312/ELK_Stack`
```bash
input {
    file {
        path => "/var/log/apache2/access.log"
        start_position => "beginning"
    }
}

filter {
    grok {
        match => { "message" => "%{IP:client_ip}" }
    }
}

output {
    stdout {
        codec => rubydebug
    }
}
```

Go to path `/home/siddharth312/ELK_Stack/logstash-8.17.1/bin`
```bash
./logstash -f /home/siddharth312/ELK_Stack/logstash.conf
```

After Logstash starts running, Access the apache page by using `localhost`. Logstash will process this input and output the `client_ip` 
```bash
{
      "@version" => "1",
     "client_ip" => "127.0.0.1",
         "event" => {
        "original" => "127.0.0.1 - - [25/Feb/2025:11:20:42 +0530] \"GET / HTTP/1.1\" 200 3460 \"-\" \"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:135.0) Gecko/20100101 Firefox/135.0\""
    },
          "host" => {
        "name" => "siddharth312-GF65-Thin-9SD"
    },
           "log" => {
        "file" => {
            "path" => "/var/log/apache2/access.log"
        }
    },
       "message" => "127.0.0.1 - - [25/Feb/2025:11:20:42 +0530] \"GET / HTTP/1.1\" 200 3460 \"-\" \"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:135.0) Gecko/20100101 Firefox/135.0\"",
    "@timestamp" => 2025-02-25T05:50:43.083079491Z
}
```
