from shareplum import Site, Office365
from shareplum.site import Version

import json
import os


root_dir = os.path.dirname(os.path.abspath(__file__))
config_path = '\\'.join([root_dir, 'config.json'])

# Lê json e configura o arquivo.
with open(config_path) as config_file:
    config = json.load(config_file)
    config = config['share_point']

username = config['user']
password = config['password']
sharepoint_url = config['url']
sharepoint_site = config['site']


class SharePoint:
    def auth(self):
        self.authcookie = Office365(
            sharepoint_url,
            username=username,
            password=password,
        ).GetCookies()
        self.site = Site(
            sharepoint_site,
            version=Version.v365,
            authcookie=self.authcookie,
        )
        return self.site

    def connect_to_list(self, ls_name):
        self.auth_site = self.auth()

        list_data = self.auth_site.List(list_name=ls_name).GetListItems()

        return list_data