from django.db import connection


def reset_index(table_name_list):
    cursor = connection.cursor()

    for table_name in table_name_list:
        try:
            cursor.execute(f"Delete from sqlite_sequence WHERE name = '{table_name}';")
            connection.commit()
        except Exception as e:
            print(e)
            connection.rollback()
            continue

    connection.close()
