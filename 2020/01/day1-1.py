

input_file = open("2020/day1.input", "r")
content_list = input_file.readlines()

for i in range(0, len(content_list)): 
    content_list[i] = int(content_list[i]) 

result1 = 0 
result2 = 0

for i in range(0, len(content_list)): 
    for j in range(0, len(content_list)):
        if (i != j and (content_list[i] + content_list[j]) == 2020):
            result1 = content_list[i]
            result2 = content_list[j]
            break

print(result1 * result2)