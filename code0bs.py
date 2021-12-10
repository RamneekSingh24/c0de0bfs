import os
import sys
import re

args = sys.argv

if len(args) != 2:
    print("Please use python3 code0bs.py [file-name]")
    exit()

with open(args[1], "r") as f:
    code = f.read()


binops = ["+", "-", "*", "/", "^", "&", "|", "||", "&&", "<<", ">>"]
uniops = ["++", "--", "-", "*"]

[preprocessor, code] = code.split("// @End Preprocessor //")




brackets = ["(", ")", "{", "}", "[", "]", ";"]

bracket_spaced_code = ""

for c in code:
    if c in brackets:
        bracket_spaced_code += f" {c} "
    else:
        bracket_spaced_code += c

code = bracket_spaced_code

str_extacted = re.split('(".*")', code)

tokens = []

for text in str_extacted:
    if re.match('".*"', text):
        tokens += [" ", text, " "]
    else:
        tokens += re.split("(\s)", text)

print(tokens)
        


defines = {}

for i, tok in enumerate(list(set(tokens))):

    if not tok.isspace():
        defines[tok] = "e" * (i + 1)


output_code = "// Comments ?!? \n"

preprocessor = preprocessor.split("\n")
preprocessor = [f"/*  ****\ ‮ /* ****/ {line}" for line in preprocessor]
preprocessor = "\n".join(preprocessor)

output_code += preprocessor + "\n" 

for tok in defines:
    output_code += f"/*  ****\ ‮ /* ****/  #define {defines[tok]} {tok} \n"

output_code += "// End Comments !! //\n"

for tok in tokens:
    if tok.isspace():
        output_code += tok
    else:
        output_code += defines[tok]



with open("output.cpp", "w") as f:
    f.write(output_code)










        









