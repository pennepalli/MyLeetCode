import sys

def wordFreq(filename):

    maxfreq=0
    maxfreqword=""
    freq = {}

    try:
        with open(filename, 'r') as file:
            for line in file:
                for word in line.split():
                    # print (word)
                    if word in freq:
                        freq[word]=freq[word]+1
                    else:
                        freq[word]=1

                    if maxfreq < freq[word] :
                        maxfreq = freq[word]
                        maxfreqword = word

    except FileNotFoundError:
        print(f"Error: File not found: {filename}")
        return None,None

    return maxfreqword, maxfreq


if __name__ == "__main__":
    fn = sys.argv[1]
    w,n = wordFreq(fn)
    print ("MaxFreqWord: ", w, " Count: ", n)
    # print ("MaxFreqWord: ", w,)


