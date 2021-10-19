
from upload_and_delete import SharePoint

#i.e - file_dir_path = r'C:\project\report.pdf'
file_dir_path = r'C:\Users\Lucas Araújo\Documents\Pasta config git\Sharepoint'

# this will be the file name that it will be saved in SharePoint as 
file_name = 'teste.csv'

# The folder in SharePoint that it will be saved under
folder_name = 'Teste'

# upload file
SharePoint().upload_file(file_dir_path, file_name, folder_name)

# delete file
SharePoint().delete_file(file_name, folder_name)