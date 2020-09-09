#Algorithm that checks how long it takes
#for the second tortoise to catch up to
#the first, given two speeds and a distance 
#between them. 

def race(v1, v2, g):
    #Check for valid inputs
    if v1 < v2 and g and v1 and v2:
        #Find the time it takes
        time = g/(v2-v1)
        #Convert the hours to a whole number
        hours = int(time)
        #Find the rest from hours and multiply by 60. 
        minutes = (time*60) % 60
        seconds = (time*3600) % 60
        #return hours, mins and secs
        return [hours, int(minutes), int(seconds)]
    #if nothing else return None. 
    return None

#Input is given as feet per hour for speed, and feet for the
#Distance. 

print(race(720, 850, 70)==[0, 32, 18])