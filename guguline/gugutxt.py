#변수 선언부분
i,j,guguLine = 0,0,""

# Main Code 부분

#calc mul
for i in range(2,10):
    f = open("C:\calc\{}단.txt".format(i),'w')
    guguLine = guguLine + ("# %5d단 #\n"%i)
    f.write(guguLine)

    for j in range(1,10):
        guguLine = ""
        guguLine = guguLine + str("%2d X %2d = %2d\n"%(i,j,j*i))
        f.write(guguLine)
        
    guguLine = ""
    f.close()