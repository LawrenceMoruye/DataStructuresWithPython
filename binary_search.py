'''
from Udacity's Introduction to Data Structures
 and algorithms course
Binary search func using iterative approach
(loops).
Takes 2 inputs,a list and value to search
Assuming the list only has distinct elements,
meaning there are no repeated values, and 
elements are in a strictly increasing order.
Return the index of value, or -1 if the value
doesn't exist in the list."

'''

def binary_search(input_array,value):
    low = 0
    high = len(input_array) - 1
    while (low <= high):
        mid = (low + high)//2
        if (input_array[mid] == value):
            return mid
        elif(input_array[mid] < value):
            low = mid + 1 
        else:
            high = mid - 1

    return -1


if __name__ =="__main__":
    test_list = [1,3,9,11,15,19,29]

    val1 = 25
    val2 = 15
    print(binary_search(test_list,val1))
    print(binary_search(test_list,val2))


