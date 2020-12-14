list = [9,6,9,9,6,5]
dataDict = {}
unique = set(list)
unique = sorted(unique)
distributionValues ={}
sortedList = []
count = 0
for i in range(0,len(list)):
    for j in range(0,len(list)):
        if list[i]==list[j]:
            count = count+1
    encounter = {list[i]:count}
    dataDict.update(encounter)
    dataDict =dict(sorted(dataDict.items(), key=lambda item: item[1]))
    count = 0
print('Encounter Times{}'.format(dataDict))
j = 0
for i in unique:
    j = j + dataDict[i]
    dValues = {i:j}
    distributionValues.update(dValues)
print('Distributed Values {}'.format(distributionValues))
for i in dataDict.keys():
    for j in range(0,dataDict[i]):
        if dataDict[i] == 0:
            break
        else:
            sortedList.append(i)
            dataDict[i] = dataDict[i] - 1
            continue
print('Sorted List with Distribution Counting Sort {}'.format(sortedList))


