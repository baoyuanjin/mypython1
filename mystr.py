'''
这是一个字符串的练习
''' 
week = "星期一星期二星期三星期四星期五星期六星期天"
chose = int(input("请输入你选择的日期(0-7)：\n"))
if chose == 1:
	print("今天是",week[0:3])
elif chose == 2:
    print("今天是",week[3:6])
else:
    print("输入数字超出范围！",chose)
