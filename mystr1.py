'''第二个练习'''
str1 = input("请输入一个字符串：")
i = 0
print("原来的字符串为：\n",str1)
print("转换过后的字符串为:\n")    
while i < len(str1):
    if ord('a')<=ord(str1[i])<=ord('z'):
    	print(chr(ord(str1[i])-(ord('a')-ord('A'))))
    else:
    	print(chr(ord(str1[i])+(ord('a')-ord('A'))))
	
    i=i+1
     
