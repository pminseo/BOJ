n = int(input())
 
alice = []
bob = []
none = []
a_c = 0
b_c = 0
n_c = 0
ans = 0
 
for _ in range(n):
    group = input().split()
    ans += int(group[1])
    if group[0] == '11':
        a_c += 1
        b_c += 1
    elif group[0] == '10':
        alice.append(int(group[1]))
        a_c += 1
    elif group[0] == '01':
        bob.append(int(group[1]))
        b_c += 1
    else:
        none.append(int(group[1]))
        n_c += 1
a_n = alice + none
b_n = bob + none
a_n.sort(reverse=True)
b_n.sort(reverse=True)
 
none.sort(reverse=True)
print(len(alice), len(bob), len(none))
 
while a_c * 2 < n or b_c * 2 < n:
    if a_c < b_c:
        sub = b_n.pop()
        if sub in bob:
            b_c -= 1
        ans -= sub
        n -= 1
 
    elif a_c > b_c:
        sub = a_n.pop()
        if sub in alice:
            a_c -= 1
        ans -= sub
        n -= 1
 
    elif a_c == b_c:
        sub = none.pop()
        ans -= sub
        n -= 1
print(ans)