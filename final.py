import csv

dataSet1=[]
dataSet2=[]

with open('bright_stars.csv', 'r') as f:
    csvReader=csv.reader(f)
    for row in csvReader:
        dataSet1.append(row)

with open('dwarf_star.csv','r') as f:
    csvReader=csv.reader(f)
    for row in csvReader:
        dataSet2.append(row)

headers1=dataSet1[0]
star_data_1=dataSet1[1:]

headers2=dataSet2[0]
star_data_2=dataSet2[1:]

headers=headers1+headers2
star_data=[]

for index, data_row in enumerate(star_data_1):
    star_data.append(star_data_1[index]+star_data_2[index])

with open('final.csv','a+') as f:
    csvWriter=csv.writer(f)
    csvWriter.writerow(headers)
    csvWriter.writerows(star_data)