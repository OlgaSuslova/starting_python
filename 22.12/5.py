# Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.

from random import choice


def equations_sum(name_1: str, name_2: str):
    with open(name_1, "r", encoding="utf-8") as f_1, \
            open(name_2, "r", encoding="utf-8") as f_2:
        first = f_1.readlines()
        second = f_2.readlines()

        if len(first) == len(second):
            with open("sum.txt", "a", encoding="utf-8") as f_3:
                for i, v in enumerate(first):
                    f_3.write(f"{v[:-5]} + {second[i]}")
        else:
            print("The contents of the files do not match!")


equations_sum("1.txt", "2.txt")



#Даны два файла, в каждом из которых находится запись многочлена.
#Задача - сформировать файл, содержащий сумму многочленов.
pol1 = "12*x**8+2*x**6+2*x**4+3*x**3+2*x**2"
pol2 = "34*x**25+20*x**11+10*x**7+8*x**4+1*x**3+6*x**1+3"

pol1 = pol1.split("+")
pol2 = pol2.split("+")

print(pol1)
print(pol2)

for indx,value in enumerate(pol1):
    pol1[indx] = list(map(int,value.split("*x**")))
for indx,value in enumerate(pol2):
    pol2[indx] = list(map(int,value.split("*x**")))

print(pol1)
print(pol2)

result = pol1 + pol2
print(result)

result = sorted(result,key = lambda x: x[1] if len(x)>1 else 0,reverse=True)

print(result)
cur_indx = 0
result_list = []
while cur_indx<len(result)-1:
    cur_num = result[cur_indx]
    next_num = result[cur_indx+1]
if len(cur_num)>1 and len(next_num)>1:
    if cur_num[1] == next_num[1]:
        sum_koeff = cur_num[0]+next_num[0]
        result_list.append([sum_koeff,cur_num[1]])
        cur_indx+=1
else:
    result_list.append(result[cur_indx])
elif len(cur_num)>1 and len(next_num) == 1:
    result_list.append(result[cur_indx])
elif len(cur_num) == 1 and len(next_num) == 1:
result_list.append([cur_num[0]+next_num[0]])
cur_indx +=1
cur_indx+=1

if cur_indx < len(result):
result_list.append(result[-1])

print(result_list)
for indx,val in enumerate(result_list):
if len(val)>1:
result_list[indx] = f'{val[0]}*x**{val[1]}'
else:
result_list[indx] = f'{val[0]}'
print(result_list)
result_string = "+".join(result_list)
print(result_string)