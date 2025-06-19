import sys

def addTwoNumbers(l1, l2):
    """
    :type l1: Optional[ListNode]
    :type l2: Optional[ListNode]
    :rtype: Optional[ListNode]
    """
    j=0
    n=0
    # for i in l1[::-1]:
    l_l1 = [int(num) for num in l1.split(",")]
    for i in l_l1:
        print ("j: ", j, " i: ", i)
        n = n + i * (10**j)
        j=j+1
    
    m = 0
    j = 0
    l_l2 = [int(num) for num in l2.split(",")]
    for i in l_l2:
        print ("J: ", j, " i: ", i)
        m = m + i * 10**j
        j = j+1

    return m+n


if __name__ == "__main__":
    # inarr1 = [int(num) for num in sys.argv[1].split(",")]
    inarr1 = sys.argv[1]
    # inarr2 = [int(num) for num in sys.argv[2].split(",")]
    inarr2 = sys.argv[2]
    val = addTwoNumbers(inarr1, inarr2)
    print("Sum: ", val)

