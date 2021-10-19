import os

from faker import Faker

from office365.sharepoint.client_context import ClientContext
from office365.sharepoint.lists.list_creation_information import ListCreationInformation
from office365.sharepoint.lists.list_template_type import ListTemplateType
from tests import test_team_site_url, test_user_credentials


def ensure_list(web, list_properties):
    lists = web.lists.filter("Title eq '{0}'".format(list_properties.Title)).get().execute_query()
    if len(lists) == 1:
        return lists[0]
    else:
        return web.lists.add(list_properties).execute_query()


def generate_documents(context, amount):
    """
    :type context: ClientContext
    :type amount: int
    """
    lib = ensure_list(context.web,
                      ListCreationInformation("Documents_Archive",
                                              None,
                                              ListTemplateType.DocumentLibrary))

    include_files = False

    fake = Faker()
    for idx in range(0, amount):
        # 1. Create a folder
        folder_name = fake.date()
        target_folder = lib.root_folder.add(folder_name)
        context.execute_query()
        print("({0} of {1}) Folder '{2}' has been created".format(idx, amount, target_folder.serverRelativeUrl))

        if include_files:
            # 2. Upload a file into a folder
            path = "../../../tests/data/SharePoint User Guide.docx"
            with open(path, 'rb') as content_file:
                file_content = content_file.read()
            name = os.path.basename(path)
            target_file = target_folder.upload_file(name, file_content).execute_query()
            print("File '{0}' has been uploaded".format(target_file.serverRelativeUrl))


def generate_contacts(context, amount):
    """
    :type context: ClientContext
    :type amount: int
    """
    contacts_list = ensure_list(context.web,
                                ListCreationInformation("Contacts_Large",
                                                        None,
                                                        ListTemplateType.Contacts)
                                )

    fake = Faker()
    for idx in range(0, amount):
        contact_properties = {
            'Title': fake.name(),
            'FullName': fake.name(),
            'Email': fake.email(),
            'Company': fake.company(),
            'WorkPhone': fake.phone_number(),
            'WorkAddress': fake.street_address(),
            'WorkCity': fake.city(),
            'WorkZip': fake.postcode(),
            'WorkCountry': fake.country(),
            'WebPage': {'Url': fake.url()}
        }
        #contact_item = contacts_list.add_item(contact_properties).execute_query()
        contact_item = contacts_list.add_item(contact_properties)
        print("({0} of {1}) Contact '{2}' has been created".format(idx, amount, contact_item.properties["Title"]))
    ctx.execute_batch()


if __name__ == '__main__':
    ctx = ClientContext(test_team_site_url).with_credentials(test_user_credentials)
    generate_contacts(ctx, 5000)
    #generate_documents(ctx, 100)