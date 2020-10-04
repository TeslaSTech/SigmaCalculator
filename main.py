if __name__ == '__main__':
    start, runto, end = 24, 35, 129
    common_difference = 5
    run_length = runto-common_difference
    sum = start-5
    sum_of_all = 0
    for n in range(runto):
        iterative = iterative  # put your iterative here if it involves n
        sum += iterative
        print(str(n+1) + ": " + str(sum))
        sum_of_all += sum
print("Sum of all: " + str(sum_of_all))
print("recursive formula: a(n) = a(n - 1) + " + str(iterative))
