# Automatic Equivalent Mutant Identification

**data_parser.py**
- Coverts .ttl (turtle format) dataset into JSON Object (Using rdflib library)
- Converts JSON object into Python dictionary using the built-in json library
- Iterates for each element (mutant) in the dictionary (dataset)
- Extracts data like program name, equivalence, mutant operator, and difference into a Mutant object

# Dataset used 
- https://b2share.eudat.eu/records/fd8e674385214fe9a327941525c31f53

# Libraries
```
https://pytorch.org/
https://pandas.pydata.org/
https://github.com/eliben/pycparser
https://pypi.org/project/javalang/
https://pypi.org/project/gensim/
https://scikit-learn.org/stable/
```
