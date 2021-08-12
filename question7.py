for T in range(int(input())):                                           #  for t in range of input
    i,a,k,c=int(input())-1,sorted(list(map(int,input().split()))),-1,0  #  sorting the list of inputs 
    while(i>0):                                                         # while is greater than 0
        if(a[i]==a[i-1]):                                               # if given condition satisfies
            k,c,i=k*a[i],c+1,i-2                                        
            if(c==2): break                                             #if equals to 2 , break
        else: i-=1                                                      # else i equals -1
    print(abs(k)) if(c==2) else print(-1)                               # print abs if cequals 2 else print -1