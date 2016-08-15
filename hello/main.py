import sys
import time

class Console:
    def stdout(self, msg):
        print(msg)
    def sysarg(self):
        if len(sys.argv) < 2:
            raise RuntimeError('no argument')
        return sys.argv[1]

class FileSystem:
    def read_file(self, file_path):
        file = open(file_path)
        line = file.readline()
        file.close()
        return line

class Configuration:
    def __init__(self, console, file_system):
        self.console = console
        self.file_system = file_system

    def target(self):
        file_path = self.console.sysarg()
        return self.file_system.read_file(file_path)

class Greeter:
    def __init__(self, console):
        self.console = console

    def greet(self, target):
        self.console.stdout(target)

class Clock:
    def get_current_time(self):
        return time.time()

class Notifier:
    def __init__(self, console):
        self.console = console

    def take_time(self, time):
        self.console.stdout('time: ' + str(time) + ' seconds')

class Timer:
    def __init__(self, notifier, clock):
        self.notifier = notifier
        self.clock = clock

    def measure(self, func):
        before = self.clock.get_current_time()
        func()
        after = self.clock.get_current_time()
        self.notifier.take_time(after - before)

def run(timer, greeter, configuration):
    target = configuration.target()
    timer.measure(lambda: greeter.greet(target))

def main():
    console = Console()
    file_sytem = FileSystem()
    clock = Clock()
    notifier = Notifier(console=console)
    timer = Timer(notifier=notifier, clock=clock)
    greeter = Greeter(console=console)
    configuration = Configuration(console=console, file_system=file_sytem)

    run(timer, greeter, configuration)

if __name__ == '__main__':
    main()
