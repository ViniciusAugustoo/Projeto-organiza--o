# definindo os numeros escolhidos 
numero1 = int(input("escolha o primeiro numero: "))
numero2 = int(input("escoha o segundo numero: "))

# criando o nome dos operadores
class operadores():
    operador = ['adicao', 'subtracao', 'multiplicacao', 'divisao']
 # criando as operações 
    def realiza_operacao(self, num1, num2):
        if escolha == 'adicao':
            return num1 + num2
        elif escolha == 'subtracao':
            return num1 - num2
        elif escolha == 'multiplicacao':
            return num1 * num2
        elif escolha == 'divisao':
            if num2 != 0:
                return num1 / num2
            else:
                return 'erro: divisao por zero nao pode'
        else:
            return "operação invalida"
        
 #mostrando as opçoes
print("1. adicao")
print("2. subtracao")
print("3. multiplcacao")
print("4. divisao")

 # escolhendo uma das opções das operaçoes 
escolha_operador = int(input("escolha um numero: "))
 # guardando as informações
operador = operadores()
 # mapeando a escolha

if escolha_operador == 1: 
    escolha = 'adicao'
elif escolha_operador == 2:
    escolha  = 'subtracao'
elif escolha_operador == 3:
    escolha = 'multiplicacao'
elif escolha_operador == 4:
    escolha = 'divisao'   
else: 
    escolha = None
 #realizando a operação eo resultado 
resultado = operadores.realiza_operacao(escolha_operador, numero1, numero2)
 #exibindo a operação

if escolha:
    print(f"voce escolheu {escolha} e o resultado é {resultado}")
else:
    print("opcao invalida")