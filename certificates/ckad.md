<a id="certified-kubernetes-application-developer-ckad"></a>
## Сертифицированный разработчик приложений Kubernetes (CKAD)

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
