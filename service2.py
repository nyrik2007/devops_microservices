import time
from create_table import create_table, update_transaction

create_table()


if __name__ == "__main__":
    while True:
        update_transaction()
        print("updated")
        time.sleep(20)
