#day.py
months='星期一星期二星期三星期四星期五星期六星期日'
n=input("请输入数字")
pos=(int(n)-1)*3
monthAbbrev=months[pos:pos+3]
print("今天是"+monthAbbrev+"。")
