#!/usr/bin/env python
# coding: utf-8

# In[4]:


# Initial Code to calculate prevalence, mortality rate, and years of potential life
#lost using the given data

#Master Calculator - this calculator should woprk for all cases
#intput promts
case_old = int(input("How many cases were reported before the new wave?:"))
case_new = int(input("How many new cases have been reported?:"))
pop = float(input("How many people, in millions, comprises the population?: "))
death_n = int(input("How many people have died along the time-frame?:"))
print("If ages are not given, please write 77")
death_age1 = int(input("What was the age of the first person who passed?: "))
death_age2 = int(input("What was the age of the second person who passed?: "))
death_age3 = int(input("What was the age of the third person who passed?: "))
death_age4 = int(input("What was the age of the fourth person who passed?: "))
death_age5 = int(input("What was the age of the fifth person who passed?: "))
#I would love to discuss with you on how to create a list which then is used to calculate in a loop the value for the ypll, and multiple variable input
print("""******************************
Thank you for your input!
The following statistics are:
******************************""")

#Variables
case_total = case_old + case_new
avg_age = 77
ypll = 0
pop *= 10**6

#incidence Calculator
incidence = (case_new/pop)*1000
incidence = round(incidence, 4)
print("There seems to be an Incidence of", incidence, "per 1000 people")

#Prevalence Calculator
prevalence = (case_total- death_n)/pop*1000
prevalence = round(prevalence, 4)
print("There seems to be a Prevalence of", prevalence, "per 1000 people")

#Mortality Rate
mortality_r = (death_n / case_total)*1000
mortality_r = round(mortality_r, 4)
print("The mortality Rate for people with this disease is:", mortality_r, "per 1000 people with this disease")

#Mortality Rate time period
mortality_ti = (death_n / case_new)*1000
mortality_ti = round(mortality_ti, 4)
print("The mortality Rate for people with this disease is:", mortality_ti, "per 1000 people within the timeframe of infection")

#YPLL Calculator
ypll_a1 = avg_age - death_age1
ypll_a2 = avg_age - death_age2
ypll_a3 = avg_age - death_age3
ypll_a4 = avg_age - death_age4
ypll_a5 = avg_age - death_age5

if ypll_a1 >= 0:
    ypll += ypll_a1
else:
    ypll_a1 = 0
    ypll += ypll_a1

if ypll_a2 >= 0:
    ypll += ypll_a2
else:
    ypll_a2 = 0
    ypll += ypll_a2

if ypll_a3 >= 0:
    ypll += ypll_a3
else:
    ypll_a3 = 0
    ypll += ypll_a3

if ypll_a4 >= 0:
    ypll += ypll_a4
else:
    ypll_a4 = 0
    ypll += ypll_a4

if ypll_a5 >= 0:
    ypll += ypll_a5
else:
    ypll_a5 = 0
    ypll += ypll_a5

print("Your Years of Potential Life Lost (if aplicable) are:", ypll, "years")




# In[ ]:





# In[ ]:




