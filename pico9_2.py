from machine import Timer

def callback1(t:Timer):
    print(1)
    
def callback2(t:Timer):
    print(2)
    
def callback3(t:Timer):
    print(3)
    t.deinit()
    
time1 = Timer()
time1.init(freq=1,callback=callback1)

time2 = Timer()

time2.init(period=2000,callback=callback2)

time3 = Timer()
time3.init(period=3000,callback=callback3)

def run10(t):
    global i
    i += 1
    if i==10:
        t.deinit()
    print(i)
    
i=1
timer = Timer(period=1000, mode=Timer.PERIODIC, callback=lambda t:run10(t))
timer = Timer(period=1000, mode=Timer.PERIODIC, callback=lambda t:print('一直執行'))