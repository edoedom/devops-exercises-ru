<a id="update-and-upgrade-apt-packages-task---solution"></a>
## Обновление кеша APT и пакетов: решение

```
- name: "update and upgrade apt packages."
  become: yes
  apt:
    upgrade: yes
    update_cache: yes
```
