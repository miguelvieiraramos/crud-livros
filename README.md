# Crud Livros

Simple crud in flask.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Installing

A step by step series of examples that tell you how to get a development env running

Creating an virtual enviroment
```
make venv
```

Entering the virtual enviroment
```
source .venv/bin/activate
```

Installing all the dependencies
```
make init
```

Creating an enviroment variable called SECRET_KEY
```
export SECRET_KEY="your secret key"
```

Creating an enviroment variable called SQLALCHEMY_DATABASE_URI. This should be a string that makes your application connects to a database. 
The following string connects to a postgres database but you can connect to any database supported by sqlalchemy.
```
export SQLALCHEMY_DATABASE_URI="postgresql://user:password@localhost/database"
```

Creating the tables and app context.
In a nutshell:
```
>>> from crud_livros import create_app, db
>>> app = create_app()
>>> app.app_context().push()
>>> db.create_all()
```
## Running
```
python run.py
```


