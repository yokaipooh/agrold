from SPARQLWrapper import SPARQLWrapper, JSON

sparql = SPARQLWrapper("http://agrold.southgreen.fr/sparql")
sparql.setQuery("""
    PREFIX uri:<http://www.southgreen.fr/agrold/resource/Zm00001d042213>
    PREFIX agrold:<http://www.southgreen.fr/agrold/vocabulary/>
SELECT ?property  ?hasValue ?isValueOf
WHERE {
  { uri: ?property ?hasValue }
  UNION
  { ?isValueOf ?property uri:}
}
""")
sparql.setReturnFormat(JSON)
results = sparql.query().convert()

for result in results["results"]["bindings"]:
    print(result["property"], result["hasValue"])



