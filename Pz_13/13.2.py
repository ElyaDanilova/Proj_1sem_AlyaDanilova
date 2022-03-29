import string

s = '--msg-template="$FileDir$\{path}:{line}:{column}:{C}:({symbol}){msg}'
zs = list()
for i in s:
    for d in string.punctuation:
        if i == d:
            zs.append(i)
print(s)
print(" ".join(zs))