import time
from random import randint
import os

def log(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        exec_time = time.time() - start
        func_name = func.__name__.replace("_", " ").title()
        user = os.getlogin()
        with open("machine.log", "a") as f:
            if exec_time > 0.001:
                f.write(f"({user})Running: {func_name:20} [ exec-time = {exec_time:.3f} s ]\n")
            else:
                f.write(f"({user})Running: {func_name:20} [ exec-time = {exec_time * 1000:.3f} ms ]\n")
        return result
    return wrapper

class CoffeeMachine():
    water_level = 25
    @log
    def start_machine(self):
        if self.water_level > 20:
            return True
        else:
            print("Please add water!")
        return False
    

    @log
    def boil_water(self):
        return "boiling..."
    

    @log
    def make_coffee(self):
        if self.start_machine():
            for _ in range(20):
                time.sleep(0.1)
            self.water_level -= 1
            print(self.boil_water())
            print("Coffee is ready!")


    @log
    def add_water(self, water_level):
        time.sleep(randint(1, 5))
        self.water_level += water_level
        print("Blub blub blub...")

if __name__ == "__main__":
    machine = CoffeeMachine()
    for i in range(0, 5):
        machine.make_coffee()
    machine.make_coffee()
    machine.add_water(70)