'Entrypoint to populate the database'
import defusedxml.ElementTree as ET


def to_sql(post):
    return (post.attrib['Id'], post.attrib['PostTypeId'], post.attrib['CreationDate'])


with open('uncommitted/Posts.xml', 'r') as posts_in:
    tree = ET.parse(posts_in)
    print([to_sql(elem) for elem in tree.getroot()][:10])
