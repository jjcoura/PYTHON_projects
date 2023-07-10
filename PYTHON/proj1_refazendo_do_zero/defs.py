import os
from valida import *
from datetime import datetime

def limpaTerminal():
    return os.system('cls' if os.name == 'nt' else 'clear')


def linha():
    return '-' * 32

data = datetime.now()
dia = data.day
mes = data.mouth
ano = data.year


def menu():
    print(' ======== <<< \033[1;36m "LOJA LEGAL" \033[m >>> ====== ')
    print('| \033[1;36m[1]\033[m \033[1;35m    -      Cadastrar Cliente    \033[m|')
    print('| \033[1;36m[2]\033[m \033[1;35m    -      Dados do Cliente     \033[m|')
    print('| \033[1;36m[3]\033[m \033[1;35m    -      Mostrar Clientes     \033[m|')
    print('| \033[1;36m[4]\033[m \033[1;35m    -      Gerar Relatório      \033[m|')
    print('| \033[1;36m[0]\033[m \033[1;35m    -      Sair                 \033[m|')
    linha()
    x = input('\033[1;36mDigite uma das opções acima: \033[m')
    linha()
    return x
    
    
def cadastro():
    limpaTerminal()
    print('=== < \033[1;92m        CADASTRAR USUÁRIO\033[m       > ===')
    nome = nome()
    login = login()
lerlogins = open('logins.txt', 'r')
for l in lerlogins.readlines():
    valores = l.split('-') 
    if login == valores[1].split(':')[1].strip():
        limpaTerminal()
        linha()
        print('033[31mLogin Existente!\033[m')
        linha()
    lerlogins.close()
    senha = senha()
    email = email()
    data = data()
    cel = cel()
    endereco = endereco()
    limpaTerminal()
    linha()
    print('Cliente cadastrado com sucesso!')
    linha()
    logins = open('logins.txt', 'a')
    logins.write(f'Nome: {nome} - Login: {login} - Senha: {senha} - Email: {email} - Data de nascimento: {nascimento} - Número de celular: {cel} - Endereço: {endereco}\n')
    logins.close()
    
    
def mostrarDados():
    limpaTerminal()
    print('=== < \033[1;92m        DADOS DO CLIENTE\033[m       > ===')
    linha()
    print('\033[1;31mlogue para acessar os seus dados!\033[m ')
    linha()
    userlogin = input('Login: ')
    usersenha = input('Senha: ')
    validar = False
    logins = open('logins.txt', 'r')
    for l in logins.readlines():
        valores = l.split('-')
        if userlogin == valores[1].split(':')[1].strip and usersenha in valores[2].strip():
            limpaTerminal()
            linha()
            print('\033[1;32mCliente Logado! Dados do usuário:\033[m')
            linha()
            for p in range(len(valores)):
                if valores[p].split(':')[0] == 'Endereço':
                    dictEndereço = eval(valores[p].split('Endereço: ')[1])
                    for chave in dictEndereço:
                        print(f'{chave: {dictEndereço[chave]}}')
                else:
                    print(valores[p])
            linha()
            validar = True
            logins.close()
            break
    if not validar:
        limpaTerminal()
        linha()    
        print('\033[1;31mERRO! logoin ou senha inválidos!\033[m')
        linha()
        
        
def clientesCadastrados():
    limpaTerminal()
    print('=== < \033[1;92m        CLIENTES CADASTRADOS\033[m       > ===')   
    logins = open('logins.txt', 'r')
    for l in login.readlines():
        l = linha.split('-')
        print(f'\033[1;92m]{l[0]} | {l[1]}\033[m') 
    linha()  
    return


def relatorio():
    cc = 0
    nomess = []
    logins = open('logins.txt', 'r')
    for linhas in logins.readlines():
        l = linhas.split('-')
        nomess.append(l[0])
        cc += 1
    arquivo = open('dados.txt', 'w+')
    arquivo.write('Relatório de Clientes\n')
    arquivo.write(f'A loja legal possui {cc} clientes(s)\n')
    for i in range(len(nomess)):
        arquivo.write(str(f'{i + 1}.{nomess[1].split(":")[1]}\n'))
    arquivo.write(f'Dados, {dia}/{mes}/{ano}.')
    linha()
    print('\033[1;32mRelatorio gerado em "dados.txt"\033[m')
    linha()
    arquivo.close()
    return        
    