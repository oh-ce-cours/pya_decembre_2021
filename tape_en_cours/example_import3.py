from a_importer import code_metier

print(code_metier.a)
from example_import2 import code_metier as code_metier2
from example_import import code_metier as code_metier1

print(code_metier is code_metier1 and code_metier1 is code_metier2)

import time 

time.sleep(10000)