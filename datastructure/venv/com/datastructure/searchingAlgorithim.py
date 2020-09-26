arr=[10,20,30,40,50,60,70,80,90,100]
x=40
def binarysearch(arr,x,l,r):
    if r >= l:
        mid=(l+r)//2
        if arr[mid]==x:
            return mid
        elif arr[mid] >x:
            return binarysearch(arr,x,l,mid-1)
        else:
            return binarysearch(arr,x,mid+1,r)
    else :
        return  -1

print(binarysearch(arr,20,0,len(arr)-1))