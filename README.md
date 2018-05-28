# IceColdPortal
Web Application that will serve as summer project for Bruhs looking to add to their computing experience.


# Local Environment Setup

## Prerequisties/Dependencies
### Please check whether or not a dependency already exists on your machine before attempting to install
- Homebrew https://docs.brew.sh/Installation



### Database setup instructions
- `brew install mysql`
- `brew services start mysql`
- `mysql -u root -p`
- Enter your password
- mysql> `CREATE DATABASE icecoldportal;` **Important**

### Python install instructions (for mac)
- `brew install python3` # need python 3.6
- `brew install caskroom/cask/mysql-connector-python`
- `cd` /<PATH_TO_THE_ICECOLDPORTAL_PROJECT_ROOT/
- `python3 -m virtualenv venv`
- `source venv/bin/activate`
- `pip install --upgrade pip`
- `pip install -r requirements.txt`
  - On mac you may get stuck on this line due to mysqlclient not being properly installed on the venv
  - run `xcode-select --install` 
  - then `pip install -v mysqlclient`
  - re-run `pip install -r requirements.txt` and make sure they are satisfied 

### setup your local application config
- Please change the password in **icecoldportal/settings/settings_local.py** to the password you create in the database setup section


### setup your local database
- `python manage.py migrate`
  - if you get stuck run `pip install django`
  - If you get an error like this `django.db.utils.OperationalError: (1045, "Access denied for user 'root'@'localhost' (using password: YES)")` your password in settings_local.py is probably wrong
#### To reset your password: 
  - `mysql -u root`
  - `mysql> USE mysql;`
  - `mysql> UPDATE user SET authentication_string=PASSWORD("NEWPASSWORD") WHERE User='root';`
  - `mysql> FLUSH PRIVILEGES;`
  - `mysql> quit`

### run the app
- python manage.py runserver

## Visit `127.0.0.1:8000` or `localhost:8000` in your browser to verify setup Completed
- If any of the above steps, please update README with the correct order


