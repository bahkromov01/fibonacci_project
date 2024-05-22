
class Fibonacci:
    def __init__(self):
        self.a = 0
        self.b = 1

    def __iter__(self):
        return self

    def __next__(self):
        result = self.b
        self.b, self.a = self.b + self.a, self.b
        return result

    def throw(self, exc_type):
        raise exc_type

    def generator(self):
        # Generator
        while True:
            yield self.b
            self.b, self.a = self.b + self.a, self.b


fibonacci_iterator = Fibonacci()
for i, num in enumerate(fibonacci_iterator):
    print(num, end=" ")
    if i >= 9:
        break

print("\n")

fibonacci_generator = Fibonacci().generator()
for i in range(10):
    try:
        print(next(fibonacci_generator), end=" ")
        if i == 5:
            fibonacci_generator.throw(ValueError)
    except ValueError:
        print("Error berdi")
        break

print("\n")


def fibonacci_generator():
    a, b = 0, 1
    while True:
        value = yield a
        if value is not None:
            a, b = b, value
        else:
            a, b = b, a + b

fib_gen = fibonacci_generator()

for _ in range(10):
    print(next(fib_gen), end=" ")

print("\n")


fib_gen.send(None)
print(next(fib_gen), end=" ")

fib_gen.send(5)
for _ in range(9):
    print(next(fib_gen), end=" ")

print("\n")

fib_gen.close()
