<a id="aws---launch-ec2-web-instance"></a>
## AWS: EC2 с веб-сервером — решение

Используйте [условия задания](exercise.md). Amazon Linux 2023 x86_64 совместим с выбранным t3.micro; ARM-образ для него не подходит.

### Консоль

Выберите регион, образ AL2023 x86_64, тип t3.micro и публичную подсеть. Включите публичный IPv4, настройте корневой диск и теги по заданию. Создайте отдельную группу безопасности в той же VPC: входящий TCP/80 из 0.0.0.0/0; исходящий доступ для загрузки пакетов. Проверьте также route table и NACL. Пару SSH-ключей создавать необязательно.

В User data вставьте содержимое [user-data.sh](terraform/user-data.sh), включая первую строку `#!/bin/bash`. Он выполняется от root, обычно только при первом запуске. После завершения cloud-init откройте HTTP-адрес экземпляра. При ошибке проверьте `/var/log/cloud-init-output.log` доступным в учебной среде способом.

### Terraform

[Полный модуль](terraform/main.tf) использует региональный AMI из публичного SSM-параметра, user data вместо SSH provisioner и группу безопасности выбранной VPC. Изменение user data заменяет экземпляр; обновление AMI может также привести к замене — смотрите plan.

В каталоге модуля укажите реальные регион и subnet_id:

```bash
terraform init
terraform plan -var='region=us-east-1' -var='subnet_id=subnet-REPLACE' -out=exercise.tfplan
terraform apply exercise.tfplan
terraform output -raw url
```

`subnet-REPLACE` — обязательная подстановка, не готовый ID. Учётной записи нужны права на создание ресурсов и чтение AMI/SSM/подсети. Apply создаёт платные ресурсы. Сохраните значения переменных в локальном tfvars для последующего destroy.

Проверьте страницу командой `curl --fail http://PUBLIC_IP/`, заменив PUBLIC_IP полученным адресом. Ожидаемая строка: `I made it! This is awesome!`. Terraform validate не проверяет наличие маршрута, IAM-права и HTTP-готовность.

После работы выполните `terraform destroy -var='region=us-east-1' -var='subnet_id=subnet-REPLACE'` с теми же реальными значениями и проверьте удаление учебных ресурсов. Подсеть в модуле — источник данных, она не удаляется.

[User data AWS](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/user-data.html) · [Сроки поддержки AL2023](https://docs.aws.amazon.com/linux/al2023/ug/release-cadence.html).
