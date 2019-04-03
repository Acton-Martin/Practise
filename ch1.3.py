f=-34.814   #-34.81
g=723.126   #723.13
print(format(f,'+0.2f'))
print(format(g,'+0.2f'))
president = dict(washington=(1789, 1797), adams=(1797, 1801))
for key in president:
	print("%s:%d-%d" %(key,president[key][0],president[key][1]))
info = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
b = []
# for index,i in enumerate(info):
#     print(i+1)
#     b.append(i+1)
# print(b)
for index, i in enumerate(info):
    info[index] +=1
print(info)