from collections import Counter
def frequency_map(s):
    d={}
    for i in s:
        d[i]=d.get(i,0)+1
    return d
    #return Counter(s)
if __name__ == "__main__":
    s="namaskaram"
    print(frequency_map(s))