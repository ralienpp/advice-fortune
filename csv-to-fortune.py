import csv


advice_fortune = open('out/advice-fortune.txt', 'wb')

with open('out/advice-fortune.csv', 'rb') as advice_file:
    advice_reader = csv.reader(advice_file)
    for advice, number in advice_reader:
        advice_fortune.write('%s\n%%\n' % advice)

advice_fortune.close()
print('Done')
