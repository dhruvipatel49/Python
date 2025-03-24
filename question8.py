def convert(string):
    words=string.split()
    unique_words=set(words)
    sorted_words=sorted(unique_words)
    result=' '.join(sorted_words)
    return result
str=input("Enter the string:")
check=convert(str)
print(check)