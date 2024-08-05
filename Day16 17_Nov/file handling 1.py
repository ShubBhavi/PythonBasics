import csv

with open("shubham1.txt",'a') as file:
    file.write("\npratik")

#csv-format

import csv

with open("data.csv",newline='') as csvfile:
   content=csv.reader(csvfile)
   for i in content:
       print(i)


#other method to read the csv file

with open("data.csv") as csvfile:
    data=csv.reader(csvfile)
    for i in data:
        print(i[0],i[1],i[2],sep='|')