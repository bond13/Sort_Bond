#Selection Sort for our project (Team Fullhouse)
#Takes in an array and sorts it
#O(n^2) algorithm

def sort(urls):
  size = len(urls)

  for index in range(size-1):
    indexOfSmallest = findSmallest(urls, index, size)
    if(index != indexOfSmallest):
      temp = urls[index]
      urls[index] = urls[indexOfSmallest]
      urls[indexOfSmallest] = temp

  return urls

def findSmallest(arr, i, size):
  currSmallestIndex = i
  for j in range(i, size):
    if(arr[j] < arr[currSmallestIndex]):
      currSmallestIndex = j

  return currSmallestIndex
