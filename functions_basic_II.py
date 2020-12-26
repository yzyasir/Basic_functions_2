# # # # 1) Countdown
# my_list = []
# def countdown(num):
#     for num in range(num, -1, -1):
#         my_list.append(num) 
#     return my_list
# # print(countdown(5))
# # # placing num instead of x gave the loop iteration


# # # 2) Print and Return
# def printreturn(x,y):
#     print(x)
#     return(y)
# # print(printreturn(1,2))
# # The print function when calling the funtion only returns and shows the 2


# # 3) First Plus Length
# def pluslength(arr):
#     x = arr[0] + len(arr)
#     return(x)
# # print(pluslength([3, 2, 3, 4, 5]))
# # The reason it wasnt working at first was because I put sqaure brackets around arr in the len


# # 4) Values Greater than Second
# def greatersecond(arr):
#     compare = arr[1]
#     new_array = []
#     count = 0
#     for x in range(0, len(arr), 1):
#         if compare < arr[x]:
#             new_array.append(arr[x])
#             count = count + 1
#     print(count)
#     if len(new_array) <= 2:
#         print("False")
#     return(new_array)
# # print(greatersecond([3, 1, 3, 3]))
# So I experimented and figured out where print of count needs to be, it needs to beout of the loop right after the if 
# the if statement needed to be indented back to catch the final array len 

# 5) This Length, That Value
# def lengthValue(size, value):
#     new_array = []
#     for x in range(0, size, 1):
#         new_array.append(value)
#     return(new_array)
#     print(new_array)
# print(lengthValue(7, 2))


