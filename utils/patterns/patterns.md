# Шаблоны проектирования (Patterns)

> Взято из этого [репозитория](https://github.com/Volodichev/patterns?tab=readme-ov-file)

**Шаблоны проектирования** — это часто встречающееся решение определённой проблемы при проектировании архитектуры программ. Паттерны часто путают с алгоритмами, ведь оба понятия описывают типовые решения каких-то известных проблем. Если привести аналогии, то алгоритм — это кулинарный рецепт с чёткими шагами, а паттерн — инженерный чертёж, на котором нарисовано решение, но не конкретные шаги его реализации.

## Порождающие паттерны (Creational Patterns):

> беспокоятся о гибком создании объектов без внесения в программу лишних зависимостей

-   [Абстрактная фабрика (Abstract Factory)](https://github.com/Volodichev/patterns/tree/main/abstract_factory#readme) Семейства связанных объектов.
-   [Строитель (Builder)](https://github.com/Volodichev/patterns/tree/main/builder#readme) Cложные объекты пошагово. один код для разных объектов.
-   [Фабричный метод (Factory Method)](https://github.com/Volodichev/patterns/tree/main/factory_method#readme) Общий интерфейс для подклассов объектов изменяемых типов.
-   [Прототип (Prototype)](https://github.com/Volodichev/patterns/tree/main/prototype#readme) Копируем объекты, не вдаваясь в подробности реализации.
-   [Одиночка (Singleton)](https://github.com/Volodichev/patterns/tree/main/singleton#readme) Класс имеет только один экземпляр, и глобальную точку доступа.

## Структурные паттерны (Structural Patterns):

> показывают различные способы построения связей между объектами

-   [Адаптер (Adapter)](https://github.com/Volodichev/patterns/tree/main/adapter#readme) Несовместимые интерфейсы
-   [Компоновщик (Composite)](https://github.com/Volodichev/patterns/tree/main/composite#readme) Древовидная структура
-   [Декоратор/оформитель (Decorator/Wrapper)](https://github.com/Volodichev/patterns/tree/main/decorator#readme) Функциональность через «обёртки».
-   [Фасад (Facade)](https://github.com/Volodichev/patterns/tree/main/facade#readme) Простой интерфейс к сложной структуре
-   [Заместитель/прокси/суррогат (Proxy/surrogate)](https://github.com/Volodichev/patterns/tree/main/proxy#readme) Подставляет объекты-заменители.

## Поведенческие паттерны (Behavioral Patterns):

> заботятся об эффективной коммуникации между объектами

-   [Команда/действие (Command/action)](https://github.com/Volodichev/patterns/tree/main/command#readme) Передает запросы в объекты как аргументы.
-   [Итератор/указатель (Iterator)](https://github.com/Volodichev/patterns/tree/main/iterator#readme) Последовательный обход элементов составных объектов.
-   [Наблюдатель/слушатель (Observer/Listener)](https://github.com/Volodichev/patterns/tree/main/observer#readme) Один объект следит за другим.
-   [Стратегия (Strategy)](https://github.com/Volodichev/patterns/tree/main/strategy#readme) Схожие алгоритмы в класс.
-   [Состояние (State)](https://github.com/Volodichev/patterns/tree/main/state#readme) Меняет поведение в зависимости от состояния.
