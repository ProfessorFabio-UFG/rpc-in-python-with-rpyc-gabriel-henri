import rpyc
from constRPYC import *  #-
from rpyc.utils.server import ThreadedServer
from collections import Counter

class DBList(rpyc.Service):
    value = []

    def exposed_append(self, data):
        self.value.append(data)
        return self.value

    def exposed_value(self):
        return self.value

    def exposed_remove(self, data):
        if data in self.value:
            self.value.remove(data)
            return True
        return False

    def exposed_clear(self):
        self.value = []
        return "List cleared."

    def exposed_length(self):
        return len(self.value)

    def exposed_average(self):
        try:
            numeric_values = [x for x in self.value if isinstance(x, (int, float))]
            if not numeric_values:
                return "No numeric values to calculate average."
            return sum(numeric_values) / len(numeric_values)
        except Exception as e:
            return f"Error: {e}"

    def exposed_mode(self):
        if not self.value:
            return "List is empty."
        count = Counter(self.value)
        mode_val, mode_freq = count.most_common(1)[0]
        return mode_val

    def exposed_sort(self, reverse=False):
        try:
            self.value.sort(reverse=reverse)
            return self.value
        except Exception as e:
            return f"Error sorting: {e}"

    def exposed_unique(self):
        return list(set(self.value))

if __name__ == "__main__":
    server = ThreadedServer(DBList(), port=PORT)
    server.start()
