import googlemaps
from datetime import datetime
import csv

gmaps = googlemaps.Client(key = open('MapsKey.txt','r',encoding='utf-8').read())

with open('Cities.csv',newline='',encoding='utf-8') as myFile, open('FullCities.csv','w',newline='',encoding='utf-8') as writeFile:
    reader = csv.reader(myFile)
    writer = csv.writer(writeFile,delimiter=',')
    #Skip Header
    firstRow = True
    for row in reader:
        if firstRow == True:
            writer.writerow(row)
            firstRow = False
        else:
            print('Original row: {}'.format(row))
            found = False
            attempts = 0
            while(found == False and attempts <10):
                directions_result = gmaps.directions(row[0],row[2],mode="driving")
                if directions_result != []:
                    directions_result = directions_result[0]['legs'][0]
                    print('Road distance: {}'.format(directions_result['distance']['text']))
                    print('Road duration: {}'.format(directions_result['duration']['text']))

                    #Store distance
                    row[3] = directions_result['distance']['text'].split(' ')[0]

                    #Store Time
                    if len(directions_result['duration']['text'].split(' ')) > 2:
                        #Hour
                        row[4] = directions_result['duration']['text'].split(' ')[0]
                        #Minutes
                        row[5] = directions_result['duration']['text'].split(' ')[2]
                        #Store Hour + decimal(min). e.g. 1h15min = 1.25h
                        row[6] = str(int(directions_result['duration']['text'].split(' ')[2])/60 + int(row[4]))
                    else:
                        #Just minutes
                        row[5] = directions_result['duration']['text'].split(' ')[0]
                        row[6] = str(int(row[5])/60)
                    found = True
                else:
                    attempts = attempts + 1
                    print('Did not find route from {} and {}. Tried {} times'.format(row[0],row[2],attempts))
            print('Final row: {}'.format(row))
            writer.writerow(row)

'''
gmaps = googlemaps.Client(key = open('MapsKey.txt','r').read())

now = datetime.now()
directions_result = gmaps.directions("Sydney Town Hall",
                                     "Parramatta, NSW",
                                     mode="transit")[0]['legs'][0]

print(directions_result)
'''