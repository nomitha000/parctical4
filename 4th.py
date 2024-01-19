abc=[2,32,12,43,23,54,18]
fh=open('output4.txt','w')

sum=0
i=0
while(i<len(abc)):
    sum=sum+abc[i]
    i=i+1
avg=int(sum/len(abc))
print('the average is:', avg)
fh.write(f'the average of the list is {str(avg)}')
fh.close()