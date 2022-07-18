def merge (leftlist, rightlist):
  newList = []
  leftindex = 0 
  rightindex = 0 

  while leftindex < len(leftlist) and rightindex < len(rightlist):
    if leftlist[leftindex] < rightlist[rightindex]:
      newList.append(leftlist[leftindex])
      leftindex += 1 
    else:

      newList.append(rightlist[rightindex])
      rightindex += 1
  
  while leftindex < len(leftlist):


    newList.append(leftlist[leftindex])
    leftindex += 1
  while rightindex < len(rightlist):

    newList.append(rightlist[rightindex])
    rightindex += 1   
  
  return newList

print(merge([1, 3, 5], [2,4]))

# def binarySearch(alist, key):
#   first = 0 
#   last = len(alist)-1
#   found = False

#   while first <= last and not found:
#     midpoint = (first + last)//2
#     if alist[midpoint][0] == key:
#       print(alist[midpoint][1])
#       found = True
#     else:
#       if key < alist[midpoint][0]:
#         last = midpoint - 1
#       else:
#         first = midpoint + 1
#   return found
# unitsFile = open("units.txt")

# unitsList = []

# for line in unitsFile:
#   items = line.strip().split(";")
#   unitsList.append([int(items[0]), items[1]])
# # print(unitsList)

# print(binarySearch(unitsList, 3))
