import csv
import os

# import colored
from colored import Fore, Back, style


# creating scheduler
class Scheduler:
    def __init__(self):
        self.schedule = {}

# csv file
        if os.path.isfile("schedule.csv"):
            with open("schedule.csv", "r") as file:
                csv_reader = csv.reader(file)
                for row in csv_reader:
                    hour, task = row
                    self.schedule[int(hour)] = task

# to add in the schedule

    def add_schedule(self, hour, task):
        if hour in self.schedule:
            color: str = f"{Style.BOLD}{fore.RED}{Back.BLACK}"

            print(f"You already have a task for {hour}:00.")