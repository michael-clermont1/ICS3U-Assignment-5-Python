#!/usr/bin/env python3

# Created by: Michael Clermont
# Created on: Mar 2022
# This program is to record integers until the user ends it


def main():
    # this function is to record integers until the user ends it

    counter = 0
    positive_count = 0
    negative_count = 0
    zero_count = 0
    user_end = 0
    # process & output
    while True:
        try:
            if counter == 1:
                user_end = input(
                    "Do you want to end the program and get your results (Y/N): "
                )
            elif counter == 0:
                numbers_entered = int(input("Enter a number to record: "))
            if user_end == "Y" or user_end == "y":
                print(
                    "\nPositive numbers: {0}, negative numbers: {1}, zeros: {2} ".format(
                        positive_count, negative_count, zero_count
                    )
                )
                break
            elif user_end == "N" or user_end == "n":
                numbers_entered = int(input("Enter a number to record: "))
            elif user_end == 0:
                counter = counter + 1
                if numbers_entered > 0:
                    positive_count = positive_count + 1
                elif numbers_entered < 0:
                    negative_count = negative_count + 1
                elif numbers_entered == 0:
                    zero_count = zero_count + 1
                continue
            else:
                print("That is not yes or no.")
                break
            if numbers_entered > 0:
                positive_count = positive_count + 1
            elif numbers_entered < 0:
                negative_count = negative_count + 1
            elif numbers_entered == 0:
                zero_count = zero_count + 1
        except Exception:
            print("\nInvalid input.")
            break
    print("\nDone.")


if __name__ == "__main__":
    main()
