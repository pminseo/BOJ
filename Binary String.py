K = int(input())
S = input()

num = int(S, 2)
count = 0
while K < num:
    S = list(S)
    for i in range(len(S)-1):
        if S[i+1] == '1':
            del S[i+1]
            count += 1
            break
        if i == len(S)-2:
            del S[i]
            count += 1
            break
    S = ''.join(S)
    num = int(S,2)

print(count)