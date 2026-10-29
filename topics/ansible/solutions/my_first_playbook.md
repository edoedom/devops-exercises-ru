<a id="my-first-playbook---solution"></a>
## Первый плейбук: решение

1. `vi first_playbook.yml`

```
- name: Install zlib and create a file
  hosts: some_remote_host
  tasks:
    - name: Install zlib
      package:
        name: zlib
        state: present
      become: yes
    - name: Create the file /tmp/some_file
      file:
        path: '/tmp/some_file'
        state: touch
```

2. Отредактируйте файл инвентаризации: `vi /etc/ansible/hosts`.

```
[some_remote_host]
some.remoted.host.com
```

Запустите плейбук:

`ansible-playbook first_playbook.yml`
