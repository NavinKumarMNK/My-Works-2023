from threading import Lock
class FizzBuzz:
    def __init__(self, n: int):
        self.n = n
        self.fifteen = self.n // 15
        self.three = self.n // 3 - self.fifteen
        self.five = self.n // 5 - self.fifteen
        self.rest = self.n - self.three - self.fifteen - self.five
        self.fl = Lock()  # Semaphore(1)
        self.bl = Lock()  # Semaphore(1)
        self.fbl = Lock() # Semaphore(1)
        self.nl = Lock()  # Semaphore(1)
        self.fl.acquire()
        self.bl.acquire()
        self.fbl.acquire()
        self.cur = 1

    def release_lock(self, is_number_thread=False):
        if self.cur % 15 == 0:
            self.fbl.release()
        elif self.cur % 3 == 0:
            self.fl.release()
        elif self.cur % 5 == 0:
            self.bl.release()
        else:
            if not is_number_thread:
                self.nl.release()
            return True
        return False

    def fizz(self, printFizz: 'Callable[[], None]') -> None:
        for _ in range(self.three):
            with self.fl:
                printFizz()
                self.cur += 1
                self.release_lock()
            self.fl.acquire()    

    def buzz(self, printBuzz: 'Callable[[], None]') -> None:
        for _ in range(self.five):
            with self.bl:
                printBuzz()
                self.cur += 1
                self.release_lock()
            self.bl.acquire()    

    def fizzbuzz(self, printFizzBuzz: 'Callable[[], None]') -> None:
        for _ in range(self.fifteen):
            with self.fbl:
                printFizzBuzz()
                self.cur += 1
                self.release_lock()
            self.fbl.acquire()    
        
    def number(self, printNumber: 'Callable[[int], None]') -> None:
        for _ in range(self.rest):
            again = True 
            with self.nl:
                printNumber(self.cur)
                self.cur += 1
                again = self.release_lock(is_number_thread=True)
            if not again:
                self.nl.acquire()     