
import sys

def remdups(inparr):
    n=None
    result=[]
    for f in inparr:
        if ( f != n ):
            result.append(f)
        n = f
    return result

if __name__ == "__main__":
    inarr = [int(num) for num in sys.argv[1].split(",")]
    print (remdups(inarr))
       
                
