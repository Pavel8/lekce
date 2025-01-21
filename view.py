import threading

# Globální proměnná sdílená mezi vlákny
shared_variable = 0

# Vytvoření Threading Lock
lock = threading.Lock()

# Funkce, která bude prováděna v různých vláknech
def increment_shared_variable():
    global shared_variable
    for _ in range(1000000):
        # Získání zámku
        lock.acquire()
        try:
            # Kritická sekce, kde se mění sdílená proměnná
            shared_variable += 1
            #shared_variable = shared_variable + 1
        finally:
            # Uvolnění zámku
            lock.release()
            #pass


thread1 = threading.Thread(target=increment_shared_variable)
thread2 = threading.Thread(target=increment_shared_variable)


thread1.start()
thread2.start()


thread1.join()
thread2.join()

# Výsledek by měl být 2000000 (2 * 1000000)
print("Výsledek:", shared_variable)