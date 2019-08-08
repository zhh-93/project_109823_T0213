import yaml
import os
def analyze_file(file,case_name):
    with open(".\\data"+os.sep+file,"r") as f:
        data = yaml.load(f)[case_name]
        list_data = []
        for i in data.values():
            list_data.append(i)
        return list_data



