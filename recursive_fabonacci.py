def get_fib(position):

    '''
    Implement a function recursively 
    to get the desired
    Fibonacci sequence value.
    '''
    if position == 0 or position == 1:
        return position
    return get_fib(position - 1) + get_fib(position - 2)

if __name__ =="__main__":
   print(get_fib(4))
