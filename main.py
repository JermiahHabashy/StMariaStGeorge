import os
import flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

app = flask.Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get("SECRET_KEY")

Bootstrap(app)

# CONNECT TO DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///static/database/menus.db'
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


# TODO:
#		2. vertaal word doc naar FRA
#		3. copy waarden van word indexFR
#		4. copy waarden van word naar foodFR en categoryFR
#		5. zet fotos in imgs
#		6. reformat folder structure
#		6a. nieuwe prijzen
#		7. zet op hostinger
# 		8. contact Ashraf voor domeinnaam
#		9. maak factuur op


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
	app.run()
