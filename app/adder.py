def add_file(filename):
    sum = 0
    with open(filename, 'r') as f:
        lines = f.readlines()

        for l in lines:
            n = int(l)
            sum += n
            print(n)

    return sum

