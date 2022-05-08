# FAST-API-freecodecamp-course

Course link: https://www.youtube.com/watch?v=0sOvCWFmrtA

Course github: https://github.com/Sanjeev-Thiyagarajan/fastapi-course

Create main.py file

Create virtual env by running

python3 -m venv myvenvname

Activate the venv by running:

source venv/bin/activate

To run the app on the server uvicorn:

uvicorn main:app

CRUD: Create Read Update Delete

18:08:25

Testing --> 16:30

For hashing passwor, install ```pip install "passlib[bcrypt]"```

Old process - not to use
```
my_posts = [{"title": "title of post 1", "content": "content of post 1", "id": 1}, {"title": "favorite food",
"content": "i like pizza", "id": 2}]

def find_post(id):
    for p in my_posts:
        if p["id"] == id:
            return p

def find_index_post(id):
    for i, p in enumerate(my_posts):
        if p["id"] == id:
            return i

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/sqlalchemy")
async def test_posts(db: Session = Depends(get_db)):

        posts = db.query(models.Post).all()

        return posts

```

To read an environment variable with python

```
import os

path = os.getenv("Path")

print(path)

```

To set envirionmental variable on MAC/LINUX

```
export MY_DB_URL="localhost:5432"

```
OR we can create the .env file and set all the variables thre with the export command

and then make: ``` source .env ``` to set the variables
OR without export command make: ``` set -o allexport; source /home/fastapi/.env; set +o allexport ``` 
To remove an envrionment variable

``` unset MY_DB_URL ```

To read all envrionment variables
```
printenv
```

To access the envrionment variable on Mac/Linux

```
echo $MY_DB_URL

```

Decode JWT token

https://jwt.io/


Alembic commands:

```
alembic upgrade <revision number>
```
To modify or create a new table, we need to create a revision (it looks like commits in github):

```
alembic revision -m "add content column to posts table"


alembic upgrade head

alembic upgrade +1

alembic upgrade -2

alembic revision --autogenerate -m "Add vote table with auto-generate"

```

To make a call from a browser

- Go on google.com
- right click, click 'inspect'
- Go to console and writte ```fetch('http://localhost:8000/').then(res => res.json()).then(console.log) ```

You first need to resolve Core policy before it works.


To install requirements

pip install -r requirements.txt

start heroku console

https://devcenter.heroku.com/articles/getting-started-with-python#start-a-console


To start app with gunicorn:
``` gunicorn -w 4 -k uvicorn.workers.UvicornWorker main:app --bind 0.0.0.0:8000 ```


To create a domain name for the app in order to have https domain go to:

https://www.namecheap.com/

Set up Firewall rules

sudo ufw allow http

sudo ufw allow https

sudo ufw allow ssh

sudo ufw allow 5432

sudo ufw enable

To delete a rule:

sudo ufw delete allow https


docker-compose up -d

docker-compose -f docker-compose-dev.yml up -d --> with custom nam of docker-composer.yml file

docker-compose down

docker ps

docker logs fastapi_1


docker exec -it fastapi_1 bash --> to connect to the container terminal

docker exec -it asynctask_airflow_run_1110b2b68aa6 bash
pytest -v -s --> To print result during the test