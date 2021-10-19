from shareplum import Site
from shareplum import Office365
from shareplum.site import Version

authcookie = Office365('url', username='email', password='senha').GetCookies()
site = Site('caminho', version=Version.v365, authcookie=authcookie)
folder = site.Folder('Shared Documents/This Folder')
print(folder)
folder.upload_file('Hello', 'new.txt')
folder.get_file('new.txt')
folder.check_out('new.txt')
folder.check_in('new.txt', "My check-in comment")
folder.delete_file('new.txt')