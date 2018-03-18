# coding:utf-8
# for i in range(1,10):
#     for j in range(1,i+1):
#         s=j*i
#         print "%s*%s=%s"%(j,i,s),
#     print "\n"


list=[4,49,7,74,21]
len=len(list)
for i in range(len):
    for j in range(len-i-1):
        if list[j]>list[j+1]:
            list[j],list[j+1]=list[j+1],list[j]
print list
