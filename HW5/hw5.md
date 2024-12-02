# Уроки 4-5 - полиморфизм, наследование, декораторы и итераторы
## Контрольные вопросы:
- В чем основная идея __полиморфизма__? Как он реализуется в Python.

Идея __полиморфизма__ заключается в использовании единственной сущности(метода, оператора или объекта) для представления различных типов в различных сценариях использования.
Пример: оператор сложения (+) работает по разному для строк и целочисленного типа данных.

- Зачем переопределять метод `radd()` наравне с 
`add()`?

Метод `add()` — это метод, используемый для определения поведения оператора сложения (+), когда он применяется к объектам класса. Когда складываются два объекта класса, у которого есть метод `add()`, Python неявно вызывает этот метод.
<br>Чтобы реализовать метод `add()`, необходимо определить его в своем классе, принимая один параметр помимо self: другой объект, который будет добавлен. Метод должен возвращать новый объект, который представляет сумму двух объектов.

Метод `radd()` дополняет `add()`, определяя поведение оператора сложения, когда левый операнд не имеет метода `add()`, или когда его метод `add()` не знает, как обработать правый операнд.
<br>Как правило, `radd()` реализуется так же, как `add()`. Это гарантирует, что операции сложения, включающие экземпляры класса, симметричны, то есть a + b даст тот же результат, что и b + a, когда один из них является экземпляром вашего класса.

- Как можно описать взаимоотношения 
__родительского__ и __дочернего__ классов?

Взаимоотношения между родительским и дочерним классами описываются через наследование. Дочерний класс наследует свойства и методы родительского класса, что позволяет ему расширять или изменять функциональность.

- Для чего используется ключевое 
слово `super()`?

Ключевое слово super() используется для вызова методов родительского класса из дочернего. Это позволяет избежать явного указания имени родительского класса и упрощает поддержку кода, особенно при множественном наследовании.

- Какую роль играет порядок классов __предков__
при __множественном наследовании__?

При множественном наследовании порядок классов предков определяет порядок разрешения методов (Method Resolution Order, MRO). Python использует алгоритм C3 линеаризации для определения порядка, что помогает избежать проблем с "алмазным" наследованием.

- Зачем нужна __обработка исключений__? В каких 
случаях ее использование некорректно?

Обработка исключений нужна для управления ошибками и исключительными ситуациями в программе. Она позволяет избежать аварийного завершения программы. Некорректно использовать обработку исключений для управления потоком выполнения, когда можно использовать обычные конструкции управления.

- Зачем в блоке `try` использовать раздел
`finally`?

Блоки try и finally в Python используются вместе для обработки исключений и выполнения определённых действий, независимо от того, произошло ли исключение или нет. 

Пример:
<br> 1. `try`: В этом блоке мы пытаемся открыть файл и прочитать его содержимое. Если произойдёт ошибка (например, если файл не существует), управление перейдёт в блок `finally`.
<br>2. `finally`: Этот блок выполнится в любом случае — даже если в блоке `try` возникло исключение. Здесь мы проверяем, был ли открыт файл, и закрываем его, чтобы избежать утечек ресурсов.

- Что нужно сделать, чтобы реализовать 
свое собственное __исключение__?

Чтобы реализовать свое собственное исключение, нужно создать новый класс, который наследуется от встроенного класса Exception. Затем можно добавлять дополнительные атрибуты и методы по необходимости.
```
class MyCustomError(Exception):
    pass
```
- Чем итератор отличается от генератора?

__Итератор__ — это объект, который реализует методы `iter__()` и `next__()`. __Генератор__ — это специальная функция, которая возвращает итератор с помощью ключевого слова `yield`. Генераторы проще в реализации и занимают меньше памяти, так как не требуют хранения всех значений сразу.

- В чем минусы декорирования функций?

1. Сложность понимания: Декораторы могут усложнить чтение и понимание кода, особенно для тех, кто не знаком с этой концепцией. Код, обернутый в декораторы, может выглядеть менее очевидным.

2. Отладка: Ошибки в декораторах могут быть трудными для отладки. Если декоратор вызывает исключение, это может затруднить определение места возникновения проблемы.

3. Потеря метаданных: При использовании декораторов оригинальная функция может потерять свои метаданные (например, имя и документацию). Это можно исправить с помощью функции functools.wraps, но не все разработчики об этом помнят.

4. Производительность: Декорирование может добавить накладные расходы на производительность, особенно если декоратор выполняет сложные операции или оборачивает множество функций.

5. Неявное поведение: Декораторы могут скрывать логику выполнения функций, что делает поведение программы менее предсказуемым и трудным для анализа.

6. Сложность тестирования: Тестирование функций с декораторами может быть сложнее, так как нужно учитывать поведение как самой функции, так и декоратора.

7. Ограниченная гибкость: Декораторы часто принимают фиксированные аргументы и могут быть менее гибкими по сравнению с другими подходами к расширению функциональности функций.

8. Множественные декораторы: При использовании нескольких декораторов порядок их применения имеет значение, что может привести к неожиданным результатам и сложности в управлении.
   
## Задания:
1) Доработайте класс комплексного числа из прошлого 
занятия: переопределите математические 
операторы (__+, -, /, *, ==__), так, чтобы они
работали с другими комплексными и со стандартными
числами. Добейтесь правильной работы с комплексным 
числом функций `print()`, `abs()`, а также
реализуйте `getter` и `setter` 
с использованием декоратора `@property`. Добавьте 
выбросы исключений при некорректном использовании 
вашего числа, например: выбросом `ValueError` при вводе 
некорректных значений в `setter` класса, выбросом своего исключения в 
случае попытки перевода в экспоненциальную 
форму, когда это невозможно. Поверх напишите программу 
калькулятор, принимающую у пользователя два комплексных
числа и проводящую с ними арифметические операции на
выбор пользователя. Калькулятор должен уметь ловить и 
обрабатывать исключения, не роняя программу,
а объясняя пользователю, что пошло не так.
2) Реализуйте класс связного списка `LinkedList`. 
(Вам потребуется реализовать вспомогательный класс `Node`,
содержащий в себе ссылки на соседей, и свое значение. Тогда
сам список содержит в себе лишь ссылку на первую вершину,
и вспомогательные данные вроде текущей длины). Список 
должен поддерживать обращение по индексам, красиво печататься,
выдавать длину через `len()` и иметь работающие методы
`.pop()`, `.append()`. Также список должен поддерживать
итерацию по нему. *Можете также добавить `.insert()` и 
`.pop()` по индексу.
3) Реализовать структуру наследования классов 
геометрических фигур *shape*. Каждый 
класс должен обладать методами `.area()`_ и 
`.perimeter()` для вычисления площади и 
периметра соответственно, а также метод `__str__()`. Среди обязательных для 
реализации структур: круг, треугольник, 
прямоугольник, квадрат, ромб. Для простоты часть фигур
можно конструировать из точек, 
передающихся в порядке обхода фигуры по 
часовой стрелке.