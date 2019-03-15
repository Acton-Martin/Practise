ticket=int(input("你是否有车票？\n如果有车票请输入1，\n如果没有车票请输入0\n"))
knifeLength=int(input("请输入你的刀具的长度"))
if ticket==1:
    print("你可以进站，并开始接受安检")
    if knifeLength<=1:
        print("你的安检通过，可以进站")
    else:
        print("你的刀具违法，需要上缴你的刀具！")
else:
    print("你连车票都没有，也想坐车？")