from src.util import Util
import random
import time


def main():
    util = Util()

    # Clear screen
    util.cls()

    # Create 1.000.000 lawsuits in memory
    print("\nCreating 1.000.000 lawsuits in memory. Please wait...")
    start = time.perf_counter()
    lawsuits_hash, lawsuits_list = util.create_lawsuits(1000000)
    end = time.perf_counter()
    elapsed_time = end - start
    print(f"\nElapsed time: {round(elapsed_time, 2)}s")

    # Divide the data in four parts and a get a sample case number from each
    sample_data = [
        lawsuits_list[random.randrange(0, 249999)]["case_number"],
        lawsuits_list[random.randrange(250000, 449999)]["case_number"],
        lawsuits_list[random.randrange(500000, 749999)]["case_number"],
        lawsuits_list[random.randrange(750000, 999999)]["case_number"],
    ]

    for i, case_number in enumerate(sample_data):
        print(f"\nRandom case number to search ({i+1}/4 range): {case_number}")

        # Search for the case number in the list with no search optimization
        # and measure the elapsed time
        start = time.perf_counter()
        util.get_lawsuit_in_list(case_number, lawsuits_list)
        end = time.perf_counter()
        elapsed_time = end - start
        print("\n|----------------------------------------------------------|")
        print(f"| List search, no optimization        | Time: {elapsed_time:8f}s    |")
        print("|----------------------------------------------------------|")

        # Quick sort and binary search for the case number in the list
        # and measure the elapsed time.
        start = time.perf_counter()
        lawsuits_list_copy = lawsuits_list.copy()
        lawsuits_list_copy.sort(key=lambda value: value["case_number"], reverse=False)
        util.binary_search(lawsuits_list_copy, case_number)
        end = time.perf_counter()
        elapsed_time = end - start
        print(f"| Quick sort and binary search        | Time: {elapsed_time:8f}s    |")
        print("|----------------------------------------------------------|")

        # Performing a binary search for the second time now that
        # the list is already sorted
        start = time.perf_counter()
        util.binary_search(lawsuits_list_copy, case_number)
        end = time.perf_counter()
        elapsed_time = end - start
        print(f"| Binary search second pass           | Time: {elapsed_time:8f}s    |")
        print("|----------------------------------------------------------|")

        # Search for the case number in the hash table
        # and measure the elapsed time
        start = time.perf_counter()
        util.get_lawsuit_in_hash(case_number, lawsuits_hash)
        end = time.perf_counter()
        elapsed_time = end - start
        print(f"| Search in hash table                | Time: {elapsed_time:8f}s    |")
        print("|----------------------------------------------------------|\n")


if __name__ == "__main__":
    main()
