from kucoin.client import Client as Kucoin
from kucoin.exceptions import KucoinAPIException
from config import KEY, SECRET
import time
from tqdm import tqdm
import csv


def get_total_trades(kucoin):
    orders = kucoin.get_dealt_orders(page=1, limit=1)
    return orders['total']


def trade_report_gen(kucoin, total_orders):

    # at list one page to begin with
    nb_page = 1
    orders_per_page = 20

    current_page = 1

    # Just fetch the number of orders and pages one, so that
    # if other orders are done, we need to call the trade report
    # again
    init = True

    orders_yield = 0

    # total_orders = 1

    oldest_ts = round(time.time() * 1000)
    while orders_yield <= total_orders:
        # print("Oldest timestamp {}, Number of orders yiels: {}/{}".format(oldest_ts, orders_yield, total_orders))
        try:
            orders = kucoin.get_dealt_orders(page=1, limit=orders_per_page, before=oldest_ts)
        except KucoinAPIException as e:
            print(e)
            print("current page: {}, orders per page: {}".format(current_page, orders_per_page))
            return

        # if init:
        #     total_orders = orders['total']
        #     init = False

        # cannot use yield from here as we need to get the oldest timestamp anyway
        for order in orders['datas']:
            oldest_ts = min(oldest_ts, order['createdAt'])
            yield order

        orders_yield += len(orders['datas'])


def main():
    kucoin = Kucoin(KEY, SECRET)
    total_orders = get_total_trades(kucoin)

    headers = ["createdAt", "coinType", "coinTypePair", "direction",
               "dealPrice", "amount", "dealValue", "fee", "feeRate", "orderOid"]
    with open('trade_history.csv', 'w') as csv_file:
        order_writer = csv.writer(csv_file)
        order_writer.writerow(headers)
        for order in tqdm(trade_report_gen(kucoin, total_orders), total=total_orders):
            order_writer.writerow([order[x] for x in headers])


if __name__ == "__main__":
    main()
