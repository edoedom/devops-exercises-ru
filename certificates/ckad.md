<a id="certified-kubernetes-application-developer-ckad"></a>
## Сертифицированный разработчик приложений Kubernetes (CKAD)

## Действующие направления подготовки

Сверено 5 ноября 2026 года с [программой CNCF CKAD](https://github.com/cncf/curriculum/tree/master/ckad). Этот конспект не покрывает её полностью.

| Раздел | Вес |
|---|---:|
| Проектирование и сборка приложения | 20% |
| Развёртывание приложения | 20% |
| Наблюдаемость и сопровождение | 15% |
| Окружение, конфигурация и безопасность | 25% |
| Сервисы и сети | 20% |

Кроме приведённых команд отработайте сборку образа и multi-container Pod; rolling update/rollback и стратегии доставки; probes, логи и метрики; ConfigMap/Secret, ServiceAccount, securityContext, ресурсы и квоты; Service/Ingress/NetworkPolicy. Убедитесь, что используемый кластер поддерживает нужные API и сетевые политики. Версию Kubernetes и условия экзамена уточняйте у организатора перед сдачей.

<a id="core-concepts"></a>
### Основные понятия

<a id="pods"></a>
### Поды

<details>
<summary>Разверните под web-1985 из образа nginx:alpine.</summary><br><b>

`kubectl run web-1985 --image=nginx:alpine --restart=Never`
</b></details>

<details>
<summary>Как узнать, на каком узле работает под?</summary><br><b>

`kubectl get po -o wide`
</b></details>

<a id="namespaces"></a>
### Пространства имён

<details>
<summary>Выведите список всех пространств имён.</summary><br><b>

kubectl get ns
</b></details>

<details>
<summary>Выведите все поды пространства имён neverland.</summary><br><b>

kubectl get po -n neverland
</b></details>

<details>
<summary>Выведите поды во всех пространствах имён.</summary><br><b>

kubectl get po --all-namespaces
</b></details>
