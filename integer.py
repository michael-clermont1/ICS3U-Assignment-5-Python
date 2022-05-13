#!/usr/bin/env python3

# Created by: Michael Clermont
# Created on: May 2022
# This program is to record integers until the user ends it


def main():
    # this function is to record integers until the user ends it

    positive_count = 0
    negative_count = 0
    zero_count = 0
    user_end = 0
    # process & output
    while True:
        try:
            numbers_entered = int(input("Enter a number to record: "))
            if numbers_entered > 0:
                positive_count = positive_count + 1
            elif numbers_entered < 0:
                negative_count = negative_count + 1
            elif numbers_entered == 0:
                zero_count = zero_count + 1
            user_end = input(
                "Do you want to end the program and get your results (Y/N (default is N)): "
            )
            if user_end == "Y" or user_end == "y":
                print(
                    "\nPositive numbers: {0}, negative numbers: {1}, zeros: {2} ".format(
                        positive_count, negative_count, zero_count
                    )
                )
                break
        except Exception:
            print("\nInvalid input, try again.")
            continue
    print("\nDone.")


if __name__ == "__main__":
    main()
