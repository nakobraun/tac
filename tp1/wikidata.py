from datetime import datetime as dt
from SPARQLWrapper import SPARQLWrapper, JSON

# Retrieve results from SPARQL
endpoint = "https://query.wikidata.org/bigdata/namespace/wdq/sparql"
sparql = SPARQLWrapper(endpoint)

statement = """
SELECT DISTINCT ?item ?itemLabel WHERE {
    ?item p:P106 ?statement0.
    ?statement0 (ps:P106/(wdt:P279*)) wd:Q175151.
    ?item p:P27 ?statement1.
    ?statement1 (ps:P27/(wdt:P279*)) wd:Q31.
    SERVICE wikibase:label { bd:serviceParam wikibase:language "en" . }
}
ORDER BY ?itemLabel
"""

sparql.setQuery(statement)
sparql.setReturnFormat(JSON)
results = sparql.query().convert()

rows = results['results']['bindings']
print(f"\n{len(rows)} Imprimeur.euses belge\n")
# print(rows[:10])

for row in rows:
    print(row['itemLabel']['value'])
