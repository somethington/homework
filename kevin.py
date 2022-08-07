
import pandas as pd
import re
source = pd.read_csv('https://raw.githubusercontent.com/somethington/homework/kevinttest/test.csv', encoding= 'unicode_escape')

columns_of_interest = []
columns_of_interest_dsub = []
d_list = []
for char in "ABCD":  #generates list of 
    for i in range(1,13): 
        columns_of_interest.append(char + str(i)) 
for char in "ABC":  
    for i in range(1,13): 
        columns_of_interest_dsub.append(char + str(i)) 

columns_of_interest_dsub.sort(key=lambda test_string : list( #sorts list of samples
    map(int, re.findall(r'\d+', test_string)))[0])

columns_of_interest.sort(key=lambda test_string : list( #sorts list of samples without D
    map(int, re.findall(r'\d+', test_string)))[0])

print(columns_of_interest)
for i in range(1,13):
    d_list.append("D" + str(i))

index_advance = []
for i in range(2, len(columns_of_interest_dsub), 3):
    index_advance.append(i)

index_c = 0
index_d = 0
lst_d_sub_columns = []
while index_c < len(columns_of_interest_dsub): #subtracts D[x] from respective group of samples
    source[str(columns_of_interest_dsub[index_c]) + "-D"] = source[columns_of_interest_dsub[index_c]] - source[d_list[index_d]]
    lst_d_sub_columns.append(str(columns_of_interest_dsub[index_c]) + "-D")
    if index_c in index_advance:
        index_d += 1
    if index_d == len(d_list):
        break
    index_c += 1
    
for i in range(0, len(lst_d_sub_columns)):
    source[lst_d_sub_columns[i] + " mean"] = source[lst_d_sub_columns[i]].mean()

source.to_csv("curiosity.csv")

                




