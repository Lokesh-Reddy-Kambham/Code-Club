lst=[1,2,3,4,5,6,7,9,10]
start=0
end=len(lst)-1
while start < end:
    lst[start],lst[end]=lst[end],lst[start]
    start=start+1
    end=end-1
    print(lst)