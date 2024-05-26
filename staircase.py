


def staircase(n):
    for i in range(1,n+1):
        slop = "#"*i
        print(slop.rjust(n))

cases = 4
staircase(cases)