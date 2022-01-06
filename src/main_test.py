"""
Perform total record count test between input file and database
"""


import xml.etree.ElementTree as ElemTree
import sqlite3

FINAL_SCHEMA = []
OUT_DATA_PATH = 'xml_in_out/data_warehouse/'
IN_FILE_PATH = 'xml_in_out/stackexchange_dataset/'
ABS_DB_PATH = OUT_DATA_PATH + 'large_dataset.db'
TABLE_LIST = ['staging_posts', 'staging_tags']
FILE_LIST = ['Posts.xml', 'Tags.xml']



def test_results(file_name, table_name):
    """
    test method for result validation
    :return:
    """

    with sqlite3.connect(ABS_DB_PATH) as connection:
        db_cursor = connection.cursor()
    db_cursor.execute(f"select count(*) from {table_name}")
    rows = db_cursor.fetchone()

    total_file_name = IN_FILE_PATH + file_name
    xml_data = ElemTree.iterparse(total_file_name)
    count = 0
    for event, data in xml_data:
        if list(data.attrib.keys()):
            count = count + 1

    debug_text = f"Rows inserted: {rows[0]} and actual: {count}"
    print(debug_text)
    assert count == rows[0], 'Number of rows inserted do not match'


for iter_idx, table in enumerate(TABLE_LIST):
    test_results(FILE_LIST[iter_idx], TABLE_LIST[iter_idx])
