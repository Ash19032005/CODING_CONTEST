# def read_input_from_file(filename):
#     with open(filename, 'r') as file:
#         # Read the total number of elements from the first line
#         n= int(file.readline().strip())
#         # Initialize an empty list to store elements
#         elements = []
#         # Read the elements in chunks
#         chunk_size = 10000  # Adjust the chunk size as needed
#         while True:
#             chunk = file.read(chunk_size)
#             if not chunk:
#                 break  # End of file
#             elements.extend(map(int, chunk.split()))
#     return n,elements
# # Example usage: Read input from a text file named "input.txt"
# n,arr = read_input_from_file("testcase13.txt")
# ans = [-1] * len(arr)
# stack=[]
# for i in range(len(arr)):
#     while stack and arr[stack[-1]]<arr[i]:
#         top=stack.pop()
#         ans[top]=arr[i]
#     stack.append(i)
# cnt=0
# for i in ans:
#     if i!=-1:
#         cnt+=1
# print(cnt)




