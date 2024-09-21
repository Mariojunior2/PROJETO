Value1 = int(input("Valor 1 "))
Value2 = int(input("Valor 2 "))

for i in range(Value1,Value2):
    if Value2 > Value1:
        Newvalor = Value2 - Value2 + Value1 - 10
        print("Os valores sao", Value1, Newvalor)
if Value2 < Value1:
    print("Os valores sao", Value1, Value2)
