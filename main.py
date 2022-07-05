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


db.session.commit()
db.create_all()


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

# van txt naar csv
# import csv
# import pandas as pd
#
# lines = '''Spaghetti pour enfants, (± 30 min. de préparation)
# Poitrine de poulet grillée,
# Boulettes amères,
# Frikandel,
# Gyros,
# Côtes levées,
# Pizza bambino,Avec une glace pour enfants en dessert
# Gelato bambino,Glace pour enfants
# Banana Royal, "Glace à la vanille avec banane, chocolat et crème fouettée"
# Dame blanche,Glace vanille avec chocolat et crème fouettée
# Yaourt grec au miel et aux noix,
# Moelleux au chocolat avec de la glace à la vanille,
# Margharita,Tomate et fromage
# Cipola, "Tomate, fromage et oignons"
# Salami, "Tomate, fromage et salami"
# Proscuito, "Tomate, fromage et jambon"
# Funghi, "Tomate, fromage et champignons"
# Proscuito & Funghi, "Tomate, fromage, jambon et champignons"
# Capriccosa: "Tomate, fromage, salami et champignons"
# Americana, "Tomate, fromage, salami et jambon"
# Peperoni, "Tomate, fromage, poivron et piments"
# Napolitana, "Tomate, fromage, anchois et olives"
# Hawaii, "Tomate, fromage, ananas et jambon"
# Siciliana, "Tomate, fromage, artichauts, poivrons et olives"
# Tonno, "Tomate, fromage, thon et oignons"
# Bolognaise, "Tomate, fromage, viande hachée et oignons"
# Bella italia, "Tomate, fromage, viande hachée et œuf"
# Boromea, "Tomate, fromage, jambon, champignons et oeuf"
# Vegetaria, "Tomate, fromage, poivron, champignons, artichauts, olives et oignons"
# Calzone, "Pizza dense et pliée avec tomate, fromage, champignons, artichauts, viande hachée et jambon"
# Shoarma, "Tomate, fromage, shoarma, poivron et oignons"
# Quattro stagioni, "Tomate, fromage, poivrons, champignons, jambon et salami"
# Lucky luciano, "Tomate, fromage, champignons, oignons, bacon et oeuf"
# Maffiosa, "Tomate, fromage, champignons, poivron, oignons et bacon"
# Pollo, "Tomate, fromage, poulet shawarma, champignons et oignons"
# O Solo Mio, "Tomate, fromage, champignons, artichauts, poivron, oignons, jambon et oeufs"
# Marinara, "Tomate, fromage, fruits de mer et anchois"
# Quattro formagi, "Tomate avec 4 fromages italiens
# Pizza Scampi, "Tomate, fromage et langoustines"
# Pizza Gerguis,Spécialité de la maison
# Extra viande,
# Extra légumes par type,
# Extra roquette,
# Kalamaria, calamars avec sauce fraîche
# Solomos,Saumon cuit sur le grill avec une sauce au citron et à l'aneth (+30 min. de préparation)
# Media saganaki, moules avec tomates fraîches dans une sauce épicée
# Fritto misto,Différentes sortes de poissons frits
# Gerides saganaki,Crevettes frites dans une sauce épicée
# Scampi griglia,Crevettes royales grillées
# Alla napolitan,Sauce tomate
# Alla funghi,Sauce tomate aux champignons
# Alla bolognaise,Sauce tomate à la viande hachée
# Alla carbonara, "Sauce crémeuse au fromage et au jambon"
# Santa Maria,Sauce au vin, à l'ail et au basilic
# Alla marinara,Sauce tomate aux fruits de mer
# Quattro formagio, Sauce crémeuse avec 4 sortes de fromage
# Alla polio, "Sauce crémeuse avec morceaux de poulet, tomates, oignons, champignons et pesto"
# Alla scampi, "Sauce crémeuse aux scampis frits, ail frais, basilic et pesto"
# Alla vegetaria, "Sauce tomate aux légumes frais, ail et basilic"
# Alla vongole, "Sauce au vin, persil, ail, oignons, tomate, pesto et basilic"
# Moussaka, "Sauce béchamel avec viande hachée assaisonnée, aubergines, pommes de terre et fromage"
# Lasagne, "Tranches de pâte avec sauce béchamel, viande hachée et fromage"
# Stifado,Morceaux d'agneau et échalotes dans une sauce épicée
# Youvetsi,Agneau avec des pâtes grecques dans une sauce tomate.
# Gyros, escalopes de porc avec tzatziki.
# Souvlaki, brochettes de viande avec gyros.
# Pollo ala banna,Morceaux de poulet avec poivron et champignons frits dans une sauce à la crème
# Scaloppa pizaioli,Veau avec sauce épicée
# Scaloppa al funghi,Veau et champignons sautés dans une sauce à la crème
# Souvlaki speciale,Porc avec poivron et champignons sautés dans une sauce au poivre
# La Cairo,Sarma et travers de porc
# Mina,Shawarma et poitrine de poulet
# Gerguis, "Armes, poulet et shaslick"
# Cyrille, "Shoarma, côtelette d'agneau et blanc de poulet"
# Corfou, "Côtelette d'agneau, souvlaki, steak et gyros"
# Agapi, "Souvlaki, blanc de poulet, steak et gyros"
# Rhodes mixtes, "Poitrine de poulet, côtes levées, côtelettes de porc et d'agneau"
# Pharao mix fish, "Saumon, crevettes et kalamari grillés (±30 min. de préparation)"
# Alexandros, "Blanc de poulet, souvlaki, filet de porc, steak et gyros"
# Rhodes mix, "Poitrine de poulet, spare ribs, côtelette de porc et d'agneau"
# Crète, "Poitrine de poulet, côtelette d'agneau, souvlaki, steak et gyros"
# Mélange de poissons Pharao, "Saumon, crevettes et kalamari grillés (± 30 min.)"
# Shoarma,
# Shoarma de poulet,
# Poitrine de poulet grillée,
# Shaslick,
# Côtelette d'agneau,
# Falafel (végétarien),
# Légumes supplémentaires (par variété), "Oignon, poivron, champignon"
# Nature,
# Doux - légèrement épicé,
# Noix de coco,
# Feu,
# Hawaï,
# Jack Daniels Honey, avec le vrai whisky Jack Daniels.
# Jack Daniels Smokey, avec le vrai whisky Jack Daniels
# Steak avec champignons frits,± 250 gr
# Bifteck de surlonge,± 250 gr
# T-bone de veau,± 350 gr
# Côte de boeuf,± 500 gr
# Côte de boeuf,± 250 gr
# Sauce crème aux champignons,
# Sauce crème au poivre,
# Pomodoro,Soupe de tomates fraîches
# Peperies,Elies poivrons grecs et olives
# Tzatziki, "Séré avec concombre, ail frais et fines herbes"
# Feta,Fromage de brebis original
# Sardeles,Poisson frit à l'ail frais
# Funghi trifolati,Champignons à l'ail frais dans une sauce à la crème
# Kalamaria, calamars avec sauce fraîche
# Gari des saganaki,Scampi frits avec une sauce tomate épicée.
# Feta saganaki, fromage feta frit.
# Pain avec beurre aux herbes,
# Scampi cream, "Dans une sauce à la crème avec de l'ail, du pesto et du basilic"
# Salade égyptienne, Salade mixte
# Salade de tomates, "Salade avec des tomates, de l'ail frais et des oignons"
# Salade grecque, Salade grecque originale avec du fromage feta
# Salade italienne, Tomate et mozzarella
# Salade de poulet, "Morceaux de poulet, salade, tomate, concombre et sauce au yaourt"
# Salade de thon, "Salade de thon
# Surf n Turf, "Scampi, bacon, tomate, concombre, croûtons et mayonnaise à la truffe"
# Entrée, "Choisissez entre: Salade de mozzarella avec noix et croûtons | Salade de filet de porc avec côtelettes de porc.
# Salade de porc avec vinaigrette à l'orange | Scampi à la crème avec basilic et croûtons
# Scampi à la crème au basilic et à l'ail "
# Plat principal, "Choisissez entre: Filet de porc à la crème de champignons | Entrecôte à la sauce au vin rouge
# Entrecôte à la sauce au vin rouge | Saumon avec tagliatelles à la crème
# Saumon avec tagliatelles à la crème"
# Dessert, "Choisissez entre: Tri de bavarois |
# Chocolat moelleux |
# Café/thé à la liqueur "
# Prix total,
# Vin rouge italien (Montepulciano d'abruzzo), "En plus d'une belle couleur rubis, il possède un nez intensément fruité. Agréablement sec et corsé, il se marie bien avec les viandes grillées, les pâtes et les fromages épicés."
# Vin rouge grec (Mavrodaphni de Patra), "Ce vin rouge doux a une belle couleur rubis foncé. La finale contient des arômes et des saveurs de raisins noirs et de prune. Le Mavrodaphni est également connu comme le porto grec. Ce vin rouge doux emmènera vos papilles en vacances en Grèce."
# Vin blanc grec (Tsantali retsina), "Vin retsina blanc et sec. Le nez est vif avec des arômes d'agrumes, de poire, de pomme et de résine de pin fraîche. La bouche est agréable, rafraîchissante et sèche, ce qui conduit à une finale saumâtre."
# Asti,
# Cava,
# Merlot,
# Chardonnay,
# Rosé,
# Limoncello,
# Ouzo,
# Porto rouge ~ blanc,
# Amaretto,
# Metaxa 5*,
# Komn Quat,
# Grappa,
# Sambucca,
# Cava,
# Pina colada,
# Whisky Williams,
# Chivas Regal,
# Whisky Cola (Williams),
# Baccardi Cola,
# Apéritif de la maison (cocktail),
# Sherry moyen ~ sec,
# Cuarenta y tres,
# Baileys,
# Martini rouge ~ blanc,
# Martini Royale ~ Bianco ~ Rosato,
# Gin Tonic,
# Campari,
# Campari orange,
# Café,
# Thé,
# Cappuccino,
# Café au lait,
# Chocolat chaud,
# Café Hasselt,
# Café au cognac,
# Café à l'amaretto,
# Café irlandais,
# Coca-Cola,
# Coca-Cola Light,
# Coca-Cola Zero,
# Fanta,
# Sprite,
# Spa bleu/rouge,
# "Looza, Looza apple, Looza Ace",
# Gini,
# Tonic,
# Ice Tea,
# Ice Tea Green,
# Schweppes agrum,
# "Lait chocolaté (froid), Fristi",
# Tonissteiner, "Corbeille de fruits, citron, orange"
# Redbull,Régulier/léger
# '''.splitlines()
# with open("csvfile.csv", "w") as file:
# 	for line in csv.reader(lines, quotechar='"', delimiter=',', quoting=csv.QUOTE_ALL, skipinitialspace=True):
# 		writer = csv.writer(file, delimiter=',')
# 		writer.writerow(line)
