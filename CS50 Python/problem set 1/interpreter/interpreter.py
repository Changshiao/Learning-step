x, y, z=input(" ").split(" ")

if y=="+":
    answer=float(x)+float(z)

elif y=="-":
    answer=float(x)-float(z)

elif y=="*":
    answer=float(x)*float(z)

elif y=="/":
    answer=float(x)/float(z)

print (round(answer,1))
