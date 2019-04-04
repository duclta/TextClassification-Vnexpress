import csv
file = open("contents.txt", "w")

with open('contents.csv', 'r') as csvFile:
    reader = csv.reader(csvFile)
    for row in reader:
        label = "__label__" + row[2].strip().replace('\n','').replace('\xa0','').replace(' ','-').lower()
        title = row[3].strip().lower()
        arr = ['.',',',':','?','!','(',')','"',"'",' -','- ','\n','\xa0']

        for item in arr:
            title = title.replace(item,'')

        file.writelines(label + " " + title + "\n")

csvFile.close()
file.close()
