import time

from create_table import create_table, update_price_usd


create_table()

if __name__ == "__main__":
    while True:
        update_price_usd()
        print("updated")
        time.sleep(20)