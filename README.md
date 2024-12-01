# Задание №3

## Описание
Разработать инструмент командной строки для учебного конфигурационного языка, синтаксис которого приведен далее. Этот инструмент преобразует текст из входного формата в выходной. Синтаксические ошибки выявляются с выдачей сообщений.

Входной текст на учебном конфигурационном языке принимается из файла, путь к которому задан ключом командной строки. Выходной текст на языке YAML попадает в стандартный вывод.

### Формат входных данных:
- **Массивы**: `#( значение значение значение ... )`
- **Имена**: `[a-zA-Z]+`
- **Значения**:
  - Числа.
  - Массивы.
---
### Конструкции:
1. **Объявление константы на этапе трансляции**:
   - `def имя := значение`
2. **Вычисление константы на этапе трансляции**:
   - `@{имя}`
   - Результатом вычисления константного выражения является значение.
---
### Команды:
- **def имя := значение** — позволяет объявить новую константу.
- **@{имя}** — вычисляет значение константы по имени.
---
### Требования:
1. **Транслятор**:
   - Преобразует текст из учебного конфигурационного языка в YAML.
   - Путь к файлу с конфигурацией задается через ключ командной строки.
   - Все ошибки синтаксиса должны быть обработаны с выводом сообщений о неверных конструкциях.
   
2. **Пример**:
   Пример входных данных:

```
def a := 10
def b := #( 1 2 3 )
c := @{a}
```
---
Пример выхода:
```yaml
a: 10
b:
  - 1
  - 2
  - 3
c: 10
```
---
Описание функций
1. `parse_config(input_file)`

Назначение: Читает конфигурационный файл и преобразует его содержимое в структуру данных.
Параметры:

    input_file (str): Путь к конфигурационному файлу.

Возвращает: Структуру данных, соответствующую YAML.
2. `parse_definition(line)`

Назначение: Парсит строку объявления константы.
Параметры:

    line (str): Строка с определением константы.

Возвращает: Кортеж с именем и значением константы.
3. parse_constant(name)

Назначение: Возвращает значение константы по имени.
Параметры:

    name (str): Имя константы.

Возвращает: Значение константы.
4. `parse_value(value)`

Назначение: Парсит строку значения (число или массив).
Параметры:

    value (str): Строка со значением.

Возвращает: Число или массив значений.
5. `parse_array(value)`

Назначение: Парсит строку, представляющую массив значений.
Параметры:

    value (str): Строка с массивом.

Возвращает: Список значений массива.
6. `parse_expression(expression)`

Назначение: Парсит выражение с вычислением констант.
Параметры:

    expression (str): Строка с выражением.
---
Возвращает: Значение выражения, включая вычисление констант.
Пример конфигурации
Пример 1:

```
def server_name := "example.com"
def port := 8080
def routes := #( "/home" "/about" "/contact" )

server:
  name: @{server_name}
  port: @{port}
  routes: @{routes}

Пример 2:

def db_host := "localhost"
def db_port := 5432
def db_credentials := #( "user" "password" )

database:
  host: @{db_host}
  port: @{db_port}
  credentials: @{db_credentials}
```
---

Запуск

![изображение](https://github.com/user-attachments/assets/26c888c1-23e0-4353-b6f3-c4ffe630e350)


---

Тестирование

![изображение](https://github.com/user-attachments/assets/9d644e54-95ad-4fdb-9ae9-b4e3cd1d7f99)
