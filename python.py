#Q1 write a function check what elements gives the target sum in the given list :
# sample test case :
# target = 9 
l = [1,2,3,4,5,8]

for i in range(len(l)):
    for j in range(i + 1 , len(l)):
        if l[i] + l[j] == 9:
            print(l[i], l[j])

