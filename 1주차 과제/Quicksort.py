import sys
arr = []


for i in range(4,len(sys.argv)):
   arr.append(int(sys.argv[i]))

def Quicksort(arr,Left,Right) :
        L=Left
        R=Right
        M=int((Left + Right) / 2)
        pivot=arr[M]

        while L<=R :
         while arr[L]<pivot :
             L+=1
            
         while arr[R]>pivot:
             R-=1

         if L<=R:
            if L!=R:
                temp=arr[L]
                arr[L]=arr[R]
                arr[R]=temp

            L=L+1
            R=R-1  

        if Left<R:
            Quicksort(arr,Left,R)

        if L<Right:
            Quicksort(arr,L,Right)     


def Quicksort2(arr,Left,Right) :
        L=Left
        R=Right
        M=int((Left + Right) / 2)
        pivot=arr[M]

        while L<=R :
         while arr[L]>pivot :
             L+=1
            
         while arr[R]<pivot :
             R-=1

         if L<=R:
            if L!=R:
                temp=arr[L]
                arr[L]=arr[R]
                arr[R]=temp

            L=L+1
            R=R-1  

        if Left>R:
            Quicksort(arr,Left,R)

        if L<Right:
            Quicksort(arr,L,Right)


if sys.argv[1]=="-o" and sys.argv[2]=='A' and sys.argv[3]=="-i" :
  Quicksort(arr,0,len(arr)-1)
  print(arr)

if sys.argv[1]=="-o" and sys.argv[2]=='D' and sys.argv[3]=="-i" :
    Quicksort(arr,0,len(arr)-1)
    arr.reverse()
    print(arr)