a = input("Input file's name")
b = input("Input new expansion")
c = a.rfind(".")
res = ""
dot = "."
k = -1
result = 0
l = len(a.split("."))
print(c, l)
if c < 0:
    res = a + dot + b
    print(res)
else:
    g = a.split(".")
    for i in range(l):
        result += g[k+1] + dot + b
    print(result)