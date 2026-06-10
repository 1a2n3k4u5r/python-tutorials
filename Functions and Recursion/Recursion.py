# When a function calls itself repeatedly
# A recursion and loop are used to perform the same function or work.
# in recursion base case is used to decide that recursion is stop or not 

# prints n to 1 backwards
def show(n):
    if (n == 0):
        return
    print(n)
    show(n-1)
    print("END") # 5 times print END

show(5)
 #5
# 4
# 3
# 2   
# 1

#returns n!
def fact(n):
    if(n == 0 or n == 1):
        return 1
    else:
        return n * fact(n-1)
    
print(fact(5))

# write  a recursive function to calculate the sum of first n natural numbers.
def calc_sum(n):
    if(n == 0):
        return 0
   
    return calc_sum(n-1) + n
sum = calc_sum(5)
print(sum)

# write a recursive function to print all elements in a list

def print_list(list, idx=0):
    if(idx == len(list)):
        return
    print(list[idx])
    print_list(list,idx+1)

fruits = ["mango","litchi","apple", "banana"]

print_list(fruits)
#mango
# litchi
# apple
# banana
