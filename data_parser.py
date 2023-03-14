import rdflib
import json
from globals import *
from mutant import Mutant
from diff_parser import UnifiedDiffParser
from convert_to_ast import convert_java, convert_c

g = rdflib.Graph()
g.parse("./dataset/dataset.ttl", format="turtle")
serialized_json = g.serialize(format='json-ld', indent=4)

# To see what the JSON object looks like:
#print(serialized_json)

# Convert JSON to a Python dictionary
json_dict = json.loads(serialized_json)
print(f"DATASET SIZE: {len(json_dict)}\n") 

num_parsed = 0
num_ignored = 0
num_equiv = 0
num_non_equiv = 0
num_java_mutants = 0
num_c_mutants = 0

# Getting information from the dictionary
for element in json_dict:
    # Some elements in the dataset represent the authors and other information that is not the mutant
    if any(key in element for key in keys_to_ignore) or difference_key not in element:
        num_ignored += 1
        continue
    # For testing purpose, we will only test the first few mutants
    if num_parsed == 10:
        break
    mutant = Mutant()

    if difference_key in element:
        difference = element[difference_key][0].get('@value')
        mutant.difference = difference
        print(f"DIFFERENCE: {mutant.difference}")
    else:
        print("Difference key not found")
        print(json.dumps(element))
        break

    if program_key in element:
        program = element[program_key][0].get('@id')
        program_cleaned = program.replace("mb:program#", "")
        mutant.program = program_cleaned
        print(f"PROGRAM: {mutant.program}")
    else:
        print("Program key not found")
        print(json.dumps(element))
        break

    if operator_key in element:
        operators_list = element[operator_key]
        for operators in operators_list:
            operator_ids = operators['@id'].split(",")
            for operator_id in operator_ids:
                operator_cleaned = operator_id.replace("mb:operator#", "").strip()
                mutant.operator.append(operator_cleaned)
        print(f"OPERATORS: {mutant.operator}")

    if equivalence_key in element:
        equivalence = element[equivalence_key][0].get('@value')
        mutant.equivalence = equivalence
        print(f"EQUIVALENCE: {equivalence}")
        if mutant.equivalence == 'true':
            num_equiv += 1
        elif mutant.equivalence == 'false':
            num_non_equiv += 1
    else:
        print("Equivalence key not found")
        print(json.dumps(element))
        break

    if id_val := element.get('@id'):
        id_val_cleaned = id_val.replace("mb:mutant#", "")
        mutant.id = id_val_cleaned
        print(f"ID: {mutant.id}")
    else:
        print("ID key not found")
        print(json.dumps(element))
        break

    mutant.calculate_type()

    num_parsed += 1

    dp = UnifiedDiffParser(mutant.program, mutant.difference)
    # Store the original and modified code into a list of strings
    full_code = dp.parse_file(save_to_file=False)

    if mutant.type == "java":
        num_java_mutants += 1
        #convert_java(full_code)
    elif mutant.type == "c":
        num_c_mutants += 1
        #convert_c(full_code)


print(f"DATASET SIZE: {len(json_dict)}\n") 
print(f"NUM_PARSED = {num_parsed}")
print(f"NUM_IGNORED = {num_ignored}")
print(f"NUM_EQUIV = {num_equiv}")
print(f"NUM_NON_EQUIV = {num_non_equiv}")
print(f"NUM_JAVA_MUTANTS = {num_java_mutants}")
print(f"NUM_C_MUTANTS = {num_c_mutants}")