# Introduction
Personal Notes Taker application allows you to write, edit and delete your own notes on a simple web application interface. It is built by Python using Flask micro-framework as the back-end and SQLAlchemy extension module for flask to connect to the database.

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
- showing last modified dates of notes
- light touch of security for input validations attacks
- responsive for mobile devices and others

# Upcoming Features
- search feature for notes
- notes content encryption
- recently deleted notes
- notes lock
- showing notes creation dates
- pagination

# Common Issues
- If the application does not work with you properly and showed 'Internal Server Error', change the default running port '5000' of it and run it again because it may be that you have a process using the same port
- If the problem still exists, make sure that you have all requirements mentioned above

# Screenshot
![alt text](https://i.postimg.cc/yN0nB1cQ/notes.png)

