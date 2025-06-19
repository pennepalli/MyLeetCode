#!/usr/bin/python3

import sys


def bigsum(str1, str2):
    l1 = len(str1)
    l2 = len(str2)

    if (l1 >= l2):
        slen = l1
        rlen = l1-l2
    else
        rlen = l2

    carryover = 0
    for i in range(rlen, 0, -1):
        m = int(str1[i-1])
        if (l2 >= l1):
            n = int(str2[i-1])
        else:
            n = 0
        nc =  (m+n+carryover)//10
        ans = (m+n+carryover)%10
        carryover = nc
        print ("i=",i, "m=",m, "n=",n, "newCarryover=",nc, "Ans=",ans)
    if (l2 > l1):
        for i in range(l2-l1,0,-1):
            m = 0
            n = int(str2[i-1])
            nc =  (m+n+carryover)//10
            ans = (m+n+carryover)%10
            carryover = nc
            print ("i=",i, "m=",m, "n=",n, "newCarryover=",nc, "Ans=",ans)

        # print ("i=",i, str1[rlen-i], str2[rlen-i])

    return str1 + ":" + str2


if __name__ == "__main__":
    v1 = sys.argv[1]
    v2 = sys.argv[2]

    bisum =  bigsum(v1,v2)
    print ("BigSum: ", bisum)


