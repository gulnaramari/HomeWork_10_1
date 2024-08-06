# Проект "Виджет".

## Описание:
Проект - это приложение на Python для виджета банковских операций клиента.

## Установка:
1. Клонируйте репозиторий:
```
git@github.com:gulnaramari/HomeWork_10_1.git
```
2. Установите зависимости:
```
pip install -r requirements.txt

```
## Использование:
1. Откройте приложение на вашем компьютере.
2. Создайте новый проект и начните добавлять названия и номера банковских карт и время проведения банковской операции. 
3. Возможности приложения:
-Тестирование правильности маскирования номера карты или счета;
-Проверка работы приложения на различных входных форматах номеров карты(счета), включая граничные случаи и нестандартные длины номеров;
-Проверка, что приложение корректно обрабатывает входные строки, где отсутствует номер карты(счета);
-Проверка работы приложения на различных входных форматах даты, включая граничные случаи и нестандартные строки с датами;
-Проверка работы приложения (модуля generators.py) на фильтрацию транзакций по заданной валюте (или ее отсутствию). Проверка на
корректную работу приложения при обработке пустого списка или списка без соответствующих валютных операций. 
-Проверка работы приложения на корректные описания для каждой транзакции.
выдает правильные номера карт в заданном диапазоне.
-Проверка работы приложения на генерацию правильных номеров карт в заданном диапазоне и корректность их форматирования.

4. Для получения дополнительной информации обратитесь к [документации](docs/README.md).

Информация о тестировании приложения:
см. в файле [отчет о тестировании от 31.07.2024_17.59].
Общий процент покрытия приложения тестами составляет 96%.
src\__init__.py                0      0   100%
src\generators.py             24      3    88%
src\masks.py                  40      2    95%
src\processing.py             33      1    97%
src\widget.py                 22      2    91%
tests\__init__.py              0      0   100%
tests\conftest.py              5      1    80%
tests\test_gen.py             24      0   100%
tests\test_masks.py           50      0   100%
tests\test_processing.py      28      0   100%
tests\test_widget.py          29      1    97%
----------------------------------------------
TOTAL                        255     10    96%



## Лицензия:

Этот проект лицензирован по [лицензии MIT](LICENSE).