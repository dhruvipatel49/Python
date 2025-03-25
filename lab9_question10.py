def frequency(string):
    words=string.split()
    freq={}
    for word in words:
        word=word.lower()
        freq[word]=freq.get(word,)+1
    return dict(sorted(freq.items()))
s=input("Enter the string:")
result=frequency(s)
print("Frequency of words in a string is",result)