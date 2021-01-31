a = input()
b = a.find('(')
c = a.find(')')
d = a[b - 1:c + 1]
e = a.replace(d,'')
print(e[:-1], d, e[-1], sep = "")
