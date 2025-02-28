def remove_substring(onestring, removestring):
    result = ""
    i = 0
    while i < len(onestring):
        if onestring[i:i+len(removestring)] == removestring:
            i += len(removestring)
        else:
            result += onestring[i]
            i += 1
    return result

onestring = input("Enter the main string: ")
removestring = input("Enter the string to remove: ")
finalstring = remove_substring(onestring, removestring)
print("Final string:", finalstring)