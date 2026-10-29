<a id="aws---launch-ec2-web-instance"></a>
## AWS: запуск экземпляра EC2 с веб-сервером

<a id="objectives"></a>
### Задание

Запустите один экземпляр EC2 со следующими параметрами:

1. Образ Amazon Linux 2.
2. Тип экземпляра с 1 vCPU и 1 ГиБ памяти.
3. Хранилище экземпляра должно удаляться при завершении его существования (terminate).
4. При запуске экземпляра:
   1. Установите пакет httpd.
   2. Запустите службу httpd.
   3. Запишите в /var/www/html/index.html строку `I made it! This is is awesome!`.
5. Назначьте тег Type: web и имя web-1.
6. Разрешите HTTP-трафик на порт 80 от любых источников.

<a id="solution"></a>
### Решение

1. Выберите ближайший подходящий регион.
2. Откройте EC2.
3. Выберите **Instances → Launch instances**.
4. Образ: Amazon Linux 2.
5. Тип экземпляра: t2.micro.
6. В настройках хранилища включите **Delete on Termination**.
7. В поле **User data** вставьте:

```
yum update -y
yum install -y httpd
systemctl start httpd
systemctl enable httpd
echo "<h1>I made it! This is is awesome!</h1>" > /var/www/html/index.html
```

8. Добавьте теги:
   * Ключ Type, значение web.
   * Ключ Name, значение web-1.
9. В группе безопасности разрешите входящий HTTP-трафик по TCP на порт 80 от любого источника.
10. Нажмите **Review**, проверьте параметры и нажмите **Launch**.
11. Если пары ключей нет, создайте и скачайте её.

**Решение с Terraform:**

```
 
provider "aws" {
  region = "us-east-1" // Or your desired region
}

resource "aws_instance" "web_server" {
  ami           = "ami-12345678" // Replace with the correct AMI for Amazon Linux 2
  instance_type = "t2.micro" // Or any instance type with 1 vCPU and 1 GiB memory

  tags = {
    Name = "web-1"
    Type = "web"
  }

  root_block_device {
    volume_size           = 8 // Or any desired size
    delete_on_termination = true
  }

  provisioner "remote-exec" {
    inline = [
      "sudo yum update -y",
      "sudo yum install -y httpd",
      "sudo systemctl start httpd",
      "sudo bash -c 'echo \"I made it! This is awesome!\" > /var/www/html/index.html'",
      "sudo systemctl enable httpd"
    ]

    connection {
      type        = "ssh"
      user        = "ec2-user"
      private_key = file("~/.ssh/your_private_key.pem") // Replace with the path to your private key
      host        = self.public_ip
    }
  }

  security_group_ids = [aws_security_group.web_sg.id]
}

resource "aws_security_group" "web_sg" {
  name        = "web_sg"
  description = "Security group for web server"
  
  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
}
```
