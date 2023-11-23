result=[]
num_cases = int(input())
for _ in range(num_cases):
    cases = input().split()
    num_repeat = int(cases[0])
    string = cases[1]
    repeated_string = ''

    for i in range(len(string)):
        repeated_string = repeated_string + string[i] * num_repeat
        repeated_string = repeated_string.replace(" ","")
    
    result.append(repeated_string)
    
for i in range(num_cases):
    print(result[i])