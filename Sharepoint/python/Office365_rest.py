from office365.runtime.auth.user_credential import UserCredential
from office365.sharepoint.client_context import ClientContext
from office365.runtime.http.request_options import RequestOptions
import json
import os
import pandas as pd
from openpyxl import load_workbook
import tempfile

site_url = "siteURL"
username = "email"
password = "senha"
ctx = ClientContext(site_url).with_credentials(UserCredential(username, password))
file_url = '/sites/PLUG/Documentos Compartilhados/General/Memoria/Acompanhamento Físico Inteligente/Testes Automação Excel Sharepoint/testeLucas.xlsx'
folder_url = '/sites/PLUG/Documentos Compartilhados/General/Memoria/Acompanhamento Físico Inteligente/Testes Automação Excel Sharepoint'


#Consulta simples de API
web = ctx.web
ctx.load(web)
ctx.execute_query()
print("Web title: {0}".format(web.properties['Title'])) #OK!


#Leitura Simples
request = RequestOptions("{0}/_api/web/".format(site_url))
response = ctx.execute_request_direct(request)
json = json.loads(response.content)
web_title = json['d']['Title']
print("Web title: {0}".format(web_title))


#download de arquivos da núvem
download_path = os.path.join(tempfile.mkdtemp(), os.path.basename(file_url))
print(download_path)
with open(download_path, "wb") as local_file:
    file = ctx.web.get_file_by_server_relative_path(file_url).download(local_file).execute_query()
print("[Ok] file has been downloaded into: {0}".format(download_path))


#Tratamento do excel com a lib pandas
excel_file = download_path
df = pd.read_excel(excel_file)
df['valor'] = df['valor'].str.replace('fail','ok')
df.to_excel (excel_file, index = False, header=True)
print(df)



#Abre o arquivo baixado e captura sua informações
path = download_path
with open(path, 'rb') as content_file:
    file_content = content_file.read()
    print('OK!')

#Envia arquivo para pasta na núvem
target_folder = ctx.web.get_folder_by_server_relative_url(folder_url)
name = 'resposta.xlsx'#os.path.basename(path)
target_file = target_folder.upload_file(name, file_content).execute_query()
print("File has been uploaded to url: {0}".format(target_file.serverRelativeUrl))


# list_title = "Documentos"
# target_folder = ctx.web.lists.get_by_title(list_title).root_folder
# name = os.path.basename(path)
# target_file = target_folder.upload_file(name, file_content).execute_query()
# print("File has been uploaded to url: {0}".format(target_file.serverRelativeUrl)) OK!


#file_info = file_creation_information
# file_info = file_content
# file_info.url = download_path
# file_info.overwrite = True
# target_file = ctx.web.get_folder_by_server_relative_url(file_url).files.add(file_info)
# ctx.execute_query()



# target_folder = ctx.web.get_folder_by_server_relative_url(folder_url).files.add(file_info).execute_query()
# print(target_folder)
# ctx.execute_query()
#target_folder.upload_file(name, file_content).execute_query()
#print("File has been uploaded to url: {0}".format(target_file.serverRelativeUrl))

