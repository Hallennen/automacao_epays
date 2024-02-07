from selenium import webdriver
from selenium.webdriver.common.by import By
import time , glob, os, shutil, getpass



print('\n\n \t\t Para realizar a extração informe os dados abaixo. \n\n\n ')

user= input('Informe o login de acesso ao Epays: ')
password = getpass.getpass('Informe a senha de acesso ao Epays: ',stream='*')
mes_ano_de_validacao = input('informe o mês da extração: (EX: JAN)  ').upper()
ano_validacao= input('Informe o ano da extração:  (EX: 2024)  ')
numero_de_paginas = int(input('Informe o numero de páginas que devem ser validadas:  (EX: 5)  '))
print('tentando')

# '36525576890'
# '40471178'



def processo():

    #logar na pagina
    driver.find_element('xpath', '//*[@id="cpf"]').send_keys(user)
    driver.find_element('xpath', '//*[@id="login-form"]/div[4]/div/input').send_keys(password)
    time.sleep(1.5)

    #botao logar 
    driver.find_element('xpath', '//*[@id="login-form"]/div[5]/action-button/button').click()
    time.sleep(3)


    #opção gestor
    driver.implicitly_wait(30)
    driver.find_element('xpath', '/html/body/app-root/auth/app-select-profile-view/external-view/div/div/div/main/form/div/div[3]/action-button[1]/button').click()
    time.sleep(2)


    #opção confirmar
    driver.implicitly_wait(30)
    driver.find_element('xpath', ' /html/body/app-root/auth/app-select-profile-view/external-view/div/div/div/main/form/div/div[4]/action-button/button').click()



    #oção pontofrag
    driver.implicitly_wait(30)
    time.sleep(2)
    driver.find_element('xpath', '/html/body/app-root/app-gestor/internal-view/div/main/div/div/app-home/div/div/div[2]/navigation-menu/div/navigation-item[6]/div').click()
    time.sleep(2)

    #espelho de ponto
    driver.find_element('xpath', '/html/body/app-root/app-gestor/internal-view/div/main/div/div/integration-pontofopag-menu/div/div/div/div[1]').click()


driver = webdriver.Edge(executable_path='msedgedriver.exe')
driver.get('https://app.epays.com.br/login')
driver.implicitly_wait(30)
processo()

#looping aqui
def ler_elementos_pagina():
    global nome_do_atendente
    
    for i in range(10):
        i= i+1 
        driver.implicitly_wait(30)
        nome_do_atendente = driver.find_element('xpath', f"/html/body/app-root/app-gestor/internal-view/div/main/div/div/app-integration-pontofopag-list/div/div/integration-pontofopag-card[{i}]/div/div[1]/div[1]").text
        Mes_ano =driver.find_element('xpath', f"/html/body/app-root/app-gestor/internal-view/div/main/div/div/app-integration-pontofopag-list/div/div/integration-pontofopag-card[{i}]/div/div[2]/div").text

        mes_ano_de_validacao_completo = (mes_ano_de_validacao + ' / ' + ano_validacao)
        if Mes_ano == mes_ano_de_validacao_completo:
            print('NOME' ,nome_do_atendente )
            print('mes/ano:', Mes_ano)
            print('Mes igual informado')
            try:
                driver.find_element('xpath', f'/html/body/app-root/app-gestor/internal-view/div/main/div/div/app-integration-pontofopag-list/div/div/integration-pontofopag-card[{i}]/div/div[4]/div/action-button[2]').click()
                time.sleep(15)
                print('baixou')
                renomear_arquivo(nome=nome_do_atendente)
            except:
                print('não foi 😢')
            
        else:
            print()



def renomear_arquivo(nome):
    print('renomeando')
    #copia da pasta download
    pasta_download = glob.glob('passar o caminho da pasta Download/*')
    ultimo_arquivo_download = max(pasta_download, key=(os.path.getmtime))

    #cola na pasta atendentes
    pasta = 'passar o caminho da pasta onde deseja colar o arquivo copiado'
    copia = shutil.copy(ultimo_arquivo_download,pasta )


    base_pasta = pasta+'/'
    
    
    #renomeia para o nome do atendente
    pasta_atendentes = glob.glob('o caminho da pasta onde foi colocado o arquivo copiado + /*')
    ultimo_arquivo_atendente = max(pasta_atendentes, key=(os.path.getmtime))
    renomear = os.rename(ultimo_arquivo_atendente, base_pasta + nome + '.pdf')

    return print('renomeado\n\n')




def proxima_pagina():
    print('Avançando para a próxima pagina')
    driver.find_element('xpath', '/html/body/app-root/app-gestor/internal-view/div/main/div/div/app-integration-pontofopag-list/div/div/pagination-navigation/nav/ul/li[8]/a').click()





for i in range(numero_de_paginas): 
    i+1
    ler_elementos_pagina()
    proxima_pagina()

input("Varredura completa, consulte os arquivos na pasta 'Que voce informou na variavel (pasta)' ")

