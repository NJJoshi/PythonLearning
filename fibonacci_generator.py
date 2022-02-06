import pyinputplus as pypi


def fib_n_generator(n):
    last = 0
    curr = 1

    if n == 0:
        return

    yield last
    if n == 1:
        return

    yield curr
    if n == 2:
        return

    ii = 2
    while ii < n + 1:
        next = curr + last
        yield next
        last = curr
        curr = next
        ii += 1

    return fib_n_generator(n)


def main():
    n = pypi.inputInt(prompt='Please enter number:', default=0)
    fib = [xx for xx in fib_n_generator(n)]
    print(fib)


main()
