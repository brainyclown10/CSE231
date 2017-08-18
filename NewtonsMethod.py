# Newton's method to calculate squre root

# get three inputs from the user (two units, 1 float)
# not not robust on bad input
num_str = input("Find the square root of integer: ")
num_int = int(num_str)
guess_str = input("Initial guess: ")
guess_float = float(guess_str)
tolerance_float = float(input("What tolerance: "))

original_guess_float = guess_float  # hang onto the original guess
count_int = 0  # count the number of guesses
previous_float = 0  # track the previous calculated value

while abs(previous_float - guess_float) > tolerance_float:
    previous_float = guess_float
    quotient_float = num_int / guess_float
    guess_float = (quotient_float + guess_float) / 2
    count_int = count_int + 1

# do the algorithm as described above

# output the three original values, the number of
# iteration and the square root
print("Square roof of", num_int, " is:", guess_float)
print("Took ", count_int, " reps to get it to tolerance: ", tolerance_float)
print("Starting from a guess of:", original_guess_float)
