# secret-santa

## Description of Project
Able to send who your secret santa is through email.

If you wish to support me, feel free to tip here :)

[!["Buy Me A Coffee"](https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png)](https://www.buymeacoffee.com/xfortisfye)


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
EMAIL = ["email1", "email2", "email3"]
```
3. Run the program and head to http://127.0.0.1:5000 to generate secret santa to your respective friends' email
