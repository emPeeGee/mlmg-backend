# Commands cheatsheet

## Creating docker container
1. Create dockerfile
2. `docker compose up -d pg`

## Docker
1. docker ps -a - List proccesses
2. docker stop <id> - Stop it
3. docker start <id> - Start it


## get inside the db
1. `docker ps` List processes
2. `docker exec -it #id bash` Connect to docker instance
3. `psql -U postgres mlmg` Connect to database


## posgresql
1. `DROP SCHEMA public CASCADE; CREATE SCHEMA public;`. Deletes all tables from db
2. \d, \dt, \l, \q

 ## Start the app
1. poetry run python app/main.py 