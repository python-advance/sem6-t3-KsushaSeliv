Сравненеие фреймворков (Python)

Протестируем фреймворки. 
Тест: DB Test, в котором мы получаем строковые данные из базы данных и возвращаем их в
виде html-ответа (1 запись в 79 bytes). В качестве базы данных использовался Postgres 11. В качестве драйвера обращений
к базе использовался psycopg2 в случае синхронных фреймворков и asyncpg в случае асинхронных.
В качестве event loop библиотеки для асинхронных фреймворков решили использовать uvloop.

Участники тестирования: Django, Flask, AioHTTP, Sanic, Tornado, Vibora.

Запросов в секунду:

![alt](https://github.com/python-advance/sem6-t3-KsushaSeliv/blob/master/1.png)

Передача данных в секунду:

![alt](https://github.com/python-advance/sem6-t3-KsushaSeliv/blob/master/2.png)

Среднее время запроса:

![alt](https://github.com/python-advance/sem6-t3-KsushaSeliv/blob/master/3.png)

Максимальное время запроса:

![alt](https://github.com/python-advance/sem6-t3-KsushaSeliv/blob/master/4.png)

Финальные результаты

![alt](https://github.com/python-advance/sem6-t3-KsushaSeliv/blob/master/5.jpg)
