<a id="certified-kubernetes-administrator-cka"></a>
## Сертифицированный администратор Kubernetes (CKA)

## Программа и недостающая практика

Сверено 5 ноября 2026 года с [программой CNCF](https://github.com/cncf/curriculum/tree/master/cka) и [описанием CKA](https://trainingportal.linuxfoundation.org/courses/certified-kubernetes-administrator-cka). Ниже — учебные задачи, а не полный банк экзамена. Версию Kubernetes и правила разрешённых ресурсов проверяйте на странице организатора перед сдачей.

| Раздел | Вес |
|---|---:|
| Архитектура, установка и конфигурация кластера | 25% |
| Рабочие нагрузки и планирование | 15% |
| Сервисы и сети | 20% |
| Хранилища | 10% |
| Поиск неисправностей | 30% |

Дополните задачи по Pod/Deployment следующими практическими сценариями:

- kubeadm: установка, обновление и восстановление кластера; RBAC и отказоустойчивый control plane.
- Helm/Kustomize, CRD и operator: установка компонентов, чтение сгенерированных ресурсов и диагностика; различия CRI/CNI/CSI.
- Gateway API: установленный controller, GatewayClass, Gateway и HTTPRoute; анализ Accepted/ResolvedRefs и доступности backend. Обычный Ingress тоже входит в подготовку.
- NetworkPolicy и CoreDNS: разрешённые/запрещённые соединения, DNS, Service, EndpointSlice, readiness и маршрутизация. NetworkPolicy требует поддерживающий её CNI.
- StorageClass/PVC: dynamic provisioning, access modes, reclaim policy, привязка тома и причины Pending; освобождение PVC не всегда удаляет данные.
- Диагностика: NotReady, Pending, CrashLoopBackOff, ImagePullBackOff, логи компонентов, ресурсы узла и недоступный Service. Объясняйте причину и проверяйте восстановление после исправления.


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
