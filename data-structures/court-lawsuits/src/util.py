import uuid
import faker
import os


class Util:
    def create_lawsuits(self, num_lawsuits):
        lawsuits_hash = {}
        lawsuits_list = []
        fake = faker.Faker()
        while len(lawsuits_hash) < num_lawsuits:
            case_number = str(uuid.uuid4())

            lawsuit = {
                "case_number": case_number,
                "plaintiff": fake.name(),
                "defendant": fake.name(),
                "filing_date": fake.date_between(start_date="-5y", end_date="today").strftime("%d-%m-%Y"),
                "status": fake.random_element(elements=("pending", "settled", "dismissed")),
            }

            lawsuits_hash[case_number] = lawsuit

            lawsuits_list.append(lawsuit)

        return lawsuits_hash, lawsuits_list

    def binary_search(self, lst, case_number):
        low = 0
        high = len(lst) - 1
        mid = 0

        while low <= high:
            mid = (high + low) // 2
            guess = lst[mid]["case_number"]

            # If guess is greater, ignore left half
            if guess < case_number:
                low = mid + 1

            # If guess is smaller, ignore right half
            elif guess > case_number:
                high = mid - 1

            # means guess is present at mid
            else:
                return lst[mid]

        # If we reach here, then the element was not present
        return None

    def get_lawsuit_in_hash(self, case_number, lawsuits_hash):
        try:
            return lawsuits_hash[case_number]
        except:
            return None

    def get_lawsuit_in_list(self, case_number, lawsuits_list):
        for lawsuit in lawsuits_list:
            if lawsuit["case_number"] == case_number:
                return lawsuit
        return None

    def cls(self):
        if os.name == "posix":
            os.system("clear")
        else:
            os.system("cls")
