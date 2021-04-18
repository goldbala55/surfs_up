# Surfs_up Challenge
Surf Shop weather analysis
## Project Overview
 Our principal investor has requested additional information on Oahu weather trends for the months of June and December.  The goal is to determine if there will be sufficient business to sustain a surf/ice cream business year-round.

## Resources
Supplied Hawaii weather observations - SQLite DB

Software: Python 3.7.9, Jupyter Notebook 6.1.4, pandas 1.1.3, numpy 1.17.0
1. Git Bash 4.4.23
2. SQLite 3.35.4, sqlalchemy 1.3.20

## Results Analysis
In reviewing the monthly weather metrics we can observe the following:
* The December weather range is in a comfortable range averaging 71 degrees with an IQR of 69-74 degrees.  This is likely to be attractive to Northern US residents where it will be winter.  [December Temperature Stats](https://github.com/goldbala55/surfs_up/blob/main/December_Hawaii_Temperature_Statistics.png)
* June temperatures warm quite a bit to an average of 75 degrees and an IQR of 73-77 degrees.  But this will likely be appealing to surfers. [June Temperature Stats](https://github.com/goldbala55/surfs_up/blob/main/June_Hawaii_Temperature_Statistics.png)
* By looking at our annual temperature distribution we can conclude that both month's ranges fall within the predominant temperature patterns. [Hawaii Annual Temperature Distribution](https://github.com/goldbala55/surfs_up/blob/main/Annual_Hawaii_Temperature_Distribution.png)

## Summary Recommendations
The weather analysis indicates there is a strong probability of success for the new business. Some additional weather analysis options:
1. Check daytime precipitation patterns during June/December; ice cream and surfing sales will weaken if there are extended periods of rain during the day.
2. rerun the temperature analysis looking only at daytime hours.  Not too many people surf at night so better daytime temperatures will drive business.
3. One non-weather observation.  Collect and analyze local hotel occupancy rates along with the weather data.  Tourists can provide a substantial boost to the business.