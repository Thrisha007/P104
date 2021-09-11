import csv

with open("HeightWeight.csv", newline = '') as f:
    reader = csv.reader(f)
    file_data = list(reader)

file_data.pop(0)
newData = []

for i in range(len(file_data)):
    n_num = file_data[i][2]
    newData.append(float(n_num)) 

n = len(newData)
total = 0

for x in newData:
    total = total + x

mean = total/n
print('Mean weight is ', str(mean))