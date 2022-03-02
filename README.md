# secret-santa

## Description of Project


## Setting Up
1. Install [Python 3.8.5 and pip](https://github.com/xfortisfye/303-see-other/blob/main/coding-language.md#python)
2. Installing dependencies
    1. Install pip requirements
    ```bash
    > cd \Path\to\root-folder
    > pip install -r requirements.txt
    ```
- - - -

## Usage
1. Initialise your email and password value in ***app.py***
```python
MAIL_USERNAME = "your_email"
MAIL_PASSWORD = "your_password"
```
2. Initialise the name and email of respective friends in order in ***app.py***
```python
NAME = ["name1", "name2", "name3"]
EMAIL = ["fakeemail1", "fakeemail2", "fakeemail3"]
```
3. Run the program and head to http://127.0.0.1:5000 to generate secret santa to your respective friends' email
