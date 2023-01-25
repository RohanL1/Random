# calculating area of curve with monte arlo method with 10 mil simulations (x^2 + y ^2 - 4 )^ 3 - 108y^2 = 0
# given range for x and y  === (x -> 0 to 2 * (2)^1/2 ) , ( y -> 0 to 4 )
# hint - calculate area for 1st quad and mult it by 4
# approach - randomly select x,y cordinates between (x - 0 to 2 * (2)^1/2 ) , ( y - 0 to 4 )
#            and check if point is in curve or not, 
#            measure total points inside the curve for total number of points
#            depending upon above we can calculate the ratio of area of curve .....

import random
import math


sqrt_2 = math.sqrt(2)
x_min , x_max = 0, 2 * sqrt_2
y_min , y_max = 0, 4

# print(x_min , x_max)
# print(y_min , y_max)

# random.seed(123)

def getRandomAreaCurve(itr): # function defination 
    cnt=0
    for i in range (0, itr):
        x = random.uniform(x_min, x_max)
        y = random.uniform(y_min, y_max) # taking random point in given min, max range for x and y

        x2=math.pow(x,2)
        y2=math.pow(y,2) # calculating tmps 
        if ((math.pow((x2 + y2 - 4 ), 3) - 108 * y2)) <= 0: # checking if point is inside the curve or not // update this in case of diff. equation
            cnt += 1
            # print(" > +1\n")

    print ("inPOINT : {}".format(cnt) ) # debug 
    fact_of_area = cnt / itr
    print ("Fact_of Area : {}".format(fact_of_area) ) # debug 
    total_area = 8 * sqrt_2 # 4 * 2 * (2)^1/2
    print ("total_area of 1st QUAD : {}".format(total_area) ) # debug 
    area_of_quater_curve = fact_of_area * total_area
    return area_of_quater_curve * 4 # total area of the curve is 4 * area Of curve in 1st 1st Quadrant

####   main   ####

print( "\n=======================\nArea = {}\n=======================\n"
.format( getRandomAreaCurve( int( input( "Enter the number of iterations : ") )))) # function Call