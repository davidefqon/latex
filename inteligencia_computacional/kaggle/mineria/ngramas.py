import nltk
from textblob import TextBlob
nltk.download('punkt')
# nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
ndltk.download('words')

# Texto de ejemplo para analizar
texto = """
Apple is expected to release a new iPhone next month. Tim Cook, the CEO of Apple, announced it during a conference in San Francisco.
The new phone is rumored to have a faster processor and an improved camera.
Investors are excited about the new release, with Apple's stock price increasing by 3% after the announcement.
"""

# Tokenizar el texto
palabras = nltk.word_tokenize(texto)

# Analizar sentimientos
blob = TextBlob(texto)
sentimiento = blob.sentiment.polarity
subjetividad = blob.sentiment.subjectivity

# Etiquetar partes del discurso
etiquetas = nltk.pos_tag(palabras)

# ExtracciÃ³n de entidades nombradas
entidades = nltk.ne_chunk(etiquetas)

# Detectar n-gramas
bigramas = list(nltk.bigrams(palabras))
trigramas = list(nltk.trigrams(palabras))

# Resultados
print("AnÃ¡lisis de Sentimientos:")
print(f"Polaridad: {sentimiento}, Subjetividad: {subjetividad}")

print("\nEtiquetas POS:")
for palabra, etiqueta in etiquetas:
    print(f"{palabra}: {etiqueta}")

print("\nEntidades Nombradas:")
for subtree in entidades.subtrees():
    if subtree.label() in ['PERSON', 'ORGANIZATION', 'GPE']:  # Tipos de entidades nombradas
        entidad = " ".join([leaf[0] for leaf in subtree.leaves()])
        print(f"{entidad}: {subtree.label()}")

print("\nBigramas:")
print([" ".join(bigrama) for bigrama in bigramas])

print("\nTrigramas:")
print([" ".join(trigrama) for trigrama in trigramas])