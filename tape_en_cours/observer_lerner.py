class Person:
    def __init__(self, name):
        self.name = name
        self.observers = []

    def get_name(self):
        self.notify(f"get name returned {self.name}")
        return self.name

    def set_name(self, new_name):
        old_name = self.name
        self.name = new_name
        self.notify(f"set name from {old_name} to {new_name}")

    def notify(self, message):
        for one_observer in self.observers:
            one_observer.notify(message)

    def attach(self, observer):
        if observer not in self.observers:
            self.observers.append(observer)

    def detach(self, observer):
        if observer in self.observers:
            self.observers.remove(observer)


class FileLogger:
    def __init__(self, filename):
        self.f = filename

    def notify(self, message):
        with open(self.f, "a") as f:
            f.write(f"{message}\n")


class ScreenLogger:
    def notify(self, message):
        print(f"ScreenLogger: {message}")


p = Person("Reuven")
fl = FileLogger("personlog.txt")
p.attach(fl)
print(p.get_name())
p.attach(ScreenLogger())
p.set_name("newname")
p.detach(fl)
print(p.get_name())

