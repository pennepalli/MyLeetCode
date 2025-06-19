import sys

def twosum(inparr, tsum):
    n=1
    for i,f in enumerate(inparr[:-1]):
        clist = inparr[n:]
        # print (f, clist)
        for j,g in enumerate(clist):
            # print("f:", f, " g:", g)
            if ( f + g == tsum):
                print("f:", f, " g:", g)
                return i,n+j
        n=n+1
    return -1,-1

if __name__ == "__main__":
    inarr = [int(num) for num in sys.argv[1].split(",")]
    insum = int(sys.argv[2])
    p1,p2 = twosum(inarr, insum)
    print("Pos1: ", p1, " Pos2: ", p2);
       
                
