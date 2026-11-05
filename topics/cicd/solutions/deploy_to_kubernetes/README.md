# Развёртывание веб-приложения через Ansible

Этот пример ожидает образ HTTP-приложения, слушающего порт 80, доступный Kubernetes API, права на namespace/Deployment/Service/Secret/Ingress и уже установленный поддерживаемый Ingress controller. Укажите его `IngressClass`; не устанавливайте снятый с сопровождения общественный ingress-nginx ради этого упражнения. Для нового проекта рассмотрите Gateway API, если выбранный контроллер его поддерживает.

На управляющем узле установите `ansible-core`, Python-пакет `kubernetes` и коллекцию `ansible-galaxy collection install kubernetes.core`. Настройте kubeconfig (`K8S_AUTH_KUBECONFIG`, если путь отличается от стандартного). Подготовьте сертификат и ключ для имени хоста; сертификат должен быть доверенным клиенту. Пример использует `hello-world.app`; замените его через `app_host` и настройте DNS.

Из этого каталога:

```bash
ansible-playbook deploy.yml \
  -e app_image=YOUR_REGISTRY/helloworld:BUILD_TAG \
  -e ingress_class=YOUR_INGRESS_CLASS \
  -e tls_cert_file=/absolute/path/fullchain.pem \
  -e tls_key_file=/absolute/path/privkey.pem
```

Пример создаёт TLS Secret с именем `tls-secret` и использует то же имя в Ingress. Приватный ключ не сохраняйте в репозитории. Вместо файлов в CI можно использовать соответствующее хранилище credentials. Для приватного registry настройте `imagePullSecrets` отдельно.

В Jenkinsfile замените URL репозитория и IMAGE_REPO, подготовьте credentials `dockerhub`, Docker/Ansible на агенте и передавайте пути TLS-файлов и ingress class. Файлы playbook и manifest должны входить в checkout приложения. Номер сборки передаётся в deployment как тег; для строгой неизменяемости используйте digest. Проверяйте rollout и доступность приложения после развёртывания.

Этот пример проверен статически, без подключения к кластеру. Источник: [kubernetes.core.k8s](https://docs.ansible.com/projects/ansible/latest/collections/kubernetes/core/k8s_module.html).
