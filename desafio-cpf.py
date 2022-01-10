cpf = '168.995.350-09'
temp_cpf = ''
soma = 0
for i in range(len(cpf) - 2):
    if cpf[i].isalnum():
        temp_cpf += cpf[i]
for num in range(len(temp_cpf)):
    soma += int(int(temp_cpf[num]) * (10-num))
if 11 - (soma % 11) > 9:
    temp_cpf += '0'
else:
    temp_cpf += str(11 - (soma % 11))
soma = 0
for num in range(len(temp_cpf)):
    soma += int(int(temp_cpf[num]) * (11-num))
if 11 - (soma % 11) > 9:
    temp_cpf += '0'
else:
    temp_cpf += str(11 - (soma % 11))
cpf_original = ''
for i in cpf:
    if i.isalnum():
        cpf_original += str(i)
if cpf_original == temp_cpf:
    print('validado')
else:
    print('errado')