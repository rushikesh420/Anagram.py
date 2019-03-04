def freq(word):
    frequency = {}
    for char in word:
        if char in frequency:
            frequency[char]=frequency[char]+1
        else:
            frequency[char]=1
    return frequency
def is_twin(a, b):
    a=a.lower()
    b=b.lower()
    if (len(a) != len(b)):
        return False
    else:
        if (freq(a)==freq(b)):
            return True
        else: 
            return False
