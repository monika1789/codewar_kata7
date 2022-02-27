# Given a number N, can you fabricate two numbers NE and NO such as NE is formed by even digits of N and NO is formed by odd digits of N? Examples:

# 126453 -> NE = 264, NO = 153
# 3012 -> NE = 2, NO = 31
# 4628 -> NE = 4628, NO = 0 0 is considered as an even number.

def even_and_odd(n): 
    n=str(n)
    NE=' '
    NO= ' '
    for  i in n:
        if int(i) == 0:
            NE += i
        elif int (i) %2==0:
            NE+=i 
        elif int(i) % 2==1:
            NO+=i
    if NO == ' ':
        NE=int(NE) 
        NO=0
        return (NE,NO)
    elif NE == ' ' :
        NO=int(NO)
        NE=0
        return (NE, NO) 
    else:
        NE =int(NE)
        NO= int(NO)
        return (NE,NO)  