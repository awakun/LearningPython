import os
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
pi_digits_path = os.path.join(THIS_FOLDER, 'pi_digits.txt')

with open(pi_digits_path) as file_object:
    contents = file_object.read()
print(contents)
