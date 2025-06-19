import sys

def myAtoi(s):
    """
    :type s: str
    :rtype: int
    """
    negate=1
    n=0
    print ("S before strip: ", s)
    s = s.lstrip()
    print ("S after strip: ", s)

    if s and ( s[0] == '+' or s[0]=='-' ) :
        if (s[0] == '-'):
            negate=-1
        s=s[1::]


    i=0
    for c in s:
        print ("C= ", c)
        if (c.isdigit()) :
            nval = int(c)
            n = n * 10 + nval
            print ("Nval= ", nval)
            i=i+1
        else :
            print ("Invalid digit")
            break
    n = n * negate
    print ("N = ", n)

    INT_MAX = 2**31 - 1
    INT_MIN = -(2**31)

    if n > INT_MAX:
        return INT_MAX
    if n < INT_MIN:
        return INT_MIN

    return n
                

if __name__ == "__main__":
    inpstr = sys.argv[1]
    r = myAtoi(inpstr)
    if (r < 0):
        print ("Return -ve number: ", r)
    else:
        print ("Return +ve number: ", r)


