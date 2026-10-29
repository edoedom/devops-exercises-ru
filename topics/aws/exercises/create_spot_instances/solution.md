<a id="aws-ec2---spot-instances"></a>
## AWS EC2: спотовые экземпляры

<a id="objectives"></a>
### Задание

A. Создайте запрос Spot Request для двух спотовых экземпляров:

* Образ Amazon Linux 2 AMI.
* Целевое количество: два экземпляра в каждый момент времени; у каждого — 2 vCPU и 3 ГиБ RAM.

B. Создайте один спотовый экземпляр с Amazon Linux 2 и типом t2.micro.

<a id="solution"></a>
### Решение

A. Создание Spot Fleet:

1. Откройте EC2.
2. Выберите **Spot Requests**.
3. Нажмите **Request Spot Instances**.
4. Задайте параметры:
   * Образ Amazon Linux 2 AMI.
   * **Total target capacity**: 2.
   * Включите **Maintain target capacity**.
   * vCPU: 2.
   * Память: 3 ГиБ.
5. Нажмите **Launch**.

B. Создание одного спотового экземпляра:

1. Откройте EC2.
2. Выберите **Instances**.
3. Нажмите **Launch Instances**.
4. Выберите Amazon Linux 2 AMI и нажмите **Next**.
5. Выберите t2.micro и нажмите **Next: Configure Instance Details**.
6. Включите **Request Spot instances**.
7. Задайте максимальную цену выше текущей.
8. Нажмите **Review and Launch**.
