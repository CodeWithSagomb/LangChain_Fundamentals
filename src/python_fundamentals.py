

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


###############################################################################################################


# 2.1 Conditions (if, elif, else)
print("\n--- 2.1 Conditions (if, elif, else) ---")

age = 18
if age < 18:
    print("Vous êtes mineur.")
elif age == 18:
    print("Vous avez exactement 18 ans.")
else:
    print("Vous êtes majeur.")

# Opérateurs logiques : and, or, not
temperature_eau = 95
if temperature_eau > 0 and temperature_eau < 100:
    print("L'eau est liquide (entre 0 et 100 degrés Celsius).")
elif temperature_eau >= 100:
    print("L'eau est gazeuse ou bout.")
else:
    print("L'eau est solide (gelée).")

# Exemple de condition simple pour la validation d'entrée
user_input = "Hello"
if user_input: # Une chaîne non vide est True
    print(f"L'entrée utilisateur est : {user_input}")
else:
    print("L'entrée utilisateur est vide.")

# Vérifier si un dictionnaire est vide
parametres_llm = {"temperature": 0.7, "max_tokens": 100}
# parametres_llm = {} # Décommenter pour tester un dictionnaire vide
if parametres_llm:
    print("Le dictionnaire de paramètres n'est pas vide.")
else:
    print("Le dictionnaire de paramètres est vide.")

##########################################################################################

# src/python_fundamentals.py (ajoutez à la suite)

# 2.2 Boucles (for, while)
print("\n--- 2.2 Boucles (for, while) ---")

# Boucle for : pour itérer sur des collections (listes, tuples, chaînes, dictionnaires)
fruits_disponibles = ["mangue", "ananas", "papaye"]
print("Itération sur les fruits :")
for fruit in fruits_disponibles:
    print(f"J'aime manger des {fruit}.")

# Boucle for avec range() : pour itérer un nombre fixe de fois
print("Compter de 0 à 4 :")
for i in range(5): # Génère une séquence de 0, 1, 2, 3, 4
    print(i)

print("Compter de 2 à 8 (pas de 2) :")
for i in range(2, 9, 2): # Début, fin (exclue), pas
    print(i)

# Itération sur les éléments d'un dictionnaire (vu précédemment, mais important de le rappeler)
llm_config = {"model": "falcon-7b", "temperature": 0.5, "max_new_tokens": 200}
print("Paramètres du LLM :")
for key, value in llm_config.items():
    print(f"- {key}: {value}")

# Boucle while : tant qu'une condition est vraie
compteur = 0
print("Compteur while :")
while compteur < 3:
    print(f"Compteur : {compteur}")
    compteur += 1 # Incrémente le compteur

# break et continue
print("Exemple de break et continue :")
for num in range(10):
    if num == 3:
        continue # Passe à l'itération suivante (saute l'affichage de 3)
    if num == 7:
        break # Arrête complètement la boucle
    print(num)



#########################################################################################################


# 3. Fonctions
print("\n--- 3. Fonctions ---")

# Définition de fonction simple
def saluer(nom):
    """Affiche un message de salutation."""
    print(f"Bonjour, {nom} !")

saluer("Marie")
saluer("Pierre")

# Fonction avec valeur de retour
def additionner(a, b):
    """Retourne la somme de deux nombres."""
    return a + b

resultat_addition = additionner(10, 5)
print(f"10 + 5 = {resultat_addition}")
print(f"3 + 7 = {additionner(3, 7)}")

# Arguments par défaut
def afficher_info_llm(modele="GPT-3.5", temperature=0.7):
    """Affiche les informations d'un modèle LLM avec des valeurs par défaut."""
    print(f"Modèle : {modele}, Température : {temperature}")

afficher_info_llm() # Utilise les valeurs par défaut
afficher_info_llm("Llama2") # Surcharge le modèle, utilise la température par défaut
afficher_info_llm("Mistral", 0.9) # Surcharge les deux

# Arguments nommés (Keyword Arguments - kwargs)
# Rend l'appel de fonction plus lisible
afficher_info_llm(temperature=0.8, modele="Falcon")

# *args et **kwargs (Arguments positionnels et nommés arbitraires)
# Très utile pour des fonctions qui peuvent accepter un nombre variable d'arguments.
# Vous le verrez souvent dans les APIs de bibliothèques comme LangChain ou Transformers.

def traiter_parametres(*args, **kwargs):
    """
    Traite un nombre arbitraire d'arguments positionnels (*args)
    et d'arguments nommés (**kwargs).
    """
    print("\nArguments positionnels (*args) :")
    for arg in args:
        print(f"- {arg}")

    print("Arguments nommés (**kwargs) :")
    for key, value in kwargs.items():
        print(f"- {key}: {value}")

traiter_parametres("doc1.txt", "doc2.pdf", modele="OpenAI", version="latest", streaming=True)
traiter_parametres(1, 2, 3, nom="Alice", age=25, ville="New York")