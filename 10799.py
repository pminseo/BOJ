char = list(input())
num = 0
ans = 0
char.append('.')
for i in range(len(char)):
    if char[i] == '(':
        num += 1
        if char[i+1] == ')':
            num -= 1
            ans += num
    elif char[i] == ')':
        num -= 1
        if char[i-1] == '(':
            num += 1
        elif char[i-1] == ')':
            ans += 1
           
print(ans)