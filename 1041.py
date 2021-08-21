n = int(input())
A,B,C,D,E,F = map(int, input().split())
if C > D:
    C, D= D, C
if A > F:
    A, F = F, A
if B > E:
    B, E = E, B
arr = [A,B,C]
arr.sort()
a,b,c = arr[0], arr[1], arr[2]
if n == 1:
    print(A+B+C+D+E+F - max(A,B,C,D,E,F))
elif n == 2:
    print(8*a + 8*b + 4*c)
else:
    c_c = 4
    b_c = c_c + (2 * (n-2) * 4) + 4
    a_c = b_c + ((n-2)**2 + ((n-2)**2)*4 + (n-2)*4)
    print(a*a_c + b*b_c + c*c_c)
