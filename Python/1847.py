A,B,C = list(map(int, input().split()))

if B < A and C >= B:
    print(':)')
elif B > A and C <= B:
    print(':(')
elif B > A and C > B and C-B < B-A:
    print(':(')
elif B > A and C > B and C-B >= B-A:
    print(':)')
elif B < A and C < B and C-B > B-A:
    print(':)')
elif B < A and C < B and C-B <= B-A:
    print(':(')
elif A == B:
    if C > B:
        print(':)')
    else:
        print(':(')
