<a id="perl"></a>
## Perl

<a id="perl-self-assessment"></a>
### Самопроверка по Perl

<details>
<summary>Что такое Perl?</summary><br><b>

Из официальной [документации](https://perldoc.perl.org/):

«Официально Perl означает Practical Extraction and Report Language — практический язык извлечения данных и составления отчётов. За исключением случаев, когда это не так».

Это язык программирования общего назначения, изначально ориентированный на обработку текста. Его используют для системного администрирования, сетевых задач, создания сайтов и многого другого.
</b></details>

<details>
<summary>Какие типы данных есть в Perl и как их определять?</summary><br><b>

* Скаляр — переменная, хранящая одно значение: строку, число или ссылку.

```
my $number = 5;
```

* Массив — список скаляров.

```
my @numbers = (1, 2, 3, 4, 5);
# or using the `qw` keyword (quote word):
my @numbers = qw/1 2 3 4 5/; 
# '/' can be another symbol, e.g qw@1 2 3 4 5@
```

* Хеш, или ассоциативный массив, — неупорядоченный набор пар «ключ — значение». Доступ к значениям осуществляется по ключам.

```
my %numbers = (
  First => '1',
  Second => '2',
  Third => '3'
);
```
</b></details>

<details>
<summary>Как прочитать значение хеша, добавить и удалить пару «ключ — значение», изменить хеш?</summary><br><b>

```
my %numbers = (
  'First' => '1',
  'Second' => '2',
  'Third' => '3'
);
```

* Чтение:

```
print($numbers{'First'});
```

* Добавление:

```
$numbers{'Fourth'} = 4;
```

* Удаление:

```
delete $numbers{'Third'};
```

* Изменение:

```
$numbers{'Fifth'} = 6;
$numbers{'Fifth'} = 5;
```
</b></details>

<details>
<summary>Как перебрать элементы массива и хеша?</summary><br><b>

* Массив:

```
my @numbers = qw/1 2 3 4 5/;

# Using `$_` that represents the current iteration in a loop. It starts from index array 0 until the last index.
foreach (@numbers) {
    print($_);
}
# Output: 12345


# "$#" returns the max index of an array. That's the reason because we can iterate accessing to the array from the index 0 to the max index.
for my $i (0..$#numbers) {
    print($numbers[$i]);
}
# Output: 12345


# Using the `map` keyword:
print map {$_} @numbers;
# Output: 12345

# Using `while`. We should take care with this option. When we use `shift` we're deleting the first element of the array and assigning it to the `element` variable. 
# After this `loop` the `numbers` array will not have elements.
while (my $element = shift(@numbers)) {
    print($element);
}
# Output: 12345
```

* Хеш:

```
 my %capital_cities = (
  'Madrid' => 'Spain',
  'Rome' => 'Italy',
  'Berlin' => 'Germany'
);

# Iterate and get the `keys`:
foreach my $city (keys %capital_cities) {
    print($city . "\n");
}
# Iterate and get the `values`:
foreach my $country (values %capital_cities) {
    print($country . "\n");
}

# Iterate and get the values and keys (first option):
foreach my $city (keys %capital_cities) {
    print("City: $city - Country: $capital_cities{$city}" . "\n");
}

# Iterate and get the values and keys (first option):
while(my ($city, $country) = each %capital_cities) {
    print("City: $city - Country: $capital_cities{$city}" . "\n");
}
```
</b></details>

<details>
<summary>Что такое подпрограмма Perl и как её определить?</summary><br><b>

Это пользовательская функция Perl, аналогичная функциям других языков. Подпрограмма определяется ключевым словом `sub`.

```
sub hello {
  print "hello";
}
```
</b></details>

<details>
<summary>Какими способами подпрограмма может получать параметры?</summary><br><b>

* Присваивание списком: массив `@_` содержит переданные параметры.

```
sub power {
    my ($b, $e) = @_;
    return $b ** $e; 
}

&power(2, 3);
```

* Поэлементное присваивание: обращение к отдельным элементам `@_`. Индексация начинается с нуля.

```
sub power {
    my $b = $_[0];
    my $e = $_[1];
    return $b ** $e; 
}

&power(2, 3);
```

* Использование `shift`: функция удаляет первый элемент массива и возвращает его значение.

```
sub power {
    my $b = shift;
    my $3 = shift;
    return $b ** $e; 
}

&power(2, 3);
```

[Источник](https://stackoverflow.com/a/21465275/12771230)

В этом ответе на Stack Overflow также обсуждается предпочтительный подход.
</b></details>

<details>
<summary>Что такое лексическая и динамическая области видимости?</summary><br><b>

В Perl `my` создаёт лексическую переменную с областью по структуре кода; `local` временно меняет значение package variable на время динамической цепочки вызовов и восстанавливает его при выходе. `our` даёт лексический доступ к package variable, но не делает её отдельной lexical-копией. [Perl scope](https://perldoc.perl.org/perlsub#Private-Variables-via-my()).
</b></details>

<details>
<summary>Как создавать и разыменовывать ссылки?</summary><br><b>

Ссылки на массив/хеш: `my $a = [1, 2]; my $h = { name => 'x' };`. Доступ: `$a->[0]`, `$h->{name}`; разыменование коллекций: `@$a`, `%$h`. Учитывайте strict/warnings и различайте ссылку и сам список. [perlref](https://perldoc.perl.org/perlref).
</b></details>

<details>
<summary>Есть ли в Perl соглашения о стиле кода?</summary><br><b>

См. [perlstyle](https://perldoc.perl.org/perlstyle).
</b></details>

<details>
<summary>Что такое Perl POD? Напишите пример.</summary><br><b>

Из официальной [документации](https://perldoc.perl.org/perlpod):

POD — простой язык разметки для написания документации Perl, программ и модулей на Perl.

```
=item
    This function returns the factorial of a number.
    Input: $n (number you wanna calculate).
    Output: number factorial.
=cut
sub factorial {
    my ($i, $result, $n) = (1, 1, shift);
    $result = $result *= $i && $i++ while $i <= $n;
    return $result;
}
```
</b></details>

<a id="perl-regex"></a>
### Регулярные выражения Perl

<details>
<summary>Проверьте, есть ли в строке слово electroencefalografista.</summary><br><b>

```
my $string = "The longest accepted word by RAE is: electroencefalografista";
if ($string =~ /electroencefalografista/) {                                                         
    print "Match!";
}
```
</b></details>

<details>
<summary>Проверьте, что в строке нет слова electroencefalografista.</summary><br><b>

```
my $string = "The longest not accepted word by RAE is: Ciclopentanoperhidrofenantreno";
if ($string !~ /electroencefalografista/) {
    print "Does not match!";
}
```
</b></details>

<details>
<summary>Замените слово amazing.</summary><br><b>

```
my $string = "Perl is amazing!";
$string =~ s/amazing/incredible/;
print $string;
# Perl is incredible!
```
</b></details>

<details>
<summary>Извлеките hh:mm:ss из следующей строки даты и времени с помощью захватывающей группы ().</summary><br><b>

```
my $date = "Fri Nov 19 20:09:37 CET 2021";
my @matches = $date =~ /(.*)(\d{2}:\d{2}:\d{2})(.*)/;
print $matches[1];
# Output: 20:09:37
```
</b></details>

<details>
<summary>Извлеките из массива все числовые элементы.</summary><br><b>

```
my @array = ('a', 1, 'b', 2, 'c', 3);
my @numbers = grep (/\d/, @array);    # Note: \d involves more digits than 0-9
map {print $_ . "\n" } @numbers;
```
</b></details>

<details>
<summary>Выведите всех пользователей Linux, чьи имена начинаются с d или D.</summary><br><b>

* Однострочная команда Perl :D

```
open(my $fh, '<', '/etc/passwd');
my @user_info = <$fh>;
map { print $& . "\n" if $_ =~ /^d([^:]*)/  } @user_info;
close $fh;
```

* Вариант без однострочной команды:

```
foreach my $user_line (@user_info) {
    if ($user_line =~ /^d([^:]*)/) {
        print $& . "\n";
    }
}
```
</b></details>

<a id="perl-files-handle"></a>
### Работа с файлами в Perl

<details>
<summary>Перечислите режимы открытия файлов.</summary><br><b>

* Только чтение: `<`.
* Запись с очисткой; если файла нет, он создаётся: `>`.
* Добавление в конец; если файла нет, он создаётся: `>>`.
* Чтение и запись: `+<`.
* Чтение и запись с очисткой; если файла нет, он создаётся: `+>`.
* Чтение и добавление в конец; если файла нет, он создаётся: `+>>`.
</b></details>

<details>
<summary>Как записать данные в файл?</summary><br><b>

```
# We can use:
# '>' Write (it clears a previous content if exists).
# '>>' Append.
open(my $fh, '>>', 'file_name.ext') or die "Error: file can't be opened";
print $fh "writing text...\n";
close($fh);
```
</b></details>

<details>
<summary>Как прочитать файл и вывести каждую строку?</summary><br><b>

```
open(my $fh, '<', 'file_to_read.ext') or die "Error: file can't be opened";
my @file = <$fh>;
foreach my $line (@file) {
    print $line;
}
```

Можно читать через файловый дескриптор, не присваивая строки массиву:

```
open(my $fh, '<', 'file_to_read.ext') or die "Error: file can't be opened";

foreach my $line (<$fh>) {
    print $line;
}
```
</b></details>

<a id="perl-oop"></a>
### ООП в Perl

<details>
<summary>Поддерживает ли Perl объектно-ориентированное программирование?</summary><br><b>

Из официальной [документации](https://perldoc.perl.org/perlootut):

Встроенная объектная система Perl минималистична и оставляет большую часть работы программисту.
</b></details>

<details>
<summary>Для чего нужна функция bless?</summary><br><b>

`bless` связывает структуру данных с классом, превращая её в объект.
</b></details>

<details>
<summary>Как создать класс Perl и вызвать его метод?</summary><br><b>

* Создадим пакет `Example.pm`:

```
package Example;

sub new {
    my $class = shift;
    my $self = {};
    bless $self, $class;
    return $self;
}

sub is_working {
    print "Working!";
}

1;
```

* Теперь создадим экземпляр класса `Example` и вызовем метод `is_working`:

```
my $e = new Example();
$e->is_working();
# Output: Working!
```
</b></details>

<details>
<summary>Поддерживает ли Perl наследование? Что означает SUPER?</summary><br><b>

Да. См. официальную [документацию](https://perldoc.perl.org/perlobj#Inheritance).
Там же описано `SUPER`, используемое для вызова метода родительского класса, и приведён пример наследования.
</b></details>

<details>
<summary>Поддерживает ли Perl полиморфизм? Что такое переопределение метода?</summary><br><b>

Да. Один из способов реализовать полиморфизм в Perl — переопределение методов.

Оно происходит, когда класс определяет собственную реализацию метода, уже существующего в родительском классе.

Пример:

```
package A;

sub new { return bless {}, shift; };
sub printMethod { print "A\n"; };

package B;

use parent -norequire, 'A';

sub new { return bless {}, shift; };
sub printMethod { print "B\n"; };

my $a = A->new();
my $b = B->new();

A->new()->printMethod();
B->new()->printMethod();

# Output:
# A
# B
```
</b></details>

<details>
<summary>Как вызвать метод родительского класса?</summary><br><b>

```
# Class `A` with `printA` method.
package A;

sub new { return bless {}, shift; };
sub printA { print "A"; };

# Class `B` that extends or use the parent class `A`.
package B;

use parent -norequire, 'A';

sub new { return bless {}, shift; };

# Instance class `B` allows call the inherited method
my $b = B->new();
$b->printA();
```
</b></details>

<a id="perl-exception-handling"></a>
### Обработка исключений в Perl

<details>
<summary>Как выполнить код и перехватить исключение в Perl?</summary><br><b>

Из официальной [документации eval](https://perldoc.perl.org/functions/eval):

`eval` выполняет небольшой фрагмент Perl и перехватывает ошибки, чтобы они не завершили вызывающую программу.

Например:

```
eval {
    die;
};
if ($@) {
    print "Error. Details: $@";
}
```

Результат:

```
Error. Details: Died at eval.pl line 2.
```

`eval`, похожий по назначению на `try` в других языках, пытается выполнить код. Код вызывает `die`, после чего выполнение продолжается проверкой `if`: она выясняет, содержит ли переменная ошибки `$@` какое-либо значение. Это напоминает `catch` в других языках и позволяет обрабатывать ошибки.
</b></details>

<a id="perl-os"></a>
### Perl и операционная система

<details>
<summary>Что такое Perl Open3?</summary><br><b>

Из официальной [документации IPC::Open3](https://perldoc.perl.org/IPC::Open3):

IPC::Open3 запускает процесс с возможностью чтения, записи и обработки ошибок через open3().

`open3` позволяет управлять STDIN, STDOUT и STDERR процесса. Обычно его используют для выполнения команд.
</b></details>

<details>
<summary>С помощью Open3 создайте файл размером 15 МБ и проверьте успешность создания.</summary><br><b>

* Код:

```
use IPC::Open3;
use Data::Dumper;

sub execute_command {
    my @command_to_execute = @_;
    my ($stdin, $stdout, $stderr);
    eval {
        open3($stdin, $stdout, $stderr, @command_to_execute);
    };
    if ($@) {
        print "Error. Details: $@";
    }
    close($stdin);
    return $stdout;
}

my $file_name = 'perl_open3_test';
&execute_command('truncate', '-s', '15M', $file_name);
my $result = &execute_command('stat', '-c', '%s', $file_name);
print Dumper(<$result>);
```

* Результат:

```
$ -> perl command.pl 
$VAR1 = '15728640
';
```
</b></details>

<a id="perl-packages--modules"></a>
### Пакеты и модули Perl

<details>
<summary>Что такое пакет Perl? А модуль?</summary><br><b>

Пакет задаёт пространство имён. Для объявления пакета, в том числе используемого как класс, служит ключевое слово `package`. Модуль загружается с помощью `use`.

Примечание: исходник упрощённо приравнивает модуль к классу. Модуль может предоставлять функции и другие средства, не являясь классом.
</b></details>

<details>
<summary>Чем отличаются расширения .pl и .pm?</summary><br><b>

Файлы обоих типов содержат код Perl. Расширение `.pm` принято использовать для модулей, а `.pl` — для сценариев. При загрузке модуля стандартными средствами расширение `.pm` имеет практическое значение; наличие классов само по себе не определяет расширение.
</b></details>

<details>
<summary>Почему модуль Perl должен возвращать значение в конце файла? Изучите пример.</summary><br><b>

Для успешной загрузки модуль должен вернуть истинное значение. Если результат ложный, стандартная загрузка завершится ошибкой. Поэтому файл часто заканчивается строкой `1;`.

```
package A;

sub new { return bless {}, shift; };
sub printMethod { print "A\n"; };

1;
```
</b></details>

<details>
<summary>Что такое CPAN и cpanm?</summary><br><b>

CPAN — Comprehensive Perl Archive Network, сеть архивов модулей Perl.

Из официального описания [App::cpanminus](https://metacpan.org/pod/App::cpanminus): cpanm получает, распаковывает, собирает и устанавливает модули из CPAN.

[Поиск модулей CPAN](https://metacpan.org/)
</b></details>

<details>
<summary>Как установить cpanm и модуль Perl?</summary><br><b>

Есть несколько способов установки модулей. Здесь используется `cpanm`.

* Установка `cpanm`:

```
$ cpan App::cpanminus
```

* Установка модуля `Test`:

```
cpanm Test
```

Проверим установленный модуль `Test`:

```
$ perl -M'Test::Simple tests => 1' -e 'ok( 1 + 1 == 2 );'
1..1
ok 1
```

```
$ perl -M'Test::Simple tests => 1' -e 'ok( 1 + 1 == 3 );'
1..1
not ok 1
#   Failed test at -e line 1.
# Looks like you failed 1 test of 1.
```
</b></details>
