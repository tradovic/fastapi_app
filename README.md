### Setting up our development environment

create a virtual environment
```
python3 -m venv <env-name>
```

activate the virtual environment, run 
```
source <env-name>/bin/activate
```

In the directory where you want to start your project, run 
```
mkdir <my_app>
```

Run cd demo_app
Run pip install fastapi
Run pip freeze > requirements.txt to create a requirements file in the <my_app> folder with all the installed dependencies

install uvicorn if it is needed
```
pip install uvicorn
```

run 
```
uvicorn main:app --reload to start your FastAPI application.
```