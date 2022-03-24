## QUIZ FUNCTIONS

# question
# This function converts miles to kilometers (km). Complete the function to return the result of the conversion Call the function to convert the trip distance from miles to kilometers 
# Fill in the blank to print the result of the conversion. Calculate the round-trip in kilometers by doubling the result, and fill in the blank to print the result  

def convert_distance(miles):
	km = miles * 1.6  # approximately 1.6 km in 1 mile
	return(km)

my_trip_miles = 55

# 2) Convert my_trip_miles to kilometers by calling the function above
my_trip_km = convert_distance(my_trip_miles)

# 3) Fill in the blank to print the result of the conversion
print("The distance in kilometers is " + str(my_trip_km))
#RD2 = round others
mytriips=my_trip_km*2

# 4) Calculate the round-trip in kilometers by doubling the result,
#    and fill in the blank to print the result
print("The round-trip in kilometers is " + str(mytriips))