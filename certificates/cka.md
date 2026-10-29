<a id="certified-kubernetes-administrator-cka"></a>
## Сертифицированный администратор Kubernetes (CKA)

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
