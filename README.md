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
- mysql> `CREATE DATABASE icecoldportal;`


### Python install instructions (for mac)
- `brew install python3` # need python 3.6
- `brew install caskroom/cask/mysql-connector-python`
- `cd` /<PATH_TO_THE_ICECOLDPORTAL_PROJECT_ROOT/
- `python3 -m virtualenv venv`
- `source venv/bin/activate`
- `pip install --upgrade pip`
- `pip install -r requirements.txt`

### setup your local application config
- Please change the password in **icecoldportal/settings/settings_local.py** to the password you create in the database setup section


### setup your local database
- `python manage.py migrate`

### run the app
- python manage.py runserver

## Visit `127.0.0.1:8000` or `localhost:8000` in your browser to verify setup Completed
- If any of the above steps, please update README with the correct order


