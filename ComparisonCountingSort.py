list = [13,6,9,3,10,7]
dataDict = {}
sortedList = []
count = 0
for i in range(0,len(list)):
    for j in range(0,len(list)):
        if list[i]>list[j]:
            # print(list[i])
            count = count + 1
    d = {count:list[i]}
    dataDict.update(d)
    count = 0
for i in range(0,len(list)):
    sortedList.append(dataDict[i])
print('Unsorted List {}'.format(list))
print('Sorted Array with Comparison Counting Sort {}'.format(sortedList))