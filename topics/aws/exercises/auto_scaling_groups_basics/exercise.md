<a id="aws-auto-scaling-groups---basics"></a>
## AWS Auto Scaling Groups: основы

<a id="requirements"></a>
### Требования

Нет работающих экземпляров EC2.

<a id="objectives"></a>
### Задание

A. Создайте группу масштабирования веб-серверов:

* Образ Amazon Linux 2 AMI.
* Тип экземпляра: t2.micro.
* Данные инициализации (user data):

```
yum install -y httpd
systemctl start httpd
systemctl enable httpd
```

B. Появились ли новые экземпляры после создания группы? Сколько и почему?

C. Установите желаемое количество экземпляров равным 2. Запустились ли дополнительные экземпляры?

D. Верните желаемое количество к 1. Что произошло?
