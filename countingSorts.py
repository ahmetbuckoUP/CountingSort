import random
import time

#Comparison Counting Sort
def comparisonCountingSort(list):
    # list = [13, 6, 9, 3, 10, 7]
    start_time = time.time()
    dataDict = {}
    sortedList = []
    count = 0
    print(len(list))
    for i in range(0, len(list)):
        for j in range(0, len(list)):
            if list[i] > list[j]:
                # print(list[i])
                count = count + 1
        d = {count: list[i]}
        dataDict.update(d)
        count = 0
    for i in range(0, len(list)):
        sortedList.append(dataDict[i])
    print("%s seconds " % (time.time() - start_time))
    # print('Unsorted List {}'.format(list))
    # print('Sorted Array with Comparison Counting Sort {}'.format(sortedList))

#Distribuiton Counting Sort
def DistributinCountingSort(list):
    # list = [9, 6, 9, 9, 6, 5]
    start_time = time.time()
    dataDict = {}
    unique = set(list)
    unique = sorted(unique)
    distributionValues = {}
    sortedList = []
    count = 0
    for i in range(0, len(list)):
        for j in range(0, len(list)):
            if list[i] == list[j]:
                count = count + 1
        encounter = {list[i]: count}
        dataDict.update(encounter)
        dataDict = dict(sorted(dataDict.items(), key=lambda item: item[0]))
        count = 0
    # print('Encounter Times{}'.format(dataDict))
    j = 0
    for i in unique:
        j = j + dataDict[i]
        dValues = {i: j}
        distributionValues.update(dValues)
    # print('Distributed Values {}'.format(distributionValues))
    for i in dataDict.keys():
        for j in range(0, dataDict[i]):
            if dataDict[i] == 0:
                break
            else:
                sortedList.append(i)
                dataDict[i] = dataDict[i] - 1
                continue
    # print('Sorted List with Distribution Counting Sort {}'.format(sortedList))
    print("%s seconds " % (time.time() - start_time))

dataLists =[]
for i in range(0,1000000):
    dataLists.append(i)

print('\n<----------Comparison Counting Sort--------->\n')
# comparisonCountingSort([13, 6, 9, 3, 10, 7])
comparisonCountingSort(dataLists)
print('\n<----------Distribution Counting Sort--------->\n')
# DistributinCountingSort([9, 6, 9,21,21, 9, 6, 5])
DistributinCountingSort(dataLists)




