import defusedxml.ElementTree as ET


def is_valid_post(post):
    return post['']


with open('uncommitted/Posts.xml', 'r') as badges_in:
    tree = ET.parse(badges_in)
    print([elem.attrib for elem in tree.getroot()][:10])
