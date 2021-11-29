def tez(n):
    if n==0:
        return 7
    else:
        pre = tez(n-1)
        if pre % 2 == 0:
            return int(pre/2)
        else:
            return int((3*pre+1)/2)

print(tez(5))