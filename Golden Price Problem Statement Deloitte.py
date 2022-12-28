golden_price=0
def Golden_Price_Checker(dummy):
    global golden_price
    My_int=str(dummy)
    temp_list=[int(x) for x in My_int]
    highest=max(temp_list)
    add=sum(temp_list)
    sub=add-highest
    if sub == highest:
        golden_price=golden_price+int(My_int)

    else:
        pass
X,Y=input().split()
ranges=[]
for i in range(int(X),int(Y)+1):
    ranges.append(i)
    Golden_Price_Checker(i)


print(sum(ranges)-golden_price)

