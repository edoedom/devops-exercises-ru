<a id="aws-auto-scaling-groups---basics"></a>
## AWS Auto Scaling Groups: основы

<a id="requirements"></a>
### Требования

Отдельная учебная группа и две подсети выбранной VPC с доступом к репозиториям пакетов. Чужие экземпляры останавливать не нужно. Ресурсы могут тарифицироваться.

<a id="objectives"></a>
### Задание

A. Создайте группу масштабирования веб-серверов:

* Образ Amazon Linux 2023 x86_64 AMI.
* Тип экземпляра: t3.micro.
* Данные инициализации (user data):

```bash
#!/bin/bash
set -euo pipefail
dnf install -y httpd
printf '%s\n' 'healthy' > /var/www/html/index.html
systemctl enable --now httpd
```

B. Появились ли новые экземпляры после создания группы? Сколько и почему?

C. Установите желаемое количество экземпляров равным 2. Запустились ли дополнительные экземпляры?

D. Верните желаемое количество к 1. Что произошло?

### Проверка и завершение

Явно задайте min=1, desired=1, max=3. Запуск до desired зависит от квот и доступной ёмкости. Для ALB используйте две зоны доступности, listener HTTP/80 и target group с health check `/`; разрешите HTTP к экземплярам только от группы безопасности ALB. Задайте grace period с учётом установки пакетов. После изменений смотрите Activity history и здоровье targets, а не только число Running. Удалите учебную ASG, ALB, target group и launch template после выполнения; уменьшение desired до нуля требует также min=0.
