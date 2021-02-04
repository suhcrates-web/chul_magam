from datetime import datetime
import article
from make_dict import make_dict
import post
import schedule
import time


def fuck():
    print("shit")
def magam_test():
    fuck()


i =1
schedule.every().day.at("19:15").do(magam_test)

while True:
    i = i+1
    schedule.run_pending()

    time.sleep(1)
    print(i)