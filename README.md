# Using Poetry

## Representive Commands

- Install Poetry
```
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py | python -
```

- Create project
```
poetry new <project name>
```

- Init project
```
poetry init
```

- Create virtualenv on project directory
```
peotry config --list
```
If the result of "virtualenvs.in-project" is null or false, you should run below command

```
poetry config virtualenvs.in-project true --local
```