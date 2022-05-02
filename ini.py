from src.model import Model
from data import tokens , settings
import threading


def checker(model , exchange , alt):
    change_f = model.estimate_arbitrage_forward(exchange , alt)
    change_b = model.estimate_arbitrage_backward(exchange , alt)

    model.log("Binance | {:5}: {:8.5f}% / {:8.5f}%".format(alt , change_f , change_b))

    if change_f > settings.MIN_DIFFERENCE:
        model.log("Got opportunity for {:5} @{:.4f} on Binance".format(alt , change_f))
        model.run_arbitrage_forward(exchange , alt)

    elif change_b > settings.MIN_DIFFERENCE:
        model.log("Got opportunity for {:5} @{:.4f} on Binance".format(alt , change_b))
        model.run_arbitrage_backward(exchange , alt)


def run(model , exchange , thread_number):
    alts = tokens.binance_tokens
    while True:
        for i in range(0 , len(alts) , thread_number):
            alts_batch = alts[i:i + thread_number]
            threads = []
            for asset in alts_batch:
                threads.append(threading.Thread(target=checker , args=(model , exchange , asset)))
                threads[-1].start()
            for thread in threads:
                thread.join()
            model.reset_cache()


if __name__ == "__main__":
    model = Model()
    exchange = model.binance
    model.log("Starting to listen the binance markets")
    thread_number = 5
    run(model , exchange , thread_number)
