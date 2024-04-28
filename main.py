import csv
import os

# import colored
from colored import Fore, Back, style


# creating scheduler
class Scheduler:
    def __init__(self):
        self.schedule = {}
