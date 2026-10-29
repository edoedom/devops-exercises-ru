<a id="elk--filebeat"></a>
## ELK и Filebeat

Настройте следующую схему обработки любого выбранного журнала:

* Запустите Elasticsearch, Logstash, Kibana и Filebeat — каждый в отдельном контейнере.
* Настройте передачу журнала из Filebeat в Logstash для обработки.
* После обработки в Logstash проиндексируйте данные в Elasticsearch.
* Убедитесь, что данные доступны в Kibana.
