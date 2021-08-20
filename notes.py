from flask import Flask, render_template , url_for, redirect, request, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import date
import random, html, secrets


app= Flask(__name__)
app.config['SECRET_KEY'] = secrets.token_urlsafe(25)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///note.sqlite3"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class note(db.Model):
    id = db.Column("id" , db.Integer, primary_key= True)
    title = db.Column('title', db.String(500))
    content = db.Column('content', db.String(500))
    date = db.Column('date', db.String(20))

    def __init__(self, title,content,date ):
        self.title = title
        self.content = content
        self.date = date


@app.route("/")
@app.route("/notes")
def notes():
    all_notes = db.session.query(note).order_by(note.id)
    return render_template("notes.html" , notes = all_notes, random=random)

@app.route("/write_note" , methods =["POST", "GET"])
def write_note():
    if request.method == "POST":
        title = str(html.escape(request.form["write_title"]))
        content = str(html.escape(request.form["write_note"]))
        date = str(html.escape(calc_date()))
        message = note(title,content,date)
        db.session.add(message)
        db.session.commit()
        flash("The note has been created successfully", "info")
        return redirect(url_for("notes"),code=302)
    else:
        return render_template("write_note.html")


@app.route("/view_note/<int:id>", methods = ["GET", "POST"])
def view_note(id):
    if db.session.query(note.id).filter_by(id=id).first() is not None:
        if request.method == "POST":
            title = str(html.escape(request.form["view_title"]))
            content = str(html.escape(request.form["view_note"]))
            edited_note = note.query.filter_by(id=id).first()
            edited_note.title = title
            edited_note.content = content
            edited_note.date = calc_date()
            db.session.commit()
            flash("The note has been saved successfully", "info")
            return redirect(url_for("notes"),code=302)
        specific_note = note.query.filter_by(id=id).first()
        return render_template("view_note.html", message=specific_note)
    else:
        flash("Sorry, you can not view a nonexistent note", "critical")
        return redirect(url_for("notes"),code=302)


@app.route("/delete_note/<int:id>", methods=["GET"] )
def delete_note(id):
    if db.session.query(note.id).filter_by(id=id).first() is not None:
        note.query.filter_by(id=id).delete()
        db.session.commit()
        flash("The note has been deleted", "info")
        return redirect(url_for("notes"),code=302)
    else:
        flash("The note does not exist", "critical")
        return redirect(url_for("notes"),code=302)


@app.route("/delete_all", methods =["POST"])
def delete_all():
    if db.session.query(note).first():
        if request.method == "POST":
            db.session.query(note).delete()
            db.session.commit()
            flash("All notes have been deleted", "info")
            return redirect(url_for("notes"),code=302)
        else:
            flash("Please confirm your action before deleting all notes", "critical")
            return redirect(url_for("notes"),code=302)
    else:
        flash("There are no notes to be deleted", "critical")
        return redirect(url_for("notes"),code=302)


def calc_date():
    today = date.today()
    date_now = today.strftime("%b-%d-%Y")
    return date_now


if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)
