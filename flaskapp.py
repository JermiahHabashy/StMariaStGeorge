# imports
import os
import flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

# flask init
app = flask.Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get("SECRET_KEY")

# bootstrap init
Bootstrap(app)

# connect to FB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///static/database/menus.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db: SQLAlchemy = SQLAlchemy(app)


# configure tables
class FoodNL(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(250), nullable=False)
	description = db.Column(db.String(250), nullable=True)
	price = db.Column(db.DECIMAL(5, 2), nullable=True)
	cat_id = db.Column(db.Integer, db.ForeignKey("categoryNL.cat_id"))

class CategoryNL(db.Model):
	cat_id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(250), nullable=False)
	foods = db.relationship("FoodNL", backref="categoryNL")

class FoodENG(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(250), nullable=False)
	description = db.Column(db.String(250), nullable=True)
	price = db.Column(db.DECIMAL(5, 2), nullable=True)
	cat_id = db.Column(db.Integer, db.ForeignKey("categoryENG.cat_id"))

class CategoryENG(db.Model):
	cat_id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(250), nullable=False)
	foods = db.relationship("FoodENG", backref="categoryENG")

class FoodFR(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(250), nullable=False)
	description = db.Column(db.String(250), nullable=True)
	price = db.Column(db.DECIMAL(5, 2), nullable=True)
	cat_id = db.Column(db.Integer, db.ForeignKey("categoryFR.cat_id"))

class CategoryFR(db.Model):
	cat_id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(250), nullable=False)
	foods = db.relationship("FoodFR", backref="categoryFR")

# save and commit tables
db.session.commit()
db.create_all()

# routes
@app.route('/')
def nl():
	return flask.render_template("indexNL.html")

@app.route('/eng')
def eng():
	return flask.render_template("indexENG.html")

@app.route('/fr')
def fr():
	return flask.render_template("indexFR.html")

# query right language menu and send with html file
@app.route('/menu')
def menu_nl():
	return flask.render_template("menuNL.html",
								 all_cat=db.session.query(CategoryNL).all(),
								 food_list=db.session.query(FoodNL))

@app.route('/menu_eng')
def menu_eng():
	return flask.render_template("menuENG.html",
								 all_cat=db.session.query(CategoryENG).all(),
								 food_list=db.session.query(FoodENG))

@app.route('/menu_fr')
def menu_fr():
	return flask.render_template("menuFR.html",
								 all_cat=db.session.query(CategoryFR).all(),
								 food_list=db.session.query(FoodFR))

# run site
if __name__ == "__main__":
	app.run(debug="off")
