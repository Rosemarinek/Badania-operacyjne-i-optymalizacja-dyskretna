import random
import math

class RNG:
    def __init__(self,seed):
        self.r = seed
        self.a = 1664525
        self.c = 1013904223
        self.m = 2**32
        
    def next(self):
        self.r = (self.a * self.r + self.c) % self.m
        return self.r / self.m

def A(epoches,buffer):
    t_s = 60 #Czas obsługi zgłoszenia 
    t = 0
    a = 0
    b = 0

    #generator wbudowany
    for i in range(0,epoches):
        random_number = random.uniform(0,1)
        result = -math.log(1-random_number)*120
        t = t + result
        a = max(b,t)
        b = a + t_s
        buffer = buffer + a - t
    print(buffer/epoches) 
    
    #generator własny
    buffer = 0
    random_number = RNG(42)
    for i in range(0,epoches):
        rand = random_number.next()
        result = -math.log(1-rand)*120
        t = t + result
        a = max(b,t)
        b = a + t_s
        buffer = buffer + a - t
    print(buffer/epoches)    

def B(epoches,buffer):
    t_s = 0 #Czas obsługi zgłoszenia 
    t = 0
    a = 0
    b = 0

    #generator wbudowany
    for i in range(0,epoches):
        random_number = random.uniform(0,1)
        result = -math.log(1-random_number)*120
        t = t + result
        a = max(b,t)
        random_number = random.uniform(0,1)
        t_s = random_number*120
        b = a + t_s
        buffer = buffer + a - t
    print(buffer/epoches)
    
    #generator własny
    buffer = 0
    random_number = RNG(42)
    for i in range(0,epoches):
        rand = random_number.next()
        result = -math.log(1-rand)*120
        t = t + result
        a = max(b,t)
        rand = random_number.next()
        t_s = rand*120
        b = a + t_s
        buffer = buffer + a - t
    print(buffer/epoches)

def C(epoches,buffer):
    t_s = 0 #Czas obsługi zgłoszenia 
    t = 0
    a = 0
    b = 0

    #generator wbudowany
    for i in range(0,epoches):
        random_number = random.uniform(0,1)
        result = -math.log(1-random_number)*120
        t = t + result
        a = max(b,t)
        random_number = random.uniform(0,1)
        t_s = -math.log(1-random_number)*60
        b = a + t_s
        buffer = buffer + a - t
    print(buffer/epoches) 
    
    #generator własny
    buffer = 0
    random_number = RNG(42)
    for i in range(0,epoches):
        rand = random_number.next()
        result = -math.log(1-rand)*120
        t = t + result
        a = max(b,t)
        rand = random_number.next()
        t_s = -math.log(1-rand)*60 
        b = a + t_s
        buffer = buffer + a - t
    print(buffer/epoches)   

def D(epoches,buffer):
    t_s = 0 #Czas obsługi zgłoszenia 
    t = 0
    a = 0
    b = 0

    #generator wbudowany
    for i in range(0,epoches):
        random_number = random.uniform(0,1)
        result = -math.log(1-random_number)*120
        t = t + result
        a = max(b,t)
        random_number1 = random.uniform(0,1)
        random_number2 = random.uniform(0,1)
        t_s = 60 + math.sqrt(-2.0 * math.log(random_number1)) * math.cos(2.0 * math.pi * random_number2) * 20
        b = a + t_s
        buffer = buffer + a - t
    print(buffer/epoches) 
    
    #generator własny
    buffer = 0
    random_number = RNG(42)
    for i in range(0,epoches):
        rand = random_number.next()
        result = -math.log(1-rand)*120
        t = t + result
        a = max(b,t)
        rand1 = random_number.next() 
        rand2 = random_number.next()
        t_s = 60 + math.sqrt(-2.0 * math.log(rand1)) * math.cos(2.0 * math.pi * rand2) * 20
        b = a + t_s
        buffer = buffer + a - t
    print(buffer/epoches)    

if __name__ == "__main__":
    buffer = 0 #bufor w którym czeka się na zgłoszenie
    epoches = 10000000 #liczba zgłoszeń
    A(epoches,buffer)
    B(epoches,buffer)
    C(epoches,buffer)
    D(epoches,buffer)
