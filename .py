import random as rd
from time import sleep
while True:
	nd1 = rd.randint(1,6)
	nd2 = rd.randint(1,6)
	r = nd1 + nd2
	print(f"el numero es {r}")
	sleep(1)
