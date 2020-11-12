# WADE-HACKATON


To use the application, run __init__.py. 

What we have done: 

1. Parser for xlsx, Parser returns a tuple (names, parsed_sheets) where names are sheets names and parsed_sheets are, as name says, parsed sheets. 
A parsed sheet is an array of rows, where each row is a dict with keys being column names.

2. An unsuccessful attempt of creating a fully rdf model from excel file. 
  The created graph contains only university and some attributes. 

Example: 


```
[] a foaf:Organization ;
    rdf:ID "PA04"^^xsd:string ;
    ns1:atLocation "CLUJ-NAPOCA"^^xsd:string ;
    foaf:homepage "http://www.sapientia.ro/ro/facultati/cluj-napoca"^^xsd:string ;
    foaf:name "Universitatea \"Sapientia\" din Cluj-Napoca"^^xsd:string .
```
Ninicu Cristian\
*parser\
*rdf implementation

Maftei Claudiu Ioan\
*rdf research\
*schema\
*shacl\
*queries
