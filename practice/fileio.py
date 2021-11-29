# read text file 
'''
f  = open('fileio.py','r')

print(f.read())

f.close()
'''

f = open("squares.txt","w")

for i in range(10,20):
    square = i * i
    f.write(f'{i}^2 = {square}\n')

f.close()

t = open("smile.gif","rb")
t1 = open("smilecopy.gif",'wb')
t1.write(t.read())
t1.close()
t.close()
