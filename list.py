import glob
from pprint import pprint
import oyaml as yaml

files = glob.glob("fa18*/README.yml")

pprint (files)
readmes = {}
for readme in files:
    with open(readme, 'r') as stream:
        filename = readme.replace("/README.yml","") # use dir name or so
        try:
            d = yaml.load(stream)
            readmes[filename] = d
        except yaml.YAMLError as exc:
            print(exc)


#pprint (readmes)

# print(yaml.dump(readmes, default_flow_style=False))
