from collections import defaultdict
import sys
import spacy
from spacy.lang.fr.examples import sentences

nlp = spacy.load('fr_core_news_md')

# Charger le texte
n=900000
text = open("../data/tmp/1902_clean.txt", encoding='utf-8').read()[:n]

# Traiter le texte
doc = nlp(text)

# Compter les entités
people = defaultdict(int)
for ent in doc.ents:
    if ent.label_ == "PER" and len(ent.text) > 3:
        people[ent.text] += 1

print("Personnes :")
# Trier et imprimer
sorted_people = sorted(people.items(), key=lambda kv: kv[1], reverse=True)

for person, freq in sorted_people[:50]:
    print(f"{person} apparait {freq} fois dans le corpus")

# Compter les entités
organisation = defaultdict(int)
for ent in doc.ents:
    if ent.label_ == "ORG" and len(ent.text) > 3:
        organisation[ent.text] += 1

print("Organisations :")
# Trier et imprimer
sorted_organisation = sorted(organisation.items(), key=lambda kv: kv[1], reverse=True)

for organisation, freq in sorted_organisation[:50]:
    print(f"{organisation} apparait {freq} fois dans le corpus")

# Compter les entités
lieux = defaultdict(int)
for ent in doc.ents:
    if ent.label_ == "LOC" and len(ent.text) > 3:
        lieux[ent.text] += 1

print("Lieux :")
# Trier et imprimer
sorted_lieux = sorted(lieux.items(), key=lambda kv: kv[1], reverse=True)

for lieux, freq in sorted_lieux[:50]:
    print(f"{lieux} apparait {freq} fois dans le corpus")
