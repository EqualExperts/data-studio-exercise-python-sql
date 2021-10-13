import defusedxml.ElementTree as ET

import main


def test_to_sql_over_example_data():
    example_data = '''<?xml version="1.0" encoding="utf-8"?>
<row Id="1" PostTypeId="1" AcceptedAnswerId="3" CreationDate="2016-08-02T15:39:14.947" Score="10" ViewCount="607" Body="&lt;p&gt;What does &quot;backprop&quot; mean? Is the &quot;backprop&quot; term basically the same as &quot;backpropagation&quot; or does it have a different meaning?&lt;/p&gt;&#xA;" OwnerUserId="8" LastEditorUserId="2444" LastEditDate="2019-11-16T17:56:22.093" LastActivityDate="2021-07-08T10:45:23.250" Title="What is &quot;backprop&quot;?" Tags="&lt;neural-networks&gt;&lt;backpropagation&gt;&lt;terminology&gt;&lt;definitions&gt;" AnswerCount="5" CommentCount="0" FavoriteCount="1" ContentLicense="CC BY-SA 4.0" />'''
    assert main.to_sql(ET.fromstring(example_data)) == ('1', '1', '2016-08-02T15:39:14.947')
