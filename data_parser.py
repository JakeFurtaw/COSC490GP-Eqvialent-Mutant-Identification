import rdflib
import json
from globals import *
from Mutant import Mutant

g = rdflib.Graph()
g.parse("./dataset/dataset.ttl", format="turtle")
serialized_json = g.serialize(format='json-ld', indent=4)

# To see what the JSON object looks like:
# print(serialized_json)

# Convert JSON to a Python dictionary
json_dict = json.loads(serialized_json)

# Getting information from the dictionary
for element in json_dict:
    mutant = Mutant()
    if program_key in element:
        program = element[program_key][0].get('@id')
        program_cleaned = program.replace("mb:program#", "")
        mutant.program = program_cleaned
        print(f"PROGRAM: {mutant.program}")
    else:
        print("Program key not found")

    if operator_key in element:
        operator = element[operator_key][0]['@id']
        operator_cleaned = operator.replace("mb:operator#", "")
        mutant.operator = operator_cleaned
        print(f"OPERATOR: {mutant.operator}")
    else:
        print("Operator key not found")

    if equivalence_key in element:
        equivalence = element[equivalence_key][0].get('@value')
        mutant.equivalence = equivalence
        print(f"EQUIVALENCE: {equivalence}")
    else:
        print("Equivalence key not found")

    id_val = element.get('@id')
    if id_val:
        id_val_cleaned = id_val.replace("mb:mutant#", "")
        mutant.id = id_val_cleaned
        print(f"ID: {mutant.id}")
    else:
        print("ID key not found")

    if difference_key in element:
        difference = element[difference_key][0].get('@value')
        mutant.difference = difference
        print(f"DIFFERENCE: {mutant.difference}")
    else:
        print("Difference key not found")
    