# list = [13,6,9,3,10,7]
list = [9, 6, 9,21,21, 9, 6, 5]
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
    try:
        sortedList.append(dataDict[i])
        continue
    except:
        data = 0
print('Unsorted List {}'.format(list))
print('Sorted Array with Comparison Counting Sort {}'.format(sortedList))