import glob
from pprint import pprint
import oyaml as yaml
import os

files = glob.glob("fa18*/README.yml")

#pprint (files)
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

#print(yaml.dump(readmes, default_flow_style=False))

print ("| hid | lastname | firstname | community | t1 | t2 | t3 | t4 |")
print ("| --- | --- | --- | --- | --- | --- | --- | --- |")
for hid in readmes:
    entry = {
        "hid": "ERROR",
        "firstname": "ERROR",
        "lastname": "ERROR",
        "community": "ERROR",
        "t1": "ERROR",
        "t2": "ERROR",
        "t3": "ERROR",
        "t4": "ERROR",
        }
    s = readmes[hid]
    
    entry["hid"] = hid
    entry["lastname"] = s["owner"]["lastname"]
    entry["firstname"] = s["owner"]["firstname"]
    entry["community"] = s["owner"]["community"]

    t = ""
    try:
        c = -1
        for t in ["t1", "t2", "t3", "t4"]:
            c = c + 1
            url = s["technologies"][c]["url"]
            entry[t] = "[{t}]({url})".format(t=t,url=url)
    except Exception as e:
        pass
    print ("{hid} | {lastname} | {firstname} | {community} | {t1} | {t2} | {t3} | {t4} |".format(**entry))
