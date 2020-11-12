from enum import Enum

from rdflib import BNode, Graph, Literal
import rdflib.namespace

from Parser import Parser

class PTypes(Enum):
    NAME = rdflib.namespace.FOAF.name
    WEB_PAGE = rdflib.namespace.FOAF.homepage
    TYPE = rdflib.namespace.RDF.type
    AT_LOCATION = rdflib.namespace.PROV.atLocation
    ID = rdflib.namespace.RDF.ID
    RELATED_TO = rdflib.namespace.SKOS.related

parser = Parser()
parser.parse("invatamant-superior-2020.xlsx")

graph = Graph()
graph.bind("foaf", rdflib.namespace.FOAF)

names, parsed = parser.get_parsed()
# print(names)
# print(parsed[names[0]][0])

UNI_RULES = [("Nume", PTypes.NAME), (PTypes.TYPE, rdflib.namespace.FOAF.Organization), ("Adresa web", PTypes.WEB_PAGE), ("Localitate", PTypes.AT_LOCATION), ("Cod Universitate", PTypes.ID)]
# FAC_RULES = [("Nume", PTypes.NAME), (PTypes.TYPE, rdflib.namespace.PROV.Entity), ("Nume", PTypes.RELATED_TO, "Universitate")]

allRules = [UNI_RULES]

universities = len(parsed[names[0]])
nodes = [None] * universities


for set_rls in allRules:
    curr = set_rls
    for rule in curr:
        for item in range(0, universities):
            if not nodes[item]:
                nodes[item] = BNode();

            for key in parsed[names[0]][item].keys():
                if key == rule[0]:
                    p = rule[1]
                    o = Literal(parsed[names[0]][item][key][0], datatype=rdflib.namespace.XSD.string)
                    graph.add((nodes[item], p.value, o))
                elif rule[0] not in parsed[names[0]][item].keys() and rule[1] not in parsed[names[0]][item].keys():
                    graph.add((nodes[item], rule[0].value, rule[1]))
                # elif len(rule) == 3:
                #     graph.add((rule[0], rule[1].value, rule[2]))



print(graph.serialize(format="turtle").decode("utf-8"))
