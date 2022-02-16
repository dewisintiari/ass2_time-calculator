# This entrypoint file to be used in development. Start by reading README.md
from time_calculator import add_time
from unittest import main

initial = input("Enter initial time (format 'hh:mm AM' or 'hh:mm PM' without the apostrophe : ")
diff = input("Enter the increment of time (format 'hh:mm' without the apostrophe): ")
day = input("Enter the day or leave it blank : ")

print(add_time(initial, diff, day))


# Run unit tests automatically
main(module='test_module', exit=False)