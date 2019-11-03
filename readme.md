**Instructions**

*Instuctions on setting up env from Conda*

Create a project directory

`<pythonprojects>/rlearning`
`cd <pythonprojects>/rlearning`

Use Conda to create the virtual env in-situ

`conda create -p $(pwd)/venv python=3.7`

_There will now be a venv directory tree with an install of python_

Activate the envionronment
`. activate ./venv`

Install the packages from requirements.txt

`pip install -r requirements.txt`

