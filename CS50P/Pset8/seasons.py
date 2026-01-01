import sys
from datetime import date
import inflect

class Time:
    def __init__(self, dob):
        try:
            self.dob = date.fromisoformat(dob)
        except ValueError:
            sys.exit("Invalid date format")

    def minutes_lived(self):
        today = date.today()
        if self.dob > today:
            sys.exit("Invalid date")

        diff = today - self.dob
        return diff.days * 24 * 60


def main():
    d = input("Enter your DOB (YYYY-MM-DD): ")
    p = inflect.engine()
    dob = Time(d)
    print(p.number_to_words(dob.minutes_lived(),andword='').capitalize(),"minutes",)


if __name__ == "__main__":
    main()
