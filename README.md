# retail

## Initialize Database
You can find sql files under the directory of `db` to initialize the database. You can use docker to run a MySQL server in your local enviornment.

```
docker run --name mysql -e MYSQL_ROOT_PASSWORD=yourpassword -d mysql
```

## Create a file `config.ini` under the root directory
```
[postgresql]
host=
database=
user=
password=
``` 

## How to test functions

### connect
```
pip install -r requirements.txt

python connect.py
```