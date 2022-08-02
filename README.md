# Django User Authentication Template

This is a django user authentication project that you can always build upon.

## Featuring/Functionality
    - Registration Feature
    - Login Feature
    - Logout Feature
    - Reset password
    - with boostrap enabled

## Screenshots
| Home | Log In | Create an account |
| -------|--------------|-----------------|
| <img src="./screenshots/home.png" width="200"> | <img src="./screenshots/login.png" width="200"> | <img src="./screenshots/create_an_account.png" width="200"> |

| Password reset | verifying page | Password change |
| ---------------|------------------|-----------------|
| <img src="./screenshots/password_reset.png" width="200"> | <img src="./screenshots/verifying_page.png" width="200"> | <img src="./screenshots/change_password.png" width="200"> |


## Installation

> To use this project you must have *python*,  *pip*, *virtualenv* installed

### Clone the project

```git
git clone https://github.com/winninggodspower/Django_user_authentication_template.git
```

### create a virtual environment

unix / mac

```pyhton
virtualenv virtualenv_name
```

windows

```pyhton
virtualenv myenv
```

## activate the virtual environment
unix / mac

``` python
virtualenv -p /usr/bin/python3 virtualenv_name
```

windows

``` python
myenv\Scripts\activate
```



### Install project dependency

``` console
pip install -r requirements.txt
```

### Start development server with the following commands

```` console
python manage.py migrate
python manage.py makemigrations
python manage.py runserver
````

> ps: when ever you want to start the development server you only have to run: ```` python manage.py runserver ````




