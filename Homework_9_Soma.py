
# coding: utf-8

# In[2]:

depth_to_words will describe the earthquake's depth
magnitude_to_words will describe the earthquake's power
day_in_words should be the day of the week
time_in_words should be "morning", "afternoon", "evening" or "night"
date_in_words should be "Monthname day", e.g. "June 22"
Any other functions as necessary


# In[3]:

import pandas as pd 


# In[4]:

df = pd.read_csv('http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/1.0_month.csv')
df.head()


# In[5]:

df = pd.read_csv("http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/1.0_month.csv")
earthquakes = df.to_dict('records')


# In[6]:

df


# In[7]:

earthquakes_df = pd.read_csv("http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/1.0_month.csv")
earthquakes = earthquakes_df.to_dict('records')


# In[8]:

earthquake = earthquakes[0]


# # PART 1
# 
# 
# # variable for depth

# In[9]:

def depth_to_words(earth_dict):
    depth = earth_dict['depth']
    
    if depth < 70:
        depth_descript = "shallow"
    elif (depth > 70) & (depth < 300):
        depth_descript = "intermediate"
    elif (depth >300): 
        depth_descript = "deep"
    else: 
        depth_descript = "no depth recorded"
    return(depth_descript)

depth_to_words(earthquake)


# # variable for magnitude

# In[10]:

def magnitude_to_words(earth_dict):
    magnitude = earth_dict['mag']

    if (magnitude >= 0) & (magnitude <= 2):
        mag_words = "micro"
    elif(magnitude > 2) & (magnitude <= 4):
        mag_words = "minor"
    elif (magnitude > 4) & (magnitude <= 6):
        mag_words = "light"
    elif (magnitude > 6) & (magnitude <= 7):
        mag_words = "moderate"
    elif (magnitude > 7) & (magnitude <= 9):
        mag_words = "strong"
    elif magnitude == 10:
        mag_words = "major"
    else:
        mag_words = "no magnitude was recorded"
    return mag_words

magnitude_to_words(earthquake)


# # variable for day in words

# In[11]:

import dateutil.parser

def day_in_words(earth_dict):
    time = earthquake['time']

    day_of_week = dateutil.parser.parse(time)
    return(day_of_week.strftime("%A"))

day_in_words(earthquake) 


# # variable for time in words

# In[12]:

def time_in_words(earth_dict):
    time = earthquake['time']
    python_time = dateutil.parser.parse(time)
    python_time.strftime("%-H")
    if (python_time.hour >= 00) & (python_time.hour < 12):
        time_of_day = "morning"
    elif (python_time.hour == 12) & (python_time.hour <= 13):
        time_of_day = "noon"
    elif (python_time.hour >= 14) & (python_time.hour < 18):
        time_of_day = "afternoon"
    elif (python_time.hour >= 18) & (python_time.hour < 24):
        time_of_day = "night"   

        
    return(time_of_day)

time_in_words(earthquake)  


# In[13]:

python_time = dateutil.parser.parse('2016-06-14T23:57:34.000Z')


# In[14]:

python_time.hour


# # variable for date in words

# In[15]:

def date_in_words(earth_dict):
    date = earthquake['time']
    month_day = dateutil.parser.parse(date)
    return(month_day.strftime("%b %d"))
date_in_words(earthquake)  


# # PART 2
# # eq_to_sentence function

# In[16]:

def eq_to_sentence(earth_dict):
    depth = depth_to_words(earth_dict)
    mag = magnitude_to_words(earth_dict)
    day= day_in_words(earth_dict)
    daytime= time_in_words(earth_dict)
    date= date_in_words(earth_dict)  
    place = earth_dict['place'] 
       
    return("A" + " " +  depth + " " + mag + " " + "earthquake was reported" + " " +day + " " + daytime + " " + "on" + " " + date + " " +place)

print(eq_to_sentence(earthquake))


# # PART 3
# # Doing it in bulk

# In[17]:

for item in earthquakes:
    if item['mag'] >= 4.0:
        print(eq_to_sentence(item))


# In[ ]:



