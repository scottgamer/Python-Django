# A module is basically a file containing a set of functions to include in your application. There are core python modules, modules you can install using the pip package manager (including Django) as well as custom modules

# Core modules
# import datetime
from datetime import date

import time
from time import time

# Pip modules
from camelcase import CamelCase

# Custom modules
# import validator
from validator import validate_email

today = date.today()
timestamp = time()

print(timestamp)

c = CamelCase()
print(c.hump('hello there world'))

email = 'test@test.com'

if validate_email(email):
    print('Valid email')
else:
    print('Invalid email')
