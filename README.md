# FAST-API-freecodecamp-course

Course link: https://www.youtube.com/watch?v=0sOvCWFmrtA

Create main.py file

Create virtual env by running

python3 -m venv myvenvname

Activate the venv by running:

source venv/bin/activate

To run the app on the server uvicorn:

uvicorn main:app

CRUD: Create Read Update Delete

9:50:25

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


