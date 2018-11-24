h,w=list(map(eval ,input().split()))
bmi=w/(h**2)
print("{:.2f}".format(bmi))
if bmi<18.5:
    nat,chi='shou','shou'
elif 18.5<=bmi<24:
    nat,chi='ok','ok'
elif 24<=bmi<25:
    nat,chi='ok','pang'
elif 25<=bmi<28:
    nat,chi='pang','pang'
elif 28<=bmi<30:
    nat,chi='pang','aaaaa'
elif 30<=bmi:
    nat,chi='aaaa','aaa'
print("{},{}".format(nat,chi))
