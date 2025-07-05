# src/huggingface_basics.py
from transformers import pipeline

print("--- 3.3 Utilisation du pipeline pour des Tâches NLP Courantes ---")

# --- Tâche 1 : Génération de Texte (Text Generation) ---
# Utilisez un modèle léger pour la démo, comme 'distilgpt2'
print("\n--- Génération de Texte ---")
try:
    generator = pipeline("text-generation", model="distilgpt2")
    # Le modèle 'distilgpt2' est un modèle plus petit et plus rapide que GPT-2 complet.
    # Il peut être téléchargé localement ou utilisé directement s'il est déjà en cache.

    # Générer du texte à partir d'un prompt
    prompt = "Dans un futur proche, l'intelligence artificielle"
    generated_text = generator(prompt, max_new_tokens=50, num_return_sequences=1)
    # max_new_tokens: limite la longueur du texte généré
    # num_return_sequences: nombre de séquences différentes à générer pour le même prompt

    print(f"Prompt : '{prompt}'")
    print(f"Texte généré : '{generated_text[0]['generated_text']}'")

    # Exemple avec un autre modèle plus grand si vous voulez tester (peut être lent sans GPU)
    # gpt2_generator = pipeline("text-generation", model="gpt2")
    # generated_text_gpt2 = gpt2_generator(prompt, max_new_tokens=50, num_return_sequences=1)
    # print(f"Texte généré par GPT2 : '{generated_text_gpt2[0]['generated_text']}'")

except Exception as e:
    print(f"Erreur lors de la génération de texte : {e}")
    print("Assurez-vous d'avoir suffisamment de RAM/GPU ou utilisez un modèle plus petit.")
    print("Essayez 'pip install accelerate' et 'pip install bitsandbytes' pour l'optimisation GPU si disponible.")


# --- Tâche 2 : Analyse de Sentiment (Sentiment Analysis) ---
# Utilise 'distilbert-base-uncased-finetuned-sst-2-english' par défaut, un modèle de classification.
print("\n--- Analyse de Sentiment ---")
classifier = pipeline("sentiment-analysis")
texts = [
    "J'adore ce film, il est absolument génial !",
    "Ceci est un produit médiocre.",
    "Le temps aujourd'hui est neutre."
]
results = classifier(texts)
for text, result in zip(texts, results):
    print(f"Texte : '{text}'")
    print(f"Sentiment : {result['label']} (Score : {result['score']:.2f})")


# --- Tâche 3 : Question-Réponse (Question Answering) ---
# Modèle par défaut est 'distilbert-base-uncased-distilled-squad', bon pour l'extraction de réponse.
print("\n--- Question-Réponse ---")
qa_pipeline = pipeline("question-answering")
context = "Le Machine Learning est un sous-domaine de l'intelligence artificielle qui permet aux systèmes d'apprendre à partir de données sans être explicitement programmés. Les algorithmes de ML identifient des motifs dans les données et utilisent ces motifs pour faire des prédictions ou prendre des décisions."
question = "Qu'est-ce que le Machine Learning ?"

answer = qa_pipeline(question=question, context=context)
print(f"Contexte : '{context}'")
print(f"Question : '{question}'")
print(f"Réponse : '{answer['answer']}' (Score : {answer['score']:.2f})")


# --- Tâche 4 : Résumé (Summarization) ---
# Utilise 'sshleifer/distilbart-cnn-12-6' par défaut.
print("\n--- Résumé ---")
summarizer = pipeline("summarization")
long_text = """
LangChain est un framework open-source qui vise à simplifier le développement d'applications basées sur les grands modèles linguistiques (LLM). Il fournit des outils, des composants et des interfaces pour créer des applications d'IA plus sophistiquées, qui vont au-delà de la simple invocation d'un LLM. Les fonctionnalités clés de LangChain incluent la connexion des LLM à des sources de données externes, l'ajout de mémoire à des conversations, et l'intégration avec d'autres outils comme des moteurs de recherche ou des bases de données. Il permet aux développeurs de chaîner plusieurs appels de LLM ensemble ou de combiner des LLM avec d'autres étapes pour des workflows complexes.
"""
summary = summarizer(long_text, max_length=60, min_length=30, do_sample=False)
# max_length, min_length: définissent la taille du résumé
# do_sample=False: pour une sortie plus déterministe (pas de génération créative)

print(f"Texte original (extrait) : '{long_text[:100]}...'")
print(f"Résumé : '{summary[0]['summary_text']}'")


# --- Tâche 5 : Traduction (Translation) ---
# Utilisez un modèle spécifique pour la traduction, par exemple pour le français vers l'anglais.
print("\n--- Traduction (Français vers Anglais) ---")
try:
    # Modèle plus léger pour la démo
    translator = pipeline("translation", model="Helsinki-NLP/opus-mt-fr-en")
    french_text = "Bonjour le monde, comment allez-vous aujourd'hui ?"
    english_translation = translator(french_text)
    print(f"Texte français : '{french_text}'")
    print(f"Traduction anglaise : '{english_translation[0]['translation_text']}'")
except Exception as e:
    print(f"Erreur lors de la traduction : {e}")
    print("Le téléchargement du modèle de traduction peut prendre du temps. Vérifiez votre connexion.")


print("\nFin des exemples Hugging Face.")