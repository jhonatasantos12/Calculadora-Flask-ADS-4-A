# SQLAlchemy ORM Tutorial for Python Developers


## Useful Commands

```bash
# starting a dockerized instance of PostgreSQL
docker run --name sqlalchemy-orm-psql \
    -e POSTGRES_PASSWORD=dbpassword \
    -e POSTGRES_USER=dbuser \
    -e POSTGRES_DB=sqlalchemy-orm-tutorial \
    -p 5432:5432 \
    -d postgres

# running basic example
python -m examples.basic

# running one to one example
python -m examples.onetoone
```



     git clone https://github.com/antoniodiasabc/sqlalchemy
     cd sqlalchemy/
     ls -lrt
     docker pull mysql:5.7
     docker run --name mysql5 -e MYSQL_ROOT_PASSWORD=mudar123 -p 3306:3306 -d mysql:5.7
     docker ps
     docker exec -it 257d598cec09 /bin/bash
     mysql -uroot -p
     create schema teste;
     
      
    pip install sqlAlchemy
    pip install PyMySQL
    python3 -m examples.basic
