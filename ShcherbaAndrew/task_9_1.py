import threading
from time import sleep

def philosopher(name, left, right):
    while True:
        print(f"{name} is thinking\n")
        # sleep(0.001)
        with left:
             with right:
                 print(f'Philosopher {name} is eating.')
                 # sleep(0.001)

FORKS = 5
forks = [threading.Lock() for n in range(FORKS)]

phils = [threading.Thread(
    target=philosopher,
    args=(n, forks[n], forks[(n + 1) % FORKS])
) for n in range(FORKS)]

for p in phils:
    p.start()