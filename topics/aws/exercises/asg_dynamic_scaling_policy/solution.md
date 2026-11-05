<a id="aws-auto-scaling-groups---dynamic-scaling-policy"></a>
## AWS Auto Scaling: динамическое масштабирование — решение

Используйте отдельную учебную ASG из [задания](exercise.md), min=1, desired=1, max=3. Создайте Target tracking policy с `ASGAverageCPUUtilization`, целевым значением 70 и включённым scale-in. Задайте default instance warmup по времени готовности приложения; detailed monitoring даёт более частые данные, но может тарифицироваться.

Для краткой нагрузки на одном учебном Linux-экземпляре можно обойтись без EPEL и stress. Следующий Bash-скрипт запускает по процессу на доступный CPU, останавливает их через 120 секунд и выполняет очистку при сигнале:

```bash
#!/bin/bash
set -euo pipefail
pids=()
cleanup() {
  for pid in "${pids[@]}"; do
    kill "$pid" 2>/dev/null || true
  done
  wait || true
}
trap cleanup EXIT
trap 'exit 130' INT
trap 'exit 143' TERM
for ((i=0; i<$(nproc); i++)); do
  yes > /dev/null &
  pids+=("$!")
done
sleep 120
```

Две минуты не гарантируют срабатывания политики: сопоставьте период метрики, alarm evaluation, warmup и Activity history. Если требуется более долгий опыт, ограниченно увеличьте длительность в выделенной группе и наблюдайте расходы. У burstable-типов учитывайте CPU credits.

Метрика усредняется по группе. Нагрузка на одну из нескольких машин может не поднять среднее выше цели; для проверки распределяйте запросы между экземплярами. При достаточной устойчивой нагрузке ASG увеличивает desired в пределах max; число добавленных машин заранее не фиксировано.

После прекращения нагрузки scale-in может произойти с задержкой. На него влияют warmup, нижний предел, защита от scale-in, другие политики и отсутствие данных. Значение ниже 70% само по себе не обещает немедленного удаления одного экземпляра. Сохраните графики и события, затем удалите учебные ресурсы.

[Target tracking](https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-scaling-target-tracking.html) · [Instance warmup](https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-default-instance-warmup.html).
