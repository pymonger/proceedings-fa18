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

print(yaml.dump(readmes, default_flow_style=False))

print ("| hid | lastname | firstname | community | t1 | t2 | t3 | t4 | paper |")
print ("| --- | --- | --- | --- | --- | --- | --- | --- | --- |")
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
        "paper": "ERROR",
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

    # paper
    if "paper" in s:
      print (s["paper"])
      try:
          title = s["paper"][0]["title"] or "TBD"
          url   = s["paper"][0]["url"] or "TBD"

          if group in ["paper"][0]:
              group_hid = group in ["paper"][0]

              if group_hid != hid:
                  entry["paper"] = "see [paper]({url})".format(url=url)
              else:
                  entry["paper"] = "[paper]({url})".format(url=url)
      except:
          paper = "TBD"
        
    print ("{hid} | {lastname} | {firstname} | {community} | {t1} | {t2} | {t3} | {t4} | {paper} |".format(**entry))
