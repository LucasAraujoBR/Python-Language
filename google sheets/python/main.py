import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys





def Logar(login,senha):
    driver.get('https://tpfecombr.sharepoint.com/sites/PLUG/Documentos%20Compartilhados/Forms/AllItems.aspx?id=%2Fsites%2FPLUG%2FDocumentos%20Compartilhados%2FGeneral%2FMemoria%2FAcompanhamento%20F%C3%ADsico%20Inteligente%2FTestes%20Automa%C3%A7%C3%A3o%20Excel%20Sharepoint&viewid=a589f12c%2D1018%2D4002%2D9167%2Dc0fa83b56523')
    time.sleep(2)
    driver.maximize_window()
    time.sleep(2)
    login_form = driver.find_element_by_id('i0116')
    login_form.clear()
    login_form.send_keys(login)
    time.sleep(2)
    driver.find_element_by_id('idSIButton9').click()
    time.sleep(5)
    password_form = driver.find_element_by_id('i0118')
    password_form.clear()
    password_form.send_keys(senha)
    time.sleep(2)
    driver.find_element_by_id('idSIButton9').click()
    time.sleep(2)
    driver.find_element_by_id('idBtn_Back').click()
    time.sleep(2)
#switch_to_frame(WebApplicationFrame)
#.switch_to.default_content()
#/html/body/div[6]/form/div[2]/div[1]/div[2]/div[1]/div[4]/div/div[2]
#//*[@id="formulaBarTextDivId"]
def manipularExcel(celula,content):
    time.sleep(4)
    driver.find_element_by_xpath('//*/div[2]/div[2]/div/div[1]/div[1]/span/span/button').click() #Abre o excel
    time.sleep(20)
    driver.switch_to.window(driver.window_handles[1]) #Muda a janela
    raiz = driver.find_element_by_tag_name("iframe")
    print(raiz.id)
    frame_excel = driver.find_element_by_xpath('/html/body/div[1]/iframe')
    driver.switch_to.frame(frame_excel) #Entra no frame excel
    celula_pesquisada = driver.find_element_by_xpath('//*[@id="m_excelWebRenderer_ewaCtl_NameBox"]') #localiza o seletor de celula do excel
    celula_pesquisada.click()
    time.sleep(2)
    celula_pesquisada.send_keys(celula,Keys.ENTER) #insere celula escolhida
    time.sleep(1)
    escreve_excel = driver.find_element_by_xpath('//*[@id="formulaBarTextDivId"]')
    escreve_excel.click()
    escreve_excel.send_keys(Keys.CONTROL + "a")
    escreve_excel.send_keys(Keys.DELETE)
    time.sleep(1)
    escreve_excel.send_keys(content,Keys.ENTER)




def busca(celula):
    time.sleep(2)
    celula_pesquisada = driver.find_element_by_xpath('//*[@id="m_excelWebRenderer_ewaCtl_NameBox"]') #localiza o seletor de celula do excel
    celula_pesquisada.click()
    celula_pesquisada.send_keys(celula,Keys.ENTER) #insere celula escolhida
    time.sleep(2)
    content = driver.find_element_by_xpath('//*[@id="formulaBarTextDivId"]')
    conteudo_celula = content.text
    print(conteudo_celula)



def Logout():
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="O365_MainLink_Me"]/div/div[2]').click()
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="mectrl_body_signOut"]').click()
    time.sleep(10)
    driver.quit()
    


login = 'email'
senha = 'senha'
driver = webdriver.Chrome(executable_path='caminho do chromedriver')  
celula = 'f5'
content = '1591845'


Logar(login,senha)
manipularExcel(celula,content)
busca(celula)
Logout()
