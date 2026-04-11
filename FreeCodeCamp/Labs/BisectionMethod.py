""" 
I've already done this in my chermical engenieer carrer,
in Simulacion de procesos 1. i've used matlab but the idea is the same so...
"""
def square_root_bisection(square_target, tolerance=0.01, max_iterations=1000):
    if square_target < 0:
        raise ValueError("Square root of negative number is not defined in real numbers")

    if square_target == 0 or square_target == 1:
        print(f"The square root of {square_target} is {square_target}")
        return square_target

    low = 0
    high = max(1, square_target)
    iterations = 0

    while (high - low) > tolerance and iterations < max_iterations:
        mid = (low + high) / 2
        square = mid * mid

        if square == square_target:
            print(f"The square root of {square_target} is approximately {mid}")
            return mid
        elif square < square_target:
            low = mid
        else:
            high = mid

        iterations += 1

    if (high - low) <= tolerance:
        root = (low + high) / 2
        print(f"The square root of {square_target} is approximately {root}")
        return root

    print(f"Failed to converge within {max_iterations} iterations")
    return None
