from sharepoint import SharePoint


clients = SharePoint().connect_to_list(ls_name='Documentos')

print(clients)