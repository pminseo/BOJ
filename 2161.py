n = int(input())
card = []
for i in range(1, n+1):
    card.append(i)
ans = []
x=0
while len(card)>1:
    ans.append(card.pop(0))
    tmp = card.pop(0)
    card.append(tmp)
ans.append(card[0])
for j in ans:
    print(j, end=" ")