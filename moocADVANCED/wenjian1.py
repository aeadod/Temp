tf=open(r'C:\Users\aeado\Desktop\f.txt','a+')

ls=['yg','zg','mg']
tf.writelines(ls)
tf.seek(0)
for line in tf :
    print(line)
tf.close()
