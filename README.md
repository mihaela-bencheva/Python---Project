# Python---Project - Course Work

This is a basic python project that is used for getting the data you want from a given website, storing it and visualizing it.

# Running the project using Docker

To create a container in Docker and run the project:

```bash
docker run --rm -it -v [the project's directory path]:/app -w /app python:3.10 bash
```

Then install pipenv:

```bash
pip install pipenv
```

And install the libraries that are used in the project:

```bash
pipenv install requests bs4
```

And finally run the script:

```bash
pipenv run python main.py
```
