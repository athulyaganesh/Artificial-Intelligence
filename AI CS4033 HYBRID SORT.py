#Homework Assignment 1

#Group 12 Members: 

#Haneesha Dushara
#Robbie Schad
#Nishanth Chidambaram
#Athulya Ganesh

#Implementation of Hybrid Sort

#According to the question, 
#1--> Mergesort
#2--> Quicksort
#3--> Bubblesort 

import time 

def merge(L1, L2):
  '''
  Merge takes  two sorted sublists, L1 and L2, 
  and combines them to return one sorted list.  
  '''
  result = []
  # merge L1 and L2
  while L1 != [] and L2 != []:
    if L1[0] < L2[0]:
      result.append(L1[0])
      L1.pop(0)
    else:
      result.append(L2[0])
      L2.pop(0)
      
  # if sublists are not equal length, 
  # append remainder of longer list to result
  if L1 != []:
    result += L1
  elif L2 != []:
    result += L2

  return result

def hybridSort(L, BIG, SMALL, T):
  '''
  hybridSort takes in a list L, 
  an int BIG (either 1 or 2, which correspond to mergesort or quicksort, respectively),
  an int SMALL (only possible value is 3, corresponding to bubblesort),
  and an int T, which corresponds to the threshold of whether the BIG or SMALL algorithm 
  should be used to sort L.
  '''
  # base case - use small function (bubbleSort)
  if len(L) <= T:
    if SMALL != 3:
      print('Invalid Input')
      return
    return bubbleSort(L) 

  elif BIG==1: # mergesort
    L1 = hybridSort(L[0:len(L)//2], BIG, SMALL, T) # recurse with first half of list
    L2 = hybridSort(L[len(L)//2:], BIG, SMALL, T) # recurse with second half of list
    return merge(L1, L2) # merge the two sorted sublists
    
  elif BIG==2: # quicksort    

    currentPosition = 0 #initializing position of Pivot element 

    for i in range(1, len(L)): 
         if L[i] <= L[0]:
              currentPosition = currentPosition + 1
              temp = L[i]
              L[i] = L[currentPosition]
              L[currentPosition] = temp

    temp = L[0]
    L[0] = L[currentPosition] 
    L[currentPosition] = temp 
    
    return  hybridSort(L[0:currentPosition], BIG, SMALL, T) + [L[currentPosition]] + hybridSort(L[currentPosition+1:len(L)],BIG, SMALL, T) #recursively call hybrid sort on the smaller lists

  else: 
    print("Invalid input")
    return

# bubbleSort
def bubbleSort(L):
  # iterate through elements
  for i in range(len(L)):
    for j in range(0, len(L)-i-1):
      # if the next element is less than the current element, swap them
      if L[j] > L[j+1]:
        temp = L[j+1]
        L[j+1] = L[j]
        L[j] = temp
  return L

#Test Cases 
print("Each test case prints mergesort and then quicksort") 
print("Example 1")
L = [90, 1, 29, 43, 54, 21, 30, 77, 101, 4, 19, 2 ]
T = 3
start = time.time() 
print(hybridSort(L, 1, 3, T))
end = time.time() 
print("Execution time (mergesort): " , end - start)
start = time.time() 
print(hybridSort(L,2,3,T))
end = time.time() 
print("Execution time (quicksort): " , end - start, '\n')
L.clear()

print("Example 2")  
L = [7,1,9,6,7]
T = 2 
start = time.time() 
print(hybridSort(L,1,3,T))
end = time.time() 
print("Execution time (mergesort): " , end - start)
start = time.time() 
print(hybridSort(L,2,3,T))
end = time.time() 
print("Execution time (quicksort): " , end - start, '\n')
L.clear() 


print("Example 3") 
L = [9, 90, 3, 40, 23, 50, 56, 12 , 67, 34, 564]
T=5
start = time.time()
print(hybridSort(L,1,3,T))
end = time.time() 
print("Execution time (mergesort): " , end - start)
start = time.time()
print(hybridSort(L,2,3,T)) 
end = time.time() 
print("Execution time (quicksort): " , end - start, '\n')

print("Example 4") 
L = [28,11,32,5,47,42,91,86,3,17,10,71,66,  33,   14,   8 ]
T=5
start = time.time()
print(hybridSort(L,1,3,T))
end = time.time() 
print("Execution time (mergesort): " , end - start)
start = time.time()
print(hybridSort(L,2,3,T)) 
end = time.time() 
print("Execution time (quicksort): " , end - start, '\n')

# Compare the behavior of these algorithms (for example, number of comparisons, or execution time).
'''
Test case results (pasted below) show that quickSort is slightly faster than mergeSort in all 4 cases in terms of computation time.
However, both of these two algorithms are faster than bubbleSort, since mergeSort and quickSort perform
O(nlogn) comparions in the average case, while bubbleSort performs O(n^2) comparions in the average case.


Example 1
[1, 2, 4, 19, 21, 29, 30, 43, 54, 77, 90, 101]
Execution time (mergesort):  0.0003094673156738281
[1, 2, 4, 19, 21, 29, 30, 43, 54, 77, 90, 101]
Execution time (quicksort):  0.0002377033233642578 

Example 2
[1, 6, 7, 7, 9]
Execution time (mergesort):  0.00021886825561523438
[1, 6, 7, 7, 9]
Execution time (quicksort):  0.00019812583923339844 

Example 3
[3, 9, 12, 23, 34, 40, 50, 56, 67, 90, 564]
Execution time (mergesort):  0.0003287792205810547
[3, 9, 12, 23, 34, 40, 50, 56, 67, 90, 564]
Execution time (quicksort):  0.00022554397583007812 

Example 4
[3, 5, 8, 10, 11, 14, 17, 28, 32, 33, 42, 47, 66, 71, 86, 91]
Execution time (mergesort):  8.20159912109375e-05
[3, 5, 8, 10, 11, 14, 17, 28, 32, 33, 42, 47, 66, 71, 86, 91]
Execution time (quicksort):  5.8650970458984375e-05 

'''