import csv
data=[]
with open('final.csv','r') as f:
    csvReader=csv.reader(f)
    for row in csvReader:
        data.append(row)

headers=data[0]
star_data=data[1:]

#Converting all planet names to lowercase
for data_point in star_data:
    data_point[0]=data_point[0].lower()

#Sorting planet names in alphabetical order
star_data.sort(key=lambda star_data:star_data[0])

with open('final_merged_sorted.csv','a+') as f:
    csvWriter=csv.writer(f)
    csvWriter.writerow(headers)
    csvWriter.writerows(star_data)