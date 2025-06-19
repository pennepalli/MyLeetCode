
import sys

def addNumbers(n):
    
    i = n
    while (i > 9):
        k = i
        modsum = 0
        while (k > 0):
            modsum = modsum + k % 10
            k = k // 10
        i = modsum
    return i



if __name__ == "__main__":
    s = int(sys.argv[1])
    print ("AddNumbers: ", addNumbers(s))

