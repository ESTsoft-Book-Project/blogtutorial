# Django Blog Tutorial

- **src**: [Build a Blog using Django, Python, and Bootstrap](https://youtu.be/sMqDJovFO-Y)
- 무작정 따라하면서 배우는 장고 블로그 만들기

## How to deploy?

1. `mkdir <your-dir-name>` => This is not a REAL project folder! for managing python virtual environments.
2. `cd <your-dir-name>`
3. `python -m venv env` ==> create virtual environment which is called `env`
4. `source env/bin/activate` ==> I don't know how to activate environments in Windows or MacOS
5. `git clone git@github.com:ESTsoft-Book-Project/blogtutorial.git`
6. `cd blogtutorial`
7. `pip install -r requirements.txt` ==> THE MOST IMPORTANT THING!
8. `./manage.py migrate` ==> migration is telling django to change state of DB. I don't know why this is required...
9. `./manage.py runserver` ==> as this command says, you'll be prompted some URL that can lead you to a blog! 🎈🎈🎉
