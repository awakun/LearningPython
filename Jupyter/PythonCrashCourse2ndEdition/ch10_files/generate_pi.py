"""This is how I made the digits_of_pi.txt file because I wanted to go
a little further than the book did."""
# Install using pipinstall mpmath
from mpmath import mp
import os

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(THIS_FOLDER, "pi_digits.txt")

# Set the number of digits of pi to get, get pi as a string with no decimal.
mp.dps = 1000
pi_to_str = str(mp.pi)
pi_to_str = pi_to_str.replace(".", "")

# Break up pi into 10 digit chunks
x = 0
pi_list = []
while x < len(pi_to_str):
    pi_list.append(pi_to_str[x : x + 10])
    x += 10

# Clear out the file
with open(filename, 'w') as f:
    for chunk in pi_list:
        if chunk == pi_to_str[0:10]:
            chunk_list = list(chunk)
            chunk_list.insert(1, ".")
            chunk = ''.join(chunk_list)

        f.write(f"{chunk}\n")
