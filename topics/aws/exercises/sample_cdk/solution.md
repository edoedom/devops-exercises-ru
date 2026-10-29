<a id="set-up-a-cdk-project---solution"></a>
### Создание проекта CDK — решение

<a id="exercise"></a>
### Задание

Инициализируйте проект CDK и подготовьте файлы, необходимые для его сборки.

<a id="solution"></a>
### Решение

<a id="initialize-a-cdk-project"></a>
#### Инициализация проекта CDK

1. Установите CDK командой `npm install -g aws-cdk`.
2. Создайте для проекта каталог `sample` и выполните в нём `cdk init app --language typescript`. Можно выбрать язык csharp, fsharp, go, java, javascript, python или typescript.
3. В каталоге появятся следующие файлы:
   1. `cdk.json`, `tsconfig.json`, `package.json` — файлы конфигурации с общими настройками проекта CDK.
   2. `bin/sample.ts` — точка входа в проект. Здесь определяется создаваемый стек.
   3. `lib/sample-stack.ts` — основной файл с кодом проекта CDK.

<a id="create-a-sample-lambda-function"></a>
#### Создание простой функции Lambda

1. Добавьте в `lib/sample-stack.ts` следующий код:

```typescript
import * as cdk from 'aws-cdk-lib';
import * as lambda from 'aws-cdk-lib/aws-lambda';
import { Construct } from 'constructs';

export class SampleStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    const hello = new lambda.Function(this, 'SampleLambda', {
      runtime: lambda.Runtime.NODEJS_14_X,
      code: lambda.Code.fromInline('exports.handler = async () => "hello world";'),
      handler: 'index.handler'
    });
  }
}

```

Будет создана функция Lambda, которая при вызове возвращает "hello world".

<a id="bootstrap-the-cdk-project"></a>
#### Подготовка среды CDK

Перед развёртыванием проекта необходимо выполнить начальную подготовку среды — bootstrap. Она создаёт стек CloudFormation с ресурсами, используемыми при развёртывании проекта. Выполните `cdk bootstrap`.

Подробнее о начальной подготовке — [здесь](https://docs.aws.amazon.com/cdk/latest/guide/bootstrapping.html).

<a id="deploy-the-project"></a>
##### Развёртывание проекта

1. После изменения зависимостей проекта выполните `npm install`, чтобы установить их.
2. Выполните `cdk synth`, чтобы сформировать шаблон CloudFormation. В оригинале указан файл `cdk.out/CDKToolkit.template.json`; имя шаблона приложения зависит от стека, а CDKToolkit относится к ресурсам начальной подготовки среды.
3. Выполните `cdk diff`, чтобы увидеть планируемые изменения в учётной записи AWS. Должен появиться стек `SampleStack`, создающий функцию Lambda и связанные ресурсы.
4. Выполните `cdk deploy`. В разделе CloudFormation учётной записи AWS должен появиться новый стек.
5. Откройте консоль Lambda и найдите созданную функцию `SampleLambda`.
