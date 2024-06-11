import math
import random

def Felszin(meret):
    felszin = (meret / 2) * (meret / 2) * math.pi
    return felszin

atmero = int(input('Kérem a medence átmérőjét (m): '))
szinek = ['kek', 'zold', 'lila', 'hupikek']
print(f'A medence színe {random.choice(szinek)}')
print(f'A medence átmérője: {Felszin(atmero)}')