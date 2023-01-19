### use quotes to use commas, can use quotes for every column
import csv

csv_file =  csv.reader(open('demo.csv', 'r', encoding='UTF-8'))
### essentially scanner
### r=read only
### UTF-8 is to make grading easier in github
### You can name your parameters and they don't have to be in order. Ex: encoding doesn't have to be the 3rd parameter

for row in csv_file:
    print(row)
    print(row[0])

with (open('demo.csv', 'r', encoding="UTF-8")) as f:
    csv_file = csv.reader(f)
    for row in csv_file:
        print(row)
### creates a csv file and then closes it at the end

dct={'hello': 'there', 'this': 'one'}
print(dct['hello'])

csv_file = csv.DictReader(open('demo.csv','r', encoding="UTF-8"))
for row in csv_file:
    print(row)
    print(row['name'])

# def some_method(a, b, c, d):
#     pass
# some_method(1, 2, 3, 4)
# some_method(d=4, b=3, a=1, c=7)

# def some_method():
#     return 1, 2, 3