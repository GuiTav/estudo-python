
# Conversão de tipo implícita: O programador não precisa declarar a conversão

peso = 60 # Int
print(peso, type(peso))
altura = 1.72 # Float
total = peso * altura # Como a altura é um float, o peso é transformado em float também para a realização do cálculo
print(total, type(total))


# Conversão explícita: O programador declara a conversão

soma = 13.45 + float("12.5") # O literal do tipo string é transformado em um float para que seja realizado o cálculo
#conversao = float("abc") # Nem sempre é possível converter um valor para outro tipo

print(f"Em uma interpolação, a conversão para o tipo string é feita automáticamente, olha: {altura} {type(altura)}")