import csv
import json

path1 = "Etc"
path2 = "Fortified"
path3 = "Hard"
path4 = "Red"
path5 = "Rose"
path6 = "Sparkling"
path7 = "White"
path8 = 'pricep'

csvfile = open(path8+".csv", 'r')
jsonfile = open(path8+".json", 'w')

#fieldnames = ("Label", "abv", "degree", "sweet","acidity","body","tannin","price","year")
fieldnames = ("Australia")

reader = csv.DictReader(csvfile, fieldnames)
out = json.dumps([row for row in reader])
jsonfile.write(out)