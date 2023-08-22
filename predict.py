import csv
from sklearn import tree

x = []
y = []
loc = "elahiyeh" #input('plz enter the location  : (Choose between   "elahiyeh"    "sanayea"   "jolfa"    "shoosh"   "darrous"   "hafthoz"   "piroozi") ')
def locate(loc):
    if loc=='elahiyeh' :
        with open('csvs\elahiye1.csv', 'r') as csvfile: 
            data = csv.reader(csvfile)
            for l in data:
                x.append(l[0:8])
                y.append(l[9])
                print(y)
        loc=1000
    if loc=='jolfa' :
        with open('a_crawl\\csvfiles\\jolfa.csv', 'r') as csvfile:  
            data = csv.reader(csvfile)
            for l in data:
                x.append(l[0:8])
                y.append(l[9])
                loc=600
    if loc=='sanayea' :
        with open('a_crawl\\csvfiles\\sanayea.csv', 'r') as csvfile: 
            data = csv.reader(csvfile)
            for l in data:
                x.append(l[0:8])
                y.append(l[9])
        loc=500
    if loc=='shoosh' :
        with open('a_crawl\\csvfiles\\shoosh.csv', 'r') as csvfile:  
            data = csv.reader(csvfile)
            for l in data:
                x.append(l[0:8])
                y.append(l[9])
        loc=100
    if loc=='darrous' :
        with open('a_crawl\\csvfiles\\darrous.csv', 'r') as csvfile:  
            data = csv.reader(csvfile)
            for l in data:
                x.append(l[0:8])
                y.append(l[9])
            
        loc=800
    if loc=='hafthoz' :
        with open('a_crawl\\csvfiles\\hafthoz.csv', 'r') as csvfile:  
            data = csv.reader(csvfile)
            for l in data:
                x.append(l[0:8])
                y.append(l[9])
        loc=400
    if loc=='piroozi' :
        with open('a_crawl\\csvfiles\\piroozi.csv', 'r') as csvfile:  
            data = csv.reader(csvfile)
            for l in data:
                x.append(l[0:8])
                y.append(l[9])
        loc=300
        
    return loc
location=locate(loc)

area = input('plz enter the area <per meter>  : ')
constr = input('plz enter the Year of construction <like "1401"> : ')
rooms = input('plz enter the rooms  : ')
floor = input('plz enter the Floor  : ')
whouse = input('Does it have a warehouse? : y/n ')
parking = input('Does it have a parking? : y/n ')
elevator = input('Does it have elevator? : y/n ')

if elevator=='y':
    elevator=1
else:
    elevator=0

if parking=='y':
    parking=1
else:
    parking=0

if whouse=='y':
    whouse=1
else:
    whouse=0

clf = tree.DecisionTreeClassifier()
clf = clf.fit(x, y)
newd = [[location, area, constr, rooms, floor, whouse, parking, elevator]]
prediction = clf.predict(newd)
print('Price is : ',prediction)