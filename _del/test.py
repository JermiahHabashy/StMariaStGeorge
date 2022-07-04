import csv
import pandas as pd

lines = '''Kids spaghetti,(± 30 min. prep time)
Grilled chicken breast,
Bitterballs,
Frikandel,
Gyros,
Spareribs,
Pizza bambino,With a children's ice cream as dessert
Gelato bambino,Children's ice cream
Banana Royal,”Vanilla cream ice with banana, chocolate and whipped cream”
Dame blanche,Vanilla ice cream with chocolate and whipped cream
Greek yogurt with honey and walnuts,
Chocolate moelleux with vanilla ice cream,
Margharita,Tomato and cheese
Cipola, "Tomato, cheese and onions"
Salami, "Tomato, cheese and salami"
Proscuito, "Tomato, cheese and ham"
Funghi, "Tomato, cheese and mushrooms"
Proscuito & Funghi, "Tomato, cheese, ham and mushrooms"
Capriccosa, "Tomato, cheese, salami and mushrooms"
Americana, "Tomato, cheese, salami and ham"
Peperoni, "Tomato, cheese, bell pepper and chili peppers"
Napolitana, "Tomato, cheese, anchovies and olives"
Hawaii, "Tomato, cheese, pineapple and ham"
Siciliana, "Tomato, cheese, artichokes, bell pepper and olives"
Tonno, "Tomato, cheese, tuna and onions"
Bolognaise, "Tomato, cheese, minced meat and onions"
Bella italia, "Tomato, cheese, minced meat and egg"
Boromea, "Tomato, cheese, ham, mushrooms and egg"
Vegetaria, "Tomato, cheese, bell pepper, mushrooms, artichokes, olives and onions"
Calzone, "Dense folded pizza with tomato, cheese, mushrooms, artichokes, minced meat and ham"
Shoarma, "Tomato, cheese, shoarma, bell pepper and onions"
Quattro stagioni, "Tomato, cheese, peppers, mushrooms, ham and salami"
Lucky luciano, "Tomato, cheese, mushrooms, onions, bacon and egg"
Maffiosa, "Tomato, cheese, mushrooms, bell pepper, onions and bacon"
Pollo, "Tomato, cheese, chicken shawarma, mushrooms and onions"
O Solo Mio, "Tomato, cheese, mushrooms, artichokes, bell pepper, onions, ham and eggs"
Marinara, "Tomato, cheese, seafood and anchovies"
Quattro formagi,Tomato with 4 italian cheeses
Pizza Scampi, "Tomato, cheese and scampi"
Pizza Gerguis,Specialty of the house
Extra meat,
Extra vegetables per type,
Extra arugula,
Kalamaria, squid with fresh sauce
Solomos,Stewed salmon from the grill with lemon and dill sauce (+30 min. prep time)
Media saganaki, mussels with fresh tomatoes in a spicy sauce
Fritto misto,Different kinds of fried fish
Gerides saganaki,Fried prawns in a spicy sauce
Scampi griglia,Grilled king prawns
Alla napolitan,Tomato sauce
Alla funghi,Tomato sauce with mushrooms
Alla bolognaise,Tomato sauce with minced meat
Alla carbonara, "Creamy sauce with cheese, ham"
Santa Maria,Wine sauce with garlic and basil
Alla marinara,Tomato sauce with seafood
Quattro formagio, Cream sauce with 4 kinds of cheese
Alla polio, "Creamy sauce with pieces of chicken, tomato, onion, mushroom and pesto"
Alla scampi, "Cream sauce with fried scampi, fresh garlic, basil and pesto"
Alla vegetaria, "Tomato sauce with fresh vegetables, garlic and basil"
Alla vongole, "Wine sauce, parsley, garlic, onions, tomato, pesto and basil"
Moussaka, "Béchamel sauce with seasoned minced meat, eggplants, potatoes and cheese"
Lasagna, "Slices of dough with bechamel sauce, minced meat and cheese"
Stifado,Pieces of lamb and shallots in a spicy sauce
Youvetsi,Lamb with Greek pasta in a tomato sauce.
Gyros,Pork cutlets with tzatziki.
Souvlaki, skewered meat with gyros
Pollo ala banna,Chicken pieces with bell pepper and fried mushrooms in cream sauce
Scaloppa pizaioli,Veal with spicy sauce
Scaloppa al funghi,Veal and sautéed mushrooms in cream sauce
Souvlaki speciale,Pork with bell pepper and fried mushrooms in pepper sauce
La Cairo,Sarma and ribs
Mina,Shawarma and chicken breast
Gerguis, "Arms, chicken and shaslick"
Cyril, "Shoarma, lamb chop and chicken breast"
Corfu, "Lamb cutlet, souvlaki, steak and gyros"
Agapi, "Souvlaki, chicken breast, steak and gyros"
Rhodes mix, "Chicken breast, spareribs, pork and lamb chops"
Pharao mixed fish, "Grilled salmon, prawns and kalamari (±30 min. prep time)"
Alexandros, "Chicken breast, souvlaki, pork tenderloin, steak and gyros"
Rhodes mix, "Chicken breast, spare ribs, pork and lamb chop"
Crete, "Chicken breast, lamb chop, souvlaki, steak and gyros"
Pharao mixed fish, "Grilled salmon, prawns and kalamari (± 30 min.)"
Shoarma,
Chicken shoarma,
Chicken breast from the grill,
Shaslick,
Lamb chop,
Falafel (vegetarian),
Extra vegetables (per variety), "Onion, bell pepper, mushroom"
Nature,
Sweet - slightly spicy,
Coconut,
Fire,
Hawai,
Jack Daniels Honey, with the real Jack Daniels whiskey
Jack Daniels Smokey, with the genuine Jack Daniels whiskey
Steak with fried mushroom,± 250 gr
Sirloin steak,± 250 gr
Veal T-bone,± 350 gr
Beef T-bone,± 500 gr
Rib eye,± 250 gr
Mushroom Cream Sauce,
Pepper Cream Sauce,
Pomodoro,Fresh tomato soup
Peperies,Elies Greek peppers and olives
Tzatziki, "Quark with cucumber, fresh garlic and herbs"
Feta cheese,Original sheep cheese
Sardeles,Fried fish with fresh garlic
Funghi trifolati,Fresh garlic mushrooms in cream sauce
Kalamaria, squid with fresh sauce
Gari des saganaki,Fried scampi with spicy tomato sauce.
Feta saganaki,Fried feta cheese
Bread with herb butter,
Scampi cream, "In cream sauce with garlic, pesto & basil"
Egyptian salad,Mixed salad
Tomato salad, "Salad with tomatoes, fresh garlic and onions"
Greek salad,Original greek salad with feta cheese
Italian salad, Tomato and mozzarella
Chicken salad, "Chicken pieces, salad, tomato, cucumber and yogurt dressing"
Tonno salad,Tuna salad
Surf n Turf, "Scampi, bacon, tomato, cucumber, crouttons and truffle mayonnaise"
Appetizer, "Choose between: Mozzarella salad with walnuts and croutons | Pork tenderloin salad with pork chops 
Salad of pork with orange dressing | Scampi in cream sauce with basil and croutons 
Scampi in cream sauce with basil and garlic"
Main course, "Choose between: Pork tenderloin with mushroom cream sauce | Entrecote with red wine sauce 
Sirloin steak with red wine sauce | Salmon with tagliatelle in cream sauce 
Salmon with tagliatelle in cream sauce"
Dessert, "Choose between: Tri of bavarois | 
Chocolate moelleux | 
Coffee/tea with liqueur"
Total price,
ltalian red wine (Montepulciano d'abruzzo), "In addition to a beautiful ruby color, it possesses an intensely fruity nose. Pleasantly dry and full-bodied, it goes well with grilled meats, pastas and spicy cheeses."
Greek Red Wine (Mavrodaphni of Patra), "This sweet, red wine has a beautiful dark ruby color. The finish contains aromas and flavors of black raisins and plum. Mavrodaphni is also known as the Greek port. This red sweet wine will take your taste buds on a vacation to Greece."
Greek White Wine (Tsantali retsina), "Dry, white retsina wine. The nose is lively with aromas of citrus, pear, apple and fresh pine resin. Nice and refreshing and dry on the palate, which leads to a briny finish."
Asti,
Cava,
Merlot,
Chardonnay,
Rosé,
Limoncello,
Ouzo,
Porto red ~ white,
Amaretto,
Metaxa 5*,
Komn Quat,
Grappa,
Sambucca,
Cava,
Pina colada,
Whisky Williams,
Chivas Regal,
Whisky Cola (Williams),
Baccardi Cola,
Aperitif of the house (cocktail),
Sherry medium ~ dry,
Cuarenta y tres,
Baileys,
Martini red ~ white,
Martini Royale ~ Bianco ~ Rosato,
Gin Tonic,
Campari,
Campari orange,
Coffee,
Tea,
Cappuccino,
Cafe au lait,
Hot chocolate,
Hasselt coffee,
Coffee with cognac,
Coffee with amaretto,
Irish coffee,
Coca-Cola,
Coca-Cola Light,
Coca-Cola Zero,
Fanta,
Sprite,
Spa blue/red,
"Looza, Looza apple, Looza Ace",
Gini,
Tonic,
Ice Tea,
Ice Tea Green,
Schweppes agrum,
"Choco milk (cold), Fristi",
Tonissteiner, "Fruit basket, lemon, orange"
Redbull,Regular/light'''.splitlines()
with open("csvfile.csv", "w") as file:
	for line in csv.reader(lines, quotechar='"', delimiter=',', quoting=csv.QUOTE_ALL, skipinitialspace=True):
		writer = csv.writer(file, delimiter=',')
		writer.writerow(line)
