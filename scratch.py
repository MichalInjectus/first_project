import os
import time

print(os.getcwd())
os.mkdir('new_foder')
time.sleep(5)
os.rename('new_foder', 'new_foder2')
time.sleep(5)
os.rmdir('new_foder2')