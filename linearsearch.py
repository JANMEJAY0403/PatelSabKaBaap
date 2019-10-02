def linearsearch(arr,val):
    for i in range(len(arr)):
        if arr[i]==val:
            return i


# for i in range(1,9):

#     f = open("File{}.txt".format(i),"r")
#     import time
#     lst=[]
#     for l in f.readlines():
#         lst.append(int(l))
#     s=time.time()
#     linearsearch(lst,4)
#     t=time.time()
#     print((t-s)*1000)
print(' # # # # average case # # # #')
for i in range(1,9):

    f = open("File{}.txt".format(i),"r")
    import time
    lst=[]
    for l in f.readlines():
        lst.append(int(l))
    s=time.time()
    linearsearch(lst,4)
    t=time.time()
    print((t-s)*1000)

# best case
print(' # # # # best case # # # #')
for i in range(1,9):

    f = open("File{}.txt".format(i),"r")
    import time
    lst=[]
    for l in f.readlines():
        lst.append(int(l))
    lst.sort()    
    s=time.time()
    linearsearch(lst,4)
    t=time.time()
    print((t-s)*1000)


# worst case
print(' # # # # worst case # # # #')

for i in range(1,9):

    f = open("File{}.txt".format(i),"r")
    import time
    lst=[]
    for l in f.readlines():
        lst.append(int(l))
    lst.sort(reverse=True)    
    s=time.time()
    linearsearch(lst,4)
    t=time.time()
    print((t-s)*1000)
