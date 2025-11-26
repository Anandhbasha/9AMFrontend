# # # def digit_maze_simple(number):
# # #     num_str = str(number)
# # #     n = len(num_str)
# # #     all_paths = []
    
# # #     def dfs(current, path):
# # #         if len(path) > 1 and path not in all_paths:
# # #             all_paths.append(path.copy())
        
# # #         for i in range(n - 1):
# # #             lst = list(current)
# # #             lst[i], lst[i + 1] = lst[i + 1], lst[i]
# # #             next_state = ''.join(lst)
            
# # #             if next_state not in path:
# # #                 path.append(next_state)
# # #                 dfs(next_state, path)
# # #                 path.pop() 
    
# # #     dfs(num_str, [num_str])
# # #     return all_paths

# # # def print_all_paths_simple(number):
# # #     paths = digit_maze_simple(number)
    
# # #     print(f"All possible paths for {number}:")
# # #     print("=" * 40)
    
# # #     for i, path in enumerate(paths, 1):
# # #         print(f"Path {i}: {' → '.join(path)}")

# # # print_all_paths_simple(123)

# # #fractal star pattern

# # n=int(input("enter n:"))
# # for i in range(n,0,-1):
# #     print("*"*i)
# # for i in range(1,n+1):
# #     print("*"*i)    

# # # ****
# # # ***
# # # **
# # # *
# # # **
# # # ***
# # # ****

# #Rotating Spiral matrix Filler

# num=input("Enter the value:")
# digits=list(num)
# print(digits)
# seen=set()
# results=[num]
# seen.add(num)
# print(seen,results)

# for i in range(len(digits)-1):
#     digits[i],digits[i+1]=digits[i+1],digits[i]
# new_num=''.join (digits)
# results.append(new_num)
# seen.add(new_num)
# print(new_num)
# for r in results:
#      print(r)



# # # input=12345
# # #output=23451


# Perfect Number Finder using only loops
for num in range(1, 10001):
    sum_div = 0
    for i in range(1, num-1):
        if num % i == 0:
            sum_div += i+
    if sum_div == num: 
         print(num,end=" ") 

    
#output
#6 28 496 8128