# Проект по автоматизации API и UI тестирования на Python для веб-сервиса строительной компании Kronverk

***
[Проект Kronverk ](https://kronverk.bureausuchkov.com/)направлен на создание эффективной системы тестирования для
проверки функциональности веб-платформы. 'Кронверк' -
ведущий игрок на рынке недвижимости, занимающийся проектированием, строительством и продажей объектов более 20 лет.
Целью автоматизации является повышение качества и надежности веб-сайта, а также снижение затрат на ручное
тестирование.<br>
Для проекта был выбран функционал, доступный в веб-интерфейсе
и через REST API. Составлено 5 UI- и 5 API-автотестов, для формирования отчета о проведенных автотестах используется
инструмент Allure.

## Шаги

1. Склонировать проект `git clone https://github.com/BNKA1993/Diplom_project`
2. Установить зависимости
3. Запустить тесты с указанием пути к директории результатов тестирования `pytest --alluredir allure_files`
4. Сформировать отчет `allure generate allure-files -o allure_report`
5. Открыть отчет `allure open allure_report`

## Стек

- pytest<br>
- selenium<br>
- requests<br>
- allure<br>
- config<br>

## Структура

- ./test - тесты
    - \_\_init\_\_.py
    - /api_test.py - API-тесты
    - /ui_test.py - UI-тесты
- ./web_pages - описание страниц
    - /CompanyApi.py - описание API-методов
    - /MainPage.py - описание методов на главной странице
    - /ResultPage.py - описание результатов
- ./pytest.ini - файл конфигурации для pytest, который содержит настройки тестирования, такие как параметры командной
  строки и плагины.
- README.md - файл с документацией проекта, в котором описаны установка, использование, структура проекта и другие
  важные аспекты.
- requirements.txt - файл с используемыми зависимостями
- run.sh - файл с командами для автоматизированного прогона и сохранения результатов проведенных проверок



## Полезные ссылки

- [Проект Kronverk: тест план + отчет о тестировании ](https://juniper-ranunculus-9dd.notion.site/d832f3802f1a4a9787b554f76577a373?pvs=4)
- [Веб-интерфейс сервиса Kronverk ](https://kronverk.bureausuchkov.com/)

## Библиотеки

- pip3 install pytest
- pip3 install selenium
- pip3 install webdriver-manager
- pip3 install allure-pytest
- pip3 install requests

## Запуск тестов

- `pytest | python3 -m pytest` (запуск тестов)
- `python3 -m pytest -s` (вывод в консоль print)
- `python3 -m pytest -v` (запуск тестов с подробным выводом в консоль)
- `python3 pytest -m ui_test.py` (запуск только UI тестов)
- `python3 pytest -m api_test.py` (запуск только API тестов)
- `python3 -m pytest --alluredir allure-result` (запуск тестов и сохранение отчета о результатах тестирования)
- `python3 allure serve allure-result/` (формирование отчета о тестировании)
