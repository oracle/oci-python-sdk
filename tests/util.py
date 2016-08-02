import unittest
import random

def random_number_string():
    return str(random.randint(0, 10000))

def unique_name(base_name):
    return base_name + '_' + random_number_string()
