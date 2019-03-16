i=1
while i<=9:
    j=1
    while j<=i:                                #使用的j小于i来控制的列。
        print("%d*%d=%d\t"%(j,i,j*i),end="")   # \t是制表符的意思，使其对齐
        j+=1
    print("")
    i+=1