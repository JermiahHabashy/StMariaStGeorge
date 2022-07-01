import flask
from flask import Flask, render_template, request, redirect, url_for, session
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import column_property
from sqlalchemy import join, ForeignKey, select

import csv

app = flask.Flask(__name__)
app.config['SECRET_KEY'] = 'giu94c478d5ze6ge1r6eq39f'

Bootstrap(app)

# CONNECT TO DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///menus.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db: SQLAlchemy = SQLAlchemy(app)


# CONFIGURE TABLE
class FoodNL(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(250), nullable=False)
	description = db.Column(db.String(250), nullable=True)
	price = db.Column(db.DECIMAL(5, 2), nullable=False)
	cat_id = db.Column(db.Integer, db.ForeignKey("categoryNL.cat_id"))


class CategoryNL(db.Model):
	cat_id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(250), nullable=False)
	foods = db.relationship("FoodNL", backref="categoryNL")


class FoodENG(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(250), nullable=False)
	description = db.Column(db.String(250), nullable=True)
	price = db.Column(db.DECIMAL(5, 2), nullable=False)
	cat_id = db.Column(db.Integer, db.ForeignKey("categoryENG.cat_id"))


class CategoryENG(db.Model):
	cat_id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(250), nullable=False)
	foods = db.relationship("FoodENG", backref="categoryENG")


class FoodFR(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(250), nullable=False)
	description = db.Column(db.String(250), nullable=True)
	price = db.Column(db.DECIMAL(5, 2), nullable=False)
	cat_id = db.Column(db.Integer, db.ForeignKey("categoryFR.cat_id"))


class CategoryFR(db.Model):
	cat_id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(250), nullable=False)
	foods = db.relationship("FoodFR", backref="categoryFR")


db.session.commit()
db.create_all()

# TODO: schrijf script dat andere talen naar foodEND en foodFR importeert
# 		vervang , die tussen "" staan door een è via word macro
# 		copy paste de waarden
#		scrhijf code die è vervangt door ,



@app.route('/')
def nl():
	return flask.render_template("indexNL.html",
								 all_cat=db.session.query(CategoryNL).all(),
								 food_list=db.session.query(FoodNL))

@app.route('/eng')
def eng():
	return flask.render_template("indexENG.html",
								 all_cat=db.session.query(CategoryENG).all(),
								 food_list=db.session.query(FoodENG))


@app.route('/fr')
def fr():
	return flask.render_template("indexFR.html",
								 all_cat=db.session.query(CategoryFR).all(),
								 food_list=db.session.query(FoodFR))



if __name__ == "__main__":
	app.run(debug=True)
