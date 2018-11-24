#daydayup


def gongzuori(df):
    dayup=1
    for i in range(365):
        if i %7 in[6,0]:
            dayup=dayup*(1-0.01)
        
        else:
            dayup=dayup*(1+df)
        
    return dayup


df=0.01

while gongzuori(df)<pow(1.01,365):
    df+=0.001

print("{:.3f}".format(df))

