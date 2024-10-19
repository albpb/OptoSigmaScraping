import re
import json
from tabulate import tabulate

# we will use this specs to iterate on the previous json
new_specs = ["\n                        Name                    ", 
            "\n                        Weight                    ",
            "Focal length",
            "Diameter \u03c6D",
            "Edge thickness te",
            "Center thickness tc",
            "Back focal length fb",
            "Radius of curvature  r"]


new_json_dict = {}

with open("product.json", "r") as product_json:
    # get data
    data = json.load(product_json)

    for row_key, row_value in data.items():
        new_product = {}
        for spec in new_specs:
            # format value
            proc_value = re.sub(r"^\s+|\s+$", "", row_value[spec])
            # eliminate lambda from diameter

            # (comment): I tried to detect specific special characters, but when python builds strings
            # it processes the special characters, so if I try to detect it by using something as "\\u[etc]"
            # python can't understand it, as it is not \u03c6 anymore, it is "φ".
            # Also, I used the following REGEX: [^\x00-\x7F]+ but it is really limited, and erases useful
            # characters as €, or vowels with accents. As a temporal solution, this REGEX erases only φ.

            proc_value = re.sub(r"\u03c6", "", proc_value)
            proc_value = re.sub(r"(\d+)([a-zA-Z]+)", r"\1 \2", proc_value)
            # format key
            proc_key = re.sub(r"^\s+|\s+$", "", spec)
            proc_key = re.sub(r"\u03c6", "", proc_key)
            # eliminates abbreviation (max 3 chars)
            proc_key = re.sub(r"\s+[a-zA-Z]{1,3}\s*$", "", proc_key)


            new_product[proc_key] = proc_value
        
        new_json_dict[row_key] = new_product


with open("product.json", "w") as json_file:
    json.dump(new_json_dict, json_file, indent=4)

for row in new_json_dict:
    product = new_json_dict[row]
    tabla = [[clave, valor] for clave, valor in product.items()]

    print("Table of "+row)
    print(tabulate(tabla, headers=["Propiedad", "Valor"], tablefmt="grid"))
    print("\n")
    










