# a function that takes a list and target value
# while loop or recursion
# increaswe the steps each time a split is done
# conditions to track target position

def binarySearch(list, element):
    middle = 0
    start = 0
    end = len(list)
    steps = 0
    
    while (start <= end):
        print("Steps ", steps + 1, " :  ==> ", str(list[start:end+1]))
        
        steps = steps + 1
        middle = (start + end) // 2
        
        if element == list[middle]:
            print("Searched item is : ", list[middle])
            return middle
        
        elif element < list[middle]:
            end = middle
        
        else:
            start = middle + 1        
    return - 1

numList = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
target = 1

binarySearch(numList, target)