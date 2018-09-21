def countvowel():
    s = input('Enter the string: ')
    x = ['a', 'e', 'i', 'o', 'u']
    unduplicate = set(s)
    duplicate_count = len(s)- len(unduplicate)
    count=''
    for char in x:
        if char in s:
             count += str(char)
    print((count,duplicate_count))
countvowel()