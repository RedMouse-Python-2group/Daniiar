import csv
op = open('price_list.csv', 'r')
reader = csv.reader(op)

for row in reader:
    print(row)
    sh = int(row[1])
    pr = int(row[2])
    if sh >= 1:
        print('Shtuki')
    elif pr >= 1:
        print('Pary')
    else:
        pass
op.seek(0)
count_rows = sum(1 for row in reader)
print("Quantity of rows", count_rows)
op.seek(0)
count_q = sum(1 for row in reader if int(row[1]) >= 1)
print(count_q)
op.seek(0)
count_p = sum(1 for row in reader if int(row[2]) >= 1)
print(count_p)
op.close()
x = count_q
y = count_p
op = open("price_list.csv", "a")
writer = csv.writer(op, delimiter=',', quoting=csv.QUOTE_MINIMAL)
writer.writerow(['Results', x, y])
op.close()

# for_database = open("results.csv", 'w')
# write = csv.writer(op, delimiter=',', quoting=csv.QUOTE_MINIMAL)
# writer.writerow(['Results', x, y])
# for_database.close()
