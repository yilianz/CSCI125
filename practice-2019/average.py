# Find the lowest score: input-list output -- lowest
def lowestS(mylist):
    smallestSofar = mylist[0]
    for num in mylist:
        if num < smallestSofar:
            smallestSofar = num
    return smallestSofar

# Calculate the average after drop the lowest score:
#  input -list output-average 
def average(mylist):
    sum = 0
    for num in mylist:
        sum +=num
    return (sum-lowestS(mylist))/(len(mylist)-1)

# test  -- done !
# print(lowestS([10,9,10]))
def cleanD(rawdata):
    goodData = []
    for data in rawdata:
        ndata = int(data[:-1])
        goodData.append(ndata)
    return goodData

# read data from the files : filename ---> list
f = open('score1.txt','r')
myrawscore = list(f)
myscore = cleanD(myrawscore)
print(average(myscore))
f.close()