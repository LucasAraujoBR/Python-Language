from sharepoint import SharePoint

# set file name
file_name = 'Planejamento de Testes.xlsx'

# set the folder name
folder_name = 'General'
#General/Memoria/Acompanhamento Físico Inteligente/Testes Automação Excel Sharepoint
# get file
file  = SharePoint().download_file(file_name, folder_name)

# save file
with open(file_name, 'wb') as f:
    f.write(file)
    f.close()