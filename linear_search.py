'''
Given an array of n elements, 
write a function to search a given element x .
steps:
 -Start from the leftmost element of array
 and one by one compare x with each element of arr[]
- If x matches with an element, return the index.
If x doesn’t match with any of elements, return -1.

'''

def linearsearch(input_array,value):
    index = 0
    while (index < len(input_array ) and input_array[index]< value):
        index +=1
    if (index >= len(input_array)or input_array[index] != value):
        return -1
    return index



if __name__ =="__main__":
    test_list = [1,3,9,11,15,19,29]

    val1 = 1
    val2 = 15
    print(linearsearch(test_list,val1))
    print(linearsearch(test_list,val2))
