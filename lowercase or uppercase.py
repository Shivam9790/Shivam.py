ch=input('enter a single character:')
if ch>='A' and ch<= 'Z': 
    print(ch,'is a uppercase character ')
elif ch>='a' and ch<= 'z':
    print(ch, 'is a lowercase character')
elif ch>='0' and ch<='9':
    print(ch,'is a digit')
else :
    print(ch,'as other character')
