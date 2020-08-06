# AnimePiK Bot

[Открыть бота в Telegram](http://t.me/animepik_bot)

## Инструкции по запуску бота
### Параметры бота (.env)
```.env
# Bot
API_TOKEN=ваш токен бота

# Postgres
POSTGRES_SERVER=db
POSTGRES_USER=postgres
POSTGRES_PASSWORD=changethis # поставте более надежный пароль для продакшена
POSTGRES_DB=app
```
### Подготовка БД
```shell script
docker-compose run bot bash /app/migrate.sh
```
### Запуск бота
**Для продакшена**
```shell script
docker-compose -f docker-compose.yml up -d
```
**Для разработки**
```shell script
docker-compose up
```