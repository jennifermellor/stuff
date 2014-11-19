__author__ = 'jen'
import csv
import random

reader = csv.reader(open('/Users/rick/Documents/Hovee Names/RandomizedFemale.csv', "rb"), delimiter = ",", skipinitialspace=True)
readerM = csv.reader(open('/Users/rick/Documents/Hovee Names/RandomizedMale.csv', "rb"), delimiter = ",", skipinitialspace=True)


listofnames = []

for name in reader:
    name.insert(0, 'female');
    listofnames.append(name)

for name in readerM:
    name.insert(0, 'male');
    listofnames.append(name)

random.shuffle(listofnames)
random.shuffle(listofnames)
random.shuffle(listofnames)

for i in listofnames:
    print i

print len(listofnames)

resultFile = open("/Users/rick/Documents/Hovee Names/RandomizedNames.csv",'wb')
resultFile.write('gender,first_name,last_name\n');
for row in listofnames:
    row[1] = ','.join(row[1].split())
    resultFile.write(','.join(row) + '\n')


