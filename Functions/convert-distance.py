def convert_distance(miles):
    km = miles * 1.6 #approximately 1.6km in 1 mile
    return km

miles = 55    #input from user
km = convert_distnace(miles)
print("The distance in kilometers is: " + str(km))
print("The round-trip in kilometers is: " + str(km * 2))
