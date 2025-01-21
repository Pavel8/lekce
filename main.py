import threading
import time

# Globální proměnná sdílená mezi vlákny
balance = 1000


# Vytvoření Threading Lock
lock = threading.Lock()

# Funkce reprezentující transakci
def make_transaction(amount):
    global balance
    current_balance = balance

    lock.acquire()

    try:
        # Kritická sekce, kde se mění sdílená proměnná
        balance = current_balance - amount
        # shared_variable = shared_variable + 1
    finally:
        # Uvolnění zámku

        lock.release()

# Vytvoření dvou vláken pro provedení transakcí
thread1 = threading.Thread(target=make_transaction, args=(200,))
thread2 = threading.Thread(target=make_transaction, args=(300,))


thread1.start()
thread2.start()


thread1.join()
thread2.join()

# Očekávaný výsledek je 500, ale může být odlišný kvůli race condition
print("Zůstatek na účtu po transakcích:", balance)