

#  Chaînes de Caractères (str) 
print("\n--- 1.1 Chaînes de Caractères (str) ---")

message = "Bonjour LangChain et le monde de l'IA !"
print(f"Chaîne originale : {message}")

# Concaténation
nom = "Alice"
salutation = "Salut " + nom + "!"
print(f"Concaténation : {salutation}")

# Méthodes utiles
phrase_salle = "   Bonjour le monde !   "
print(f"Chaîne avec espaces : '{phrase_salle}'")
print(f"Après strip() : '{phrase_salle.strip()}'") # Supprime les espaces blancs au début et à la fin

mots = message.split(" ") # Divise la chaîne par les espaces
print(f"Après split() : {mots}")

nouvelle_phrase = "-".join(mots) # Joint les éléments d'une liste avec un séparateur
print(f"Après join() : {nouvelle_phrase}")

texte_remplace = message.replace("monde", "univers") # Remplace une sous-chaîne
print(f"Après replace() : {texte_remplace}")

# Très important pour les prompts : f-strings
# Elles permettent d'intégrer des expressions Python directement dans des chaînes.
# C'est la méthode moderne et recommandée.

modele_nom = "GPT-4"
temperature = 0.7

prompt_exemple = f"Quel est le rôle de {modele_nom} en IA ? Réponds avec une température de {temperature}."
print(f"\nExemple de f-string pour un prompt : {prompt_exemple}")

# 
a = 10
b = 5
calcul = f"La somme de {a} et {b} est {a + b}."
print(f"Calcul dans f-string : {calcul}")



#################################################################################################

# 1.2 Nombres (int, float)
print("\n--- 1.2 Nombres (int, float) ---")

nombre_entier = 10
nombre_flottant = 3.14
print(f"Entier : {nombre_entier}, Flottant : {nombre_flottant}")

# Opérations arithmétiques
somme = nombre_entier + 5
difference = nombre_flottant - 1.0
produit = nombre_entier * nombre_flottant
division = nombre_entier / 3 
division_entiere = nombre_entier // 3 
modulo = nombre_entier % 3 
puissance = 2 ** 3 #

print(f"Somme : {somme}")
print(f"Différence : {difference}")
print(f"Produit : {produit}")
print(f"Division : {division}")
print(f"Division entière : {division_entiere}")
print(f"Modulo : {modulo}")
print(f"Puissance : {puissance}")

###########################################################################################################



# 1.3 Listes (list)
print("\n--- 1.3 Listes (list) ---")

liste_fruits = ["pomme", "banane", "cerise"]
print(f"Liste originale : {liste_fruits}")

# Accès par index (commence à 0)
print(f"Premier fruit : {liste_fruits[0]}")
print(f"Dernier fruit : {liste_fruits[-1]}") # Accès depuis la fin

# Slicing (extraction de sous-listes)
print(f"Sous-liste (index 0 à 1) : {liste_fruits[0:2]}") # [0, 2[
print(f"Tous sauf le premier : {liste_fruits[1:]}")
print(f"Tous sauf le dernier : {liste_fruits[:-1]}")

# Modification
liste_fruits[1] = "orange"
print(f"Liste après modification : {liste_fruits}")

# Ajout d'éléments
liste_fruits.append("kiwi") # Ajoute à la fin
print(f"Après append() : {liste_fruits}")

liste_fruits.insert(1, "raisin") # Insère à un index spécifique
print(f"Après insert() : {liste_fruits}")

# Suppression d'éléments
liste_fruits.remove("pomme") # Supprime la première occurrence de la valeur
print(f"Après remove('pomme') : {liste_fruits}")

element_supprime = liste_fruits.pop() # Supprime et retourne le dernier élément
print(f"Après pop() (supprimé : {element_supprime}) : {liste_fruits}")

# Longueur de la liste
print(f"Longueur de la liste : {len(liste_fruits)}")

# Vérifier la présence
if "orange" in liste_fruits:
    print("L'orange est dans la liste !")

# Itération
print("Itération sur la liste :")
for fruit in liste_fruits:
    print(f"- {fruit}")

# Itération avec index (utile pour parfois manipuler l'élément et son index)
print("Itération avec index :")
for index, fruit in enumerate(liste_fruits):
    print(f"{index}: {fruit}")



#####################################################################################################

# --- 1.4 Dictionnaires (dict) ---
print("\n--- 1.4 Dictionnaires (dict) ---")

# Création d'un dictionnaire
personne = {
    "nom": "Dupont",
    "prenom": "Jean",
    "age": 30,
    "ville": "Paris"
}
print(f"Dictionnaire original : {personne}")

# Accès aux valeurs par clé
print(f"Nom : {personne['nom']}")
print(f"Âge : {personne['age']}")

# Modification d'une valeur
personne["age"] = 31
print(f"Âge mis à jour : {personne['age']}")

# Ajout d'une nouvelle paire clé-valeur
personne["profession"] = "Développeur IA"
print(f"Après ajout : {personne}")

# Suppression d'une paire clé-valeur
del personne["ville"]
print(f"Après suppression de 'ville' : {personne}")

# Vérifier la présence d'une clé
if "prenom" in personne:
    print("La clé 'prenom' existe.")

# Obtenir toutes les clés, toutes les valeurs, toutes les paires
print(f"Clés : {personne.keys()}")
print(f"Valeurs : {personne.values()}")
print(f"Paires (items) : {personne.items()}")

# Itération sur les dictionnaires
print("Itération sur les clés :")
for cle in personne.keys(): # Ou simplement for cle in personne:
    print(f"- {cle}")

print("Itération sur les valeurs :")
for valeur in personne.values():
    print(f"- {valeur}")

print("Itération sur les paires clé-valeur :")
for cle, valeur in personne.items():
    print(f"- {cle}: {valeur}")

# Accès sécurisé avec .get()
# Retourne None si la clé n'existe pas, ou une valeur par défaut spécifiée
email = personne.get("email", "N/A")
print(f"Email (via .get()) : {email}")



#####################################################################################################

# 1.5 Tuples (tuple) et Sets (set)
print("\n--- 1.5 Tuples (tuple) ---")

# Tuple : collection ordonnée et IMMUABLE (non modifiable)
coordonnees = (10.0, 20.5)
print(f"Tuple de coordonnées : {coordonnees}")
print(f"X : {coordonnees[0]}, Y : {coordonnees[1]}")

# coordonnees[0] = 11.0 # Ceci provoquerait une erreur ! Un tuple est immuable.

print("\n--- 1.5 Sets (set) ---")
# Set : collection NON ORDONNÉE d'éléments UNIQUES
couleurs = {"rouge", "vert", "bleu", "rouge"} # 'rouge' en double sera ignoré
print(f"Set de couleurs : {couleurs}")

couleurs.add("jaune")
print(f"Après add('jaune') : {couleurs}")

couleurs.remove("vert")
print(f"Après remove('vert') : {couleurs}")

# Opérations sur les sets (union, intersection, différence)
set_a = {1, 2, 3}
set_b = {3, 4, 5}
print(f"Union de A et B : {set_a.union(set_b)}")
print(f"Intersection de A et B : {set_a.intersection(set_b)}")