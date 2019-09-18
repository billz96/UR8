# UR8
LATEST EDITION: https://github.com/tigerlero/UR8

In this project our team will be creating a simple and **_`not beautiful`_** YouTube **_`clone`_**.

It will include:
- [ ] Video Rating
- [ ] Video Review
- [ ] Like/ Dislike Reviews
- [ ] Recommended Videos
- [x] Image Uploading
- [x] Video Uploading
- [x] Update Video
- [x] Delete Video
- [x] Password Reset
- [ ] Channel

### Enjoy!!

## Requirements

1. Python 3
2. Django
3. Bootstrap
4. Postgres
5. psycopg2 (`pip3 install psycopg2`)
6. A database named "DjangoDB"

## Usage
* Clone/Download Repo Locally
* In "UR8-master/ur8_proj/settings.py" change the 'USER' and 'PASSWORD' fields in the "DATABASE" dictionary to your postgres account
* Move to the "UR8-master" directory
* Run the following commands:
  * python3 manage.py makemigrations 
  * python3 manage.py migrate
  * python3 manage.py runserver
* In your browser go to "http://127.0.0.1:8000/ur8/"
