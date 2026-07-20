import sys
# for i in range(5,0,-1):
#     print(i)

def countdown(n):
  if n <= 0:
    print("Done!")
  else:
    print(n)
    countdown(n - 1)

# countdown(5)



# 5! =?? (5 * 4 * 3 * 2 * 1) = 120
# def factorial(n):
#   # Base case
#   if n <= 1:
#     return 1
#   # Recursive case
#   else:
#     return n * factorial(n - 1) # 5 * (5-1) = 20 * (4-1) = 60 * (3-1) = 120 * (2-1) = 120

# print(factorial(5))



# def sum_list(numbers):
#     if len(numbers) == 0:
#         return 0
#     elif len(numbers) == 1:
#         return numbers[0]
#     else:
#         return numbers[0] + sum_list(numbers[1:])
# # [0]=1 + ([1]=2) = 3 + ([2]=3) = 6 + ([3]=4) = 10 + ([4]=5) = 15
# my_list = [1, 2, 3, 4, 5]
# print(sum_list(my_list))



def find_max(numbers):
    if len(numbers) == 1:
        return numbers[0]
    else:
        max_of_rest = find_max(numbers[1:])
        return numbers[0] if numbers[0] > max_of_rest else max_of_rest
    # if the function is called at line 45 then how the return statement will execute?
#Python has a limit on how deep recursion can go. The default limit is usually around 1000 recursive calls.
#If you need deeper recursion, you can increase the limit, but be careful as this can cause crashes:
my_list = [3, 7, 2, 9, 1]
print(find_max(my_list))

#Increasing the recursion limit should be done with caution. For very deep recursion, consider using iteration instead.

#not required it's use to set limit to the recursion function
sys.setrecursionlimit(2000)
print(sys.getrecursionlimit())