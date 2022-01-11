"""
Module to read large xml files batchwise and store into a given sqlite db
"""


import xml.etree.ElementTree as ElemTree
import sqlite3

FINAL_SCHEMA = []
OUT_DATA_PATH = 'xml_in_out/data_warehouse/'
IN_FILE_PATH = 'xml_in_out/stackexchange_dataset/'
ABS_DB_PATH = OUT_DATA_PATH + 'large_dataset.db'
TABLE_LIST = ['staging_posts', 'staging_tags']
FILE_LIST = ['Posts.xml', 'Tags.xml']


def create_database(abs_db_path, file_list, table_list, schema_input):
    """
    Drop and define tables at given db path, returns nothing
    """
    with sqlite3.connect(abs_db_path) as db_connection:
        db_cursor = db_connection.cursor()

    for table_name in table_list:
        db_cursor.execute(f"DROP TABLE IF EXISTS {table_name}")
    for idx in range((len(file_list))):
        schema = ','.join([x + ' text' for x in (schema_input[idx])])
        create_table_query = f"CREATE TABLE IF NOT EXISTS {TABLE_LIST[idx]} ({schema})"
        db_cursor.execute(create_table_query)


def build_schema(input_file):
    """
    Iterate through files and capture needed schema for data storage
    :param input_file:
    :return:
    """
    abs_file_path = IN_FILE_PATH + input_file
    xml_iter = ElemTree.iterparse(abs_file_path)
    module_called = 0
    elem_list = []
    temp_storage_schema = []
    counter = 1


    for event, elem in xml_iter:
        counter = counter + 1
        elem_list.extend(elem.attrib.keys())

        if (counter % 10000) == 0:
            module_called = module_called + 1
            temp_storage_schema.extend(list(set(elem_list)))
            elem.clear()
            elem_list = []
    if len(elem_list) > 0:
        temp_storage_schema.extend(list(set(elem_list)))
    return list(set(temp_storage_schema))


def create_schema_text(input_file_list):
    """
    Reads the input file list and capture the unique column name per file into a final schema text
    list
    :return:
    """
    output_schema = []
    for file_name in input_file_list:
        output_schema.append(build_schema(file_name))
    return output_schema


def insert_data(data_1, table_name, column_list):
    """
    Updates database in a loop
    :return:
    """
    # import sqlite3
    with sqlite3.connect(ABS_DB_PATH) as con:
        cursor = con.cursor()

    for idx, colhead in enumerate(column_list):
        column_names = ",".join(colhead)
        escaped_data = [sub.replace("'", "''") for sub in data_1[idx]]
        value_concatenated = "\'" + "\',\'".join(escaped_data) + "\'"
        insert_query = f"INSERT INTO {table_name} ({column_names}) values ({value_concatenated})"
        cursor.execute(insert_query)
    con.commit()


def batch_insert_process(file_list):
    """
    Iterate through each row of input file, if the no of records read reaches 10000
    then update the database, and then process the next batch of 10000
    :param file_list:
    :return:
    """
    for idx, file_name in enumerate(file_list):

        total_file_name = IN_FILE_PATH + file_name
        xml_iter = ElemTree.iterparse(total_file_name)
        column_list = []
        counter = 0
        value_array = []
        update_counter = 0

        for event, elem in xml_iter:
            list_of_val = []

            if list(elem.attrib.keys()):
                column_list.append(list(elem.attrib.keys()))

            for key in elem.attrib.keys():
                list_of_val.append(elem.attrib[key])

            if len(list_of_val) > 0:
                value_array.append(list_of_val)
                counter = counter + 1

            if (counter % 10000) == 0 and counter != 0:
                insert_data(value_array, TABLE_LIST[idx], column_list)
                update_counter = update_counter + 1
                value_array = []
                column_list = []
        if len(value_array) > 0:
            insert_data(value_array, TABLE_LIST[idx], column_list)

# Create list of unique column name
final_schema = create_schema_text(FILE_LIST)

# Create database and tables
create_database(ABS_DB_PATH, FILE_LIST, TABLE_LIST, final_schema)

# Insert records in the tables in batches of 10000
batch_insert_process(FILE_LIST)
