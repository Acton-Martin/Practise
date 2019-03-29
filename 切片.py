a="0123456789"
print(a.find("3"))  #返回了r的索引值，确实是在3上
if "1" in a:
    print("YES")
print(a.rfind("8"))
print(a.find("8"))
print(a.index("8"))
b="abcdefg"
print(b.lower())
print(b.upper())
c="bc"
d="EFG"
print(b.replace(c,d))           #aEFGdefg