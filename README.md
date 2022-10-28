# DevOps_exam

Стек: 
- caddy (Debian, Ubuntu, Raspbian)
- postgresql (final relise)
- uwsgi
- python app (flask, psycopg2) 

На целевой машине - два активных эндпоинта:
- корневой с выводом Hello World.
- /ping_db - выдает есть ли конект к базе (возвращает "Живая" или "Не живая")
