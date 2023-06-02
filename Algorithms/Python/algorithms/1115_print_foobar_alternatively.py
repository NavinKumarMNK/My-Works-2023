from threading import Event
from typing import Callable
class FooBar:
    def __init__(self, n):
        self.n = n
        self.accessFoo = Event()
        self.accessFoo.set()
        self.accessBar = Event()
        self.accessBar.clear()

    def foo(self, printFoo: 'Callable[[], None]') -> None:
        for i in range(self.n):
            self.accessFoo.wait()
            # printFoo() outputs "foo". Do not change or remove this line.
            printFoo()
            self.accessFoo.clear()
            self.accessBar.set()


    def bar(self, printBar: 'Callable[[], None]') -> None:
        for i in range(self.n):
            self.accessBar.wait()
            # printBar() outputs "bar". Do not change or remove this line.
            printBar()
            self.accessBar.clear()
            self.accessFoo.set()


from threading import Lock #Fatter Solution
class FooBar:
    def __init__(self, n):
        self.n = n
        self.fooLock = Lock()
        self.barLock = Lock()
        self.barLock.acquire()

    def foo(self, printFoo: Callable[[], None]) -> None:
        for i in range(self.n):
            self.fooLock.acquire()
            printFoo()
            self.barLock.release()

    def bar(self, printBar: Callable[[], None]) -> None:
        for i in range(self.n):
            self.barLock.acquire()
            # printBar() outputs "bar". Do not change or remove this line.
            printBar()
            self.fooLock.release()



from threading import Barrier
class FooBar:
    def __init__(self, n):
        self.n = n
        self.barrier = Barrier(2)

    def foo(self, printFoo):
        for i in range(self.n):
            printFoo()
            self.barrier.wait()

    def bar(self, printBar):
        for i in range(self.n):
            self.barrier.wait()
            printBar()