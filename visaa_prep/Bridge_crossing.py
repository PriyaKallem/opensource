A,B,C=map(int,input().split())
Max_Mangoes_Wg=C-B
if Max_Mangoes_Wg<=0:
    Max_Mangoes=0
else:
    Max_Mangoes=Max_Mangoes_Wg //A
print(Max_Mangoes)
