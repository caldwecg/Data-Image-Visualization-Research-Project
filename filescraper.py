webarray = []
filearray = []
import os
import re
import json
import fileinput

directory = os.fsencode("./views")

for file in os.listdir(directory):
    filename = os.fsdecode(file)
    if not filename.endswith(".DS_Store"):
        with open('./views/'+ filename) as topo_file:
            for line in topo_file:
                if "      <a href=" in line:
                    if not "<a href=\"index" in line:
                        found = re.findall(r'"([^"]*)"', line)
                        webarray+=found


# with open('data.json', 'w') as jsonfile:
#     json.dump(webarray, jsonfile)


for file in os.listdir(directory):
    filename = os.fsdecode(file)
    if not filename.endswith(".DS_Store"):
        with open('./views/'+ filename) as topo_file:
            for line in topo_file:
                if "<img src=" in line:
                    found = re.findall(r'"([^"]*)"', line)
                    newfound = [found[0]]
                    filearray+=newfound




dictionary = dict(zip(filearray, webarray))

for file in os.listdir(directory):
    filename = os.fsdecode(file)
    if not filename.endswith(".DS_Store"):
        with fileinput.FileInput('./views/'+ filename, inplace=True, backup='.bak') as file:
            for line in file:
                if "<img src=" in line:
                    found = re.findall(r'"([^"]*)"', line)
                    newfound = found[0]
                    print(line.replace(newfound, dictionary[newfound]), end='')
                else:
                    print(line, end='')

print("Text replaced")

