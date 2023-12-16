from machine import Timer

def callback1(t):
    print(1)
    
def callback2(t):
    print(2)
    
#time2 = Timer()
#time2.init(period=2000,callback=callback2)

def run10(t):
    global i
    i += 1
    if i==10:
        t.deinit()
    print(i)
    
i=1
timer = Timer(period=1000, mode=Timer.PERIODIC, callback=lambda t:run10(t))
timer = Timer(period=1000, mode=Timer.PERIODIC, callback=lambda t:print('一直執行'))