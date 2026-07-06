import sqlite3


def reset_index(table_name_list):
    conn = sqlite3.connect("example.db")
    cursor = conn.cursor()

    # 2. Send the raw query
    for table_name in table_name_list:
        try:
            cursor.execute(f"Delete from sqlite_sequence WHERE name = {table_name};")
            conn.commit()
        except Exception as e:
            print(e)
            conn.rollback()
            continue

    conn.close()
