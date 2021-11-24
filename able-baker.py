#multi chanel simulation model example of able-baker customer care
import random                       

def arrival_time():    
    r=random.random()
    if 0 <= r < 0.25:
        return 1
    if 0.25 <= r < 0.65:
        return 2
    if 0.65 <= r < 0.85:
        return 3
    if 0.85 <= r < 1:
        return 4
def able_time():    
    r=random.random()
    if 0 <= r < 0.3:
        return 2
    if 0.3 <= r < 0.58:
        return 3
    if 0.58 <= r < 0.83:
        return 4
    if 0.83 <= r < 1:
        return 5
def baker_time():    
    r=random.random()
    if 0 <= r < 0.35:
        return 3
    if 0.35 <= r < 0.6:
        return 4
    if 0.6 <= r < 0.8:
        return 5
    if 0.8 <= r < 1:
        return 6
    
class caller:
    def __init__(self, _ID, _art, _server, _ser_start, _sert, _delay):
        self.ID_ = _ID              #the similar but different variables are named with underscore before/after/none
        self.art_ = _art            #arrival time
        self.server_ = _server      #assigned server name
        self.ser_start_ = _ser_start    #start of service
        self.sert_ = _sert          #service duration
        self.delay_ = _delay        #waiting time


def main():
    list = []                       #list of class objects of caller
    art = 0                         
    av_a = 0                        #availability of able
    av_b = 0                        #availability of baker
    free_a = 0                      #next time able is free
    free_b = 0                      #next time baker is free
    idle_a = 0                      #idle time of able
    idle_b = 0                      #idle time of baker
    delay = 0                       
    for i in range(100):
        if art>=free_a:
            idle_a += art-free_a
            av_a = 0
        if art>=free_b:
            idle_b += art-free_b
            av_b = 0

        if av_a == 0:                       #if able is idle
            server = 'able'
            sert = able_time()
            av_a = 1
            ser_start = art
            free_a = ser_start + sert
        elif av_b == 0:                     #if able is busy and baker is idle
            server = 'baker'
            sert = baker_time()
            av_b = 1
            ser_start = art
            free_b = ser_start + sert
        else:                               #if both are busy
            if free_a<= free_b:             #if able finishes first
                server = 'able'
                sert = able_time()
                av_a = 1
                ser_start = free_a
                free_a = ser_start + sert
                delay = ser_start - art
            else:                           #if baker finishes first
                server = 'baker'
                sert = baker_time()
                av_b = 1
                ser_start = free_b
                free_b = ser_start + sert
                delay = ser_start - art
        
        list.append( caller(i+1, art, server, ser_start, sert, delay))
        art += arrival_time()
        delay = 0

    print("~ID~" , "~arrival time~" , "~server~" , "~start time~" , "~service time~" , "~delay~")
    for person in list:
        print(person.ID_,"\t" , person.art_,"\t" , person.server_,"\t\t" , person.ser_start_,"\t\t" , person.sert_,"\t" , person.delay_)
    print("idle time of able is ", idle_a)
    print("idle time of baker is ", idle_b)

if __name__ == '__main__':
    main()