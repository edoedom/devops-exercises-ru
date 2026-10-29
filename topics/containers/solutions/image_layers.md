<a id="layer-by-layer"></a>
## Слой за слоем

<a id="objective"></a>
### Цель

Разобраться в слоях образа.

<a id="requirements"></a>
### Требования

Убедитесь, что Docker установлен и служба запущена.

```
# Fedora/RHEL/CentOS
rpm -qa | grep docker
systemctl status docker
```

<a id="instructions"></a>
### Инструкции

1. Напишите любой корректный Dockerfile:

```
FROM ubuntu
EXPOSE 212
ENV foo=bar
WORKDIR /tmp
RUN dd if=/dev/zero of=some_file bs=1024 count=0 seek=1024
RUN dd if=/dev/zero of=some_file bs=1024 count=0 seek=1024
RUN dd if=/dev/zero of=some_file bs=1024 count=0 seek=1024
```

2. Соберите образ:

`docker image build -t super_cool_app:latest .`

3. Какие инструкции создают слои, а какие добавляют метаданные?

```
FROM, RUN -> new layer
EXPOSE, ENV, WORKDIR -> metadata
```

4. Как проверить ответ?

Выполните `docker image history super_cool_app`: команда показывает инструкции и связанный с ними размер. Ненулевой размер часто указывает на изменение файловой системы, но полагаться только на него нельзя: например, RUN с `ls -l` может показывать нулевой размер.

Также в оригинале предлагается `docker image inspect super_cool_appl`: в разделе RootFS можно посмотреть количество слоёв и сопоставить их с инструкциями.

> Примечание к переводу: в имени образа последней команды исходника лишняя буква l. Используйте имя реально созданного образа — super_cool_app.

5. Можно ли уменьшить размер образа?

Да. Например, объедините инструкции RUN:

`RUN dd if=/dev/zero of=some_file bs=1024 count=0 seek=1024 && dd if=/dev/zero of=some_file bs=1024 count=0 seek=1024 && dd if=/dev/zero of=some_file bs=1024 count=0 seek=1024`

В данном примере выигрыш может быть небольшим, но в других случаях объединение связанных операций заметно уменьшает образ.
