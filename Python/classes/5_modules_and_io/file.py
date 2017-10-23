# f = open('text_file.txt', 'r')
# print(f)
# print(f.read())
#
# print(f.readline())

# for line in f:
#     print (line),
#
# print(f.closed)

# with open('text_file.txt', 'r') as f:
#     read_data = f.read()
# print(f.closed)

# f = open('write_file.txt', 'w')
# f.write('hello')
# f.close()
# print f.closed

# JSON file
# https://docs.python.org/2/library/json.html
# import json
# with open('eur_usd.json', 'r') as f:
#     data = f.read()
#     json_data = json.loads(data)
# print(json_data['granularity'])
# print(json.dumps(json_data))

# CSV file
# https://docs.python.org/2/library/csv.html
# import csv
# with open('eur_usd_2.csv', 'w') as csvfile:
#     fieldnames = ['time', 'openMid', 'highMid', 'lowMid', 'closeMid', 'volume', 'complete']
#     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#     writer.writeheader()
#     for row in json_data['candles']:
#         writer.writerow(row)

# with open('eur_usd.csv', 'r') as f:
#     content = f.readlines()
#     for row in content:
#         print(row)
#
# import csv
# with open('eur_usd.csv', 'r') as f:
#     reader = csv.reader(f)
#     for row in reader:
#         print(row)
# 
# import csv
# with open('eur_usd.csv', 'wb') as f:
#     writer = csv.writer(f)
#     writer.writerows(someiterable)
