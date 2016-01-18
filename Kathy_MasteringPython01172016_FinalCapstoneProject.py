
# coding: utf-8

# In[1]:

#count vowels=enter a string and the program counts the number of vowels in the text.  have it report sum of each vowel
Text=str(raw_input('Enter a text: ')).lower()
vowelfound=[x for x in Text]
Acount=vowelfound.count('a')
Ecount=vowelfound.count('e')
Icount=vowelfound.count('i')
Ocount=vowelfound.count('o')
Ucount=vowelfound.count('u')
Sum=Acount+Ecount+Ocount+Ucount
vowelscount={"A": Acount, "E": Ecount, "I": Icount, "O": Ocount, "U": Ucount}
print 'The count for each vowel is:{}'.format(vowelscount)
print 'The total vowel count is: {}'.format(Sum)


# In[7]:

#Distance between two cities - calculates the distance between 2 cities, and their states and/or country and allows the user to specify
#a unit of distance.  This program may require finding coordinates for the cities like latitude and longtitude
from geopy.geocoders import Nominatim
from geopy.distance import great_circle

City1=str(raw_input('Enter the origin city, state, or country: ')).lower()
City2=str(raw_input('Enter the distination city, state, or country: ')).lower()

msr=str(raw_input('Choose a preferred measure: m for miles, km for kilometer, or ft for feet:')).lower()

geolocator = Nominatim()
location1 = geolocator.geocode(City1)
City1_long_lat=((location1.latitude, location1.longitude))
print City1_long_lat

location2 = geolocator.geocode(City2)
City2_long_lat=((location2.latitude, location2.longitude))
print City2_long_lat

if msr=='m':
    print(great_circle(City2_long_lat, City1_long_lat).miles)
if msr=='km':
    print(great_circle(City2_long_lat, City1_long_lat).kilometers)
if msr=='ft':
    print(great_circle(City2_long_lat, City1_long_lat).feet)








# In[ ]:




# In[ ]:



