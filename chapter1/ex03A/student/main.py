# Write your code here
distance_in_miles = 60
time_in_hours = 3

distanceInKnots = distance_in_miles/1.15078
distanceInFeet = distance_in_miles*5280
timeInSeconds = time_in_hours * 3600
speedInKnots = distanceInKnots/time_in_hours
speedInMilesPerHour = distance_in_miles/time_in_hours
speedInFeetPerSecond = distanceInFeet/timeInSeconds

print ("The speed in feet per second is " + str(speedInFeetPerSecond))
print("The speed in knots is: " + str(speedInKnots))
print("the speed in miles per hour is " + str(speedInMilesPerHour))

