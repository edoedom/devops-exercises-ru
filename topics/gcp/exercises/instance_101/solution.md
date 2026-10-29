<a id="create-an-instance"></a>
# Создание экземпляра

<a id="objectives"></a>
## Задание

1. Создайте виртуальную машину со следующими параметрами:
   1. Имя: instance-1.
   2. Тип: e2-micro.
   3. Метки:
      1. app: web.
      2. env: dev.
2. С помощью CLI gcloud:
   1. Измените значение метки app на db.
   2. Удалите метку env.

<a id="solution"></a>
## Решение

<a id="console"></a>
### Консоль

1. Откройте **Compute Engine → VM instances**.
2. Нажмите **Create Instance**:
   1. Укажите имя instance-1.
   2. Через **Add label** добавьте метки app: web и env: dev.
   3. Выберите тип машины e2-micro.
3. Нажмите **Create**.
4. Выберите экземпляр и нажмите **Show info panel**:
   1. На вкладке **Labels** измените значение app на db.
   2. Удалите метку env.

<a id="shell"></a>
### Командная оболочка

```
gcloud config set project <PROJECT_ID>
gcloud config set compute/region <REGION NAME>
gcloud config set compute/zone <ZONE NAME>

gcloud compute instances create instance-1 --labels app=web,env=dev --machine-type=e2-micro
gcloud compute instances update instance-1 --update-labels app=db
gcloud compute instances update instance-1 --remove-labels env
```

<a id="terraform"></a>
### Terraform

[Посмотреть main.tf](main.tf).
