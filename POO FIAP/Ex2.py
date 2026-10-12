'''
Exercícios:

1- Atribua o valor 'Italiana' ao atributo categoria da instância restaurante_praca da classe Restaurante.

2- Acesse o valor do atributo nome da instância restaurante_praca da classe Restaurante.

3- Verifique o valor inicial do atributo ativo para a instância restaurante_praca e exiba uma mensagem informando se o restaurante está ativo ou inativo.

4- Acesse o valor do atributo de classe categoria diretamente da classe Restaurante e armazene em uma variável chamada categoria.

5- Altere o valor do atributo nome para 'Bistrô'.

6- Crie uma nova instância da classe Restaurante chamada restaurante_pizza com o nome 'Pizza Place' e categoria 'Fast Food'.

7- Verifique se a categoria da instância restaurante_pizza é 'Fast Food'.

8- Mude o estado da instância restaurante_pizza para ativo.

- Imprima no console o nome e a categoria da instância restaurante_praca.
'''

class Restaurante:
    nome = ""
    categoria = ""
    ativo = False




restaurante_praca = Restaurante();

#1.
restaurante_praca.categoria = "Italiana"
restaurante_praca.nome = "Fast Italy"

#2.
nome_restaurante = restaurante_praca.nome

#3.
if restaurante_praca.nome == "Bistrô":
    print("Restaurante Ativo!")
else:
    print("Restaurante Inativo!")

#4.

categoria = Restaurante.categoria

#5.
restaurante_praca.nome = "Bistrô"

#6.

restaurante_pizza = Restaurante()
restaurante_pizza.categoria = "Fast Food"
restaurante_pizza.nome = "Pizza Place"

#7.
if restaurante_pizza.categoria == "Fast Food":
    print("É um Fast Food")
else:
    print("Não é um Fast Food")


#8.
restaurante_pizza.ativo = True

#9.
print(f" Restaurante 1:\n Nome: {restaurante_praca.nome}\n Categoria: {restaurante_praca.categoria}\n\n Restaurante 2:\n Nome: {restaurante_pizza.nome}\n Categoria: {restaurante_pizza.categoria}")