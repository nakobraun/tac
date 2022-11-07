import os
import yake

# Instantier l'extracteur de mots clés
kw_extractor = yake.KeywordExtractor(lan="fr", top=50)

# Lister les Fichiers
data_path = "../data/txt/"
files = os.listdir(data_path)

# Récupérer les fichiers selon une date précise
date = '1902';
file_date = []
for file in files:
    file_split = file.split('-')
    file_splite = file_split[0].split('_')
    file_annee = file_splite[-1]
    if date in file_annee:
        file_date.append(file)
# print(file_date[:15])

# Récupérer le texte des fichiers
motsclefs = []
for file_d in file_date:
    text = open(os.path.join(data_path, file_d), 'r').read()
    # Extraire les mots clés de ces textes
    keywords = kw_extractor.extract_keywords(text)
    for words in keywords:
        word = words[0]
        motsclefs.append(word)

print(f"\nLe nombre de mots clefs : {len(motsclefs)}")
print(f"\nles 200 premiers mots clefs : {motsclefs[:100]}")
