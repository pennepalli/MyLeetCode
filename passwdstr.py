import sys

def passwordStrength(password):
    subpswd = {}
    strength = 0
    
    for i in range(len(password) - 4):
        s = password[i:i+4]
        print ("Sub: ", s)
        if s in subpswd:
            print( "S already exists")
        else:
            subpswd[s] = 1
            strength = strength+1
    return strength


if __name__ == "__main__":
    pswd = sys.argv[1]
    print("passwd strength: ", passwordStrength(pswd))
