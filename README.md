## Тестовое задание для фронта

В репозитории небольшой вебсервис сделанный как backend для тестового задания 
на вакансию Frontend reactJS developer. Ниже описано как, куда и какие данные 
он передает в клиентскую часть. Предпочтительнее разобраться и запустить наш
вебсервис, но вы можете написать аналогичный сервис на NodeJS например и 
использовать его. Но повторю, предпочтительнее разобраться и запустить наш 
бакенд. 

### Запуск бакенда 

Если у вас установлен docker и docker-compose просто запустите в каталоге с 
кодом **docker-compose up**, если нет создайте докер образ по файлу Dockerfile, 
запустите его и передайте в него команду **python3.6 server.py**.
Либо создайте в каталоге виртуальное окружение Python следующими командами:
```bash
    pyvenv-3.6 .env
    source .env/bin/activate
    python3.6 setup.py develop
    python3.6 server.py
```

### Что идет с бакенда?

В результате на порту localhost:8888 запустится вебсервер, откройте страницу 
http://localhost:8888, если все прошло нормально, вы увидите как через webcoket 
в консоль непрерывно (с небольшим случайным интервалом 0,1-0,3сек)
идут сообщения в JSON формате
```json
{
    "x": 12,    /* номер столбца, случайное число от 0 до 99  */
    "y": 21,    /* номер строки, случайное число от 0 до 99   */
    "n": 100.5  /* случайное число число от -999.99 до 999.99 */
}
```

### Тестовое задание

Ваша задача с помощью reactJS построит таблицу 40 на 40 активных ячеек и 
панель слева в которой будет размещаться список. Сильно заморачиваться с 
дизайном не надо, как-то так.

    +------------+ +--------+--------+--------+--------+--------+
    | +--------+ | |        |        |        |        |        | 
    | | 500.12 | | +--------+--------+--------+--------+--------+
    | +--------+ | |        | 500.12 |        |        |        |
    | +--------+ | +--------+--------+--------+--------+--------+
    | | 150.25 | | |  42.25 |        |        |-715.27 |        |
    | +--------+ | +--------+--------+--------+--------+--------+
    | +--------+ | |        |        |        |        |        |
    | |-715.27 | | +--------+--------+--------+--------+--------+
    | +--------+ | |        |-872.25 |        |        |-102.80 | 
    |            | +--------+--------+--------+--------+--------+
    |            | | 482.02 |        |        |  42.02 |        |
    |            | +--------+--------+--------+--------+--------+
    +------------+ |        |        | 150.25 |        |        |
                   +--------+--------+--------+--------+--------+
                   |        |        |        |        |   5.20 |
                   +--------+--------+--------+--------+--------+
               
Необходимо заполнять таблицу приходящими данными (значение в поле "n", 
координаты в "x" "y"). Положительные числа синим, отрицательные красным цветом. 
Если ячейка не получала значения больше 5 сек, содержимое должно быть стерто 
(желательно плавно обесцвечиваясь в течении 5 сек).

### Задание на Бис!

Претендующим на senior обязательно. При клике мышкой на ячейке таблицы, в списке 
на панеле слева должна появляться ячейка являющаяся копией той на которой был клик. 
Если исходная ячейка получила новое значение меньше чем за 5 сек, то и копия в 
списке должна обновиться. Если исходная ячейка не получила новое значение в течении 
5 сек, то ее копия из списка удаляется.
