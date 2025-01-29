#escolhendo o numero para contabilizar
numero1 = int(input('digite o primeiro numero: ') )
numero2 = int(input('digite o segundo numero: ') )

# criando o nome dos operadores
class operadores():
    operador = ["adicao", "subtracao", "multiplicacao", "divisao"]
    # criando as operações 
    def realiza_operacao(self, num1, num2):
        if escolha == 'adicao':
            return (num1 + num2)
        elif escolha == 'subtracao':
            return (num1 - num2)
        elif escolha == 'multiplicacao':
            return (num1 * num2)
        elif escolha == 'divisao':
            if num2 != 0:
             return num1 / num2
            else:
                return " erro: divisao por zero nao existe"
        else:
            return "operação invalida"
        #mostrando as opçoes
print("escolha um operador: ")
print("1. adicao")
print("2. subtracao")
print("3. multiplicacao")
print("4. divisao")
# escolhendo uma das opções das operaçoes 
escolha_numero = int(input("digite um numero correspondente: "))
# guardando as informações
operador = operadores()
# mapeando a escolha
if escolha_numero == 1:
    escolha = 'adicao'
elif escolha_numero == 2:
    escolha = 'subtracao'
elif escolha_numero == 3:
    escolha = 'multiplicacao'
elif escolha_numero == 4:
    escolha = 'divisao'
else:
    escolha = None

#realizando a operação eo resultado 

resultado = operadores.realiza_operacao (escolha_numero, numero1, numero2)

#exibindo a operação
if escolha:
    print(f"voce escolheu {escolha} e o resultado é {resultado}")
else:
    print("opcao invalida")