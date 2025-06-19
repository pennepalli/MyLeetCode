import sys

def reverseWords(s):
    """
    :type s: str
    :rtype: str
    """
    if (s):
        warr = s.split()
        numWords = len(warr)
    else:
        return None

    i=0 
    for i in range(numWords-1, -1, -1) :
        print (warr[i], "", end='')

if __name__ == "__main__":
    s = sys.argv[1]
    reverseWords(s)
