country = input('EU or US? ')
if country == 'US'
    eufloor = input('European Floor? ') 
    usfloor = int(eufloor) + 1
    print('US Floor', usfloor)
else if country == 'EU'
    usfloor = input('US Floor? ')
    eufloor = int(usfloor) - 1
    print('EU Floor', eufloor)
