from globals import *
import os

class UnifiedDiffParser:
    def __init__(self, program=None, difference=None):
        self.program = program
        self.difference = difference
        self.string_to_del = """"""
        self.string_to_add = """"""
        self.line_num_to_del = None
        self.line_num_to_add = None  
        self.parse_unified_diff()
  
    def parse_unified_diff(self):
        # split the self.difference into lines
        lines = self.difference.strip().split("\n")
        self.line_num_to_del = int(lines[0].split(" ")[1].split(",")[0][1:])
        self.line_num_to_add = int(lines[0].split(" ")[2].split(",")[0][1:])
        # remove the first line
        lines = lines[1:]

        # get the string to del or add
        for line in lines:
            if line.startswith("-"):
                self.string_to_del += line[1:]
            elif line.startswith("+"):
                self.string_to_add += line[1:]

    def parse_file(self, save_to_file=True):
        with open(f"./dataset/programs/{self.program}", 'r') as f:
            file = iter(f)
            file_copy = list(file)

        # modify the list of lines as needed
        del file_copy[self.line_num_to_del - 1]
        file_copy.insert(self.line_num_to_add - 1, self.string_to_add + '\n')

        orig_str = ''.join(file_copy)
        mod_str = ''.join(file_copy)

        if save_to_file:
            path = "./modified_files"
            original_file_name = f"{self.program}.original"
            modified_file_name = f"{self.program}.modified"

            if not os.path.exists(path):
                os.makedirs(path)

            original_file_path = os.path.join(path, original_file_name)
            modified_file_path = os.path.join(path, modified_file_name)
            
            # write the modified and original content to separate files in the new directory
            with open(original_file_path, "w") as orig_file, open(modified_file_path, "w") as mod_file:
                orig_file.write(''.join(file_copy))
                mod_file.write(''.join(file_copy))

        return [orig_str, mod_str]

    def print_all(self):
        print(self.line_num_to_del)
        print(self.line_num_to_add)
        print(self.string_to_del)
        print(self.string_to_add)