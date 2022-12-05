# Подготовка модуля к интеграции парсера

## Установка необходимых зависимостей

Выполните установку oxeekparser

``pip install oxeekparser``

## Импорт библиотеки в модуль

Импортируйте библиотеку, установленную в предыдущем шаге

``from oxeekparser import Parser``


## Настройка среды

1. Установите последнюю стабильную версию браузера Chrome
    https://www.google.com/intl/ru/chrome/browser-tools/


2. Загрузите последнюю стабильную версию ChromeDriver 
    https://chromedriver.chromium.org


3. Создайте папку с профилем Chrome или укажите папку профиля вашего собственного браузера

## Использование в модуле 

Создайте экземпляр класса Parser и перейдайте в качестве параметров:

    1. Путь до ChromeDriver
    2. Путь к профилю Chrome
    3. Время ожидания парсера




