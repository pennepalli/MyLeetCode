import sys

def maxval(arr):
#  arr=[4,56,7,23,52,900,323,4,5,6,56]

    n=0
    for i in arr:
        if i > n:
            n = i
    return (n)

if __name__ == "__main__":
    inarr = [int(num) for num in sys.argv[1].split(",")]
    print (maxval(inarr))

    
