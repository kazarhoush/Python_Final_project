
# coding: utf-8

# In[ ]:


# Count Vowels - Enter a string and the program counts the number of vowels in the text. 
# For added complexity have it report a sum of each vowel found.

print "Check the count of vowels in a word or sentence."
sen = str(raw_input("Enter sentence or word here: "))

word_list = [str(char).lower() for char in sen]

x = word_list.count('a')
y = word_list.count('e')
z = word_list.count('i')
ab = word_list.count('o')
bc = word_list.count('u')

num_count = x + y + z + ab + bc
print "The vowel count is {}".format(num_count)


# Distance Between Two Cities - Calculates the distance between two cities and allows the user to specify a unit of distance. This program may require finding coordinates for the cities like latitude and longitude.

# In[ ]:

from geopy.geocoders import Nominatim
from geopy.distance import great_circle

print "Calculate the distance between two cities and specify a unit of distance."
print "\n"

city = str(raw_input("Enter city and state or country: "))
print "\n"

city2 = str(raw_input("Enter city and state or country: "))
print "\n"

print "Please choose your preferred measurement."
print "\n"

m = str(raw_input("Enter m for miles: ")).lower()
print "\n"
k = str(raw_input("Enter km for kilometers: ")).lower()
print "\n"
f = str(raw_input("Enter ft for feet: ")).lower()

geolocator = Nominatim()
location = geolocator.geocode(city)
location2 = geolocator.geocode(city2)

address1 = location.address
address2 = location2.address

x = location.latitude, location.longitude
y = location2.latitude, location2.longitude

mile = great_circle(x, y).miles
kilometers = great_circle(x, y).kilometers
feet = great_circle(x, y).feet


if m == 'm':
    a1 = "The distance between {0} and {1} is {2} miles.".format(address1.encode('utf-8'), address2.encode('utf-8'), round(mile))
    print a1
    print "\n"
if k == 'km':
    a2 = "The distance between {0} and {1} is {2} kilometers.".format()
    print a2
    print "\n"
if f == 'ft':
    a3 = "The distance between {0} and {1} is {2} feet.".format()
    print a3
    print "\n"

