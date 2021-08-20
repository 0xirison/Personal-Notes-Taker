# Introduction
Personal Notes Taker application allows you to write, edit and delete your own notes on a simpe web application interface. It is built by Python (Flask Microframework) as the backend and uses SQLAlchemy module extension for flask to connect to the database.

# Installation
```
git clone https://github.com/0xirison/Personal-Notes-Taker.git
```
```
pip3 install -r requirements.txt
```

# Usage
```
python notes.py
```
then open the application in your browser by writing: 127.0.0.1:5000


# Features
- representing each note as a card
- random colorful card for every page refresh
- simple notes cards animation (transforming)
- write, edit and delete notes
- showing last modified date of notes
- light touch of security for input validations attacks
- responsive for mobile devices and others

# Upcoming Features
- search feature for notes
- notes content encryption
- recently deleted notes
- Notes lock

# Common Issues
- If the application does not work with you properly and showed 'Internal Server Error', change the default running port '5000' of it and run it again
- If the problem still exists, make sure that you have all requirements mentioned above

# Screenshot
![alt text](https://i.postimg.cc/yN0nB1cQ/notes.png)

