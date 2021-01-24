class Counter:
    count = 0

    def get_count(self):
        print(self.count)

    def add(self):
        self.count += 1
        self.get_count()

    def minus(self):
        self.count -= 1
        self.get_count()
counter = Counter()
counter.add()
counter.add()
counter.minus()
