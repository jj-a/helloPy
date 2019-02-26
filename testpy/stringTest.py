
poem = 'All that doth flow we cannot liquid name Or else would file and water be the same'
poem.replace('e', 'E')  # replace된 poem 문자열 리턴
print(poem)
print(poem.replace('e', 'E'))
# str.replace(poem, 'change string')  # Error
print(poem.replace(poem, 'change string'))  # 이게 무슨 의미가.. 있을까...