# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
pd.options.mode.chained_assignment = None #to supress SettingWithCopyWarning

#Path of the file is stored in the variable path

#Code starts here

# Data Loading 
data = pd.read_csv(r'dataset.csv')
data = data.rename({'Total':'Total_Medals'},axis='columns')

# Summer or Winter
data = data.drop(146)
data['Better_Event'] = np.where(data['Total_Summer']>=data['Total_Winter'], 'Summer', 'Winter')

data['Better_Event'].fillna('Both')
Better_event = data['Better_Event'].value_counts()
print(Better_event)
#based on the Better_Event output
better_event = 'Summer'

# Top 10
top_countries = data.take([0,5, 10,15],axis=1)
#top_countries = top_countries.drop(146)

def top_ten(df,col):
    top_ten = df.nlargest(10, col)
    country_list = list(top_ten['Country_Name'])
    return country_list

top_10_summer = top_ten(top_countries,'Total_Summer')
#print(top_10_summer)
top_10_winter = top_ten(top_countries,'Total_Winter')
#print(top_10_winter)
top_10 = top_ten(top_countries,'Total_Medals')
#print(top_10)

set1 = set(top_10)
set2 = set(top_10_summer)
set3 = set(top_10_winter)
setx = set1.intersection(set2)
common = setx.intersection(set3) 
print(common)
# Plotting top 10
summer_df = data[data['Country_Name'].isin(top_10_summer)]
winter_df = data[data['Country_Name'].isin(top_10_winter)]
#print(winter_df)
top_df = data[data['Country_Name'].isin(top_10)]

summer_df.plot(kind='bar',x='Country_Name',y='Total_Summer')
plt.xlabel("Countries")
plt.ylabel('Total Medals won in Summer')
plt.title('Top 10 in Summer Olympics')
plt.show()

winter_df.plot(kind='bar',x='Country_Name',y='Total_Winter')
plt.xlabel("Countries")
plt.ylabel('Total Medals won in Winter')
plt.title('Top 10 in Winter Olympics')
plt.show()

top_df.plot(kind='bar',x='Country_Name',y='Total_Medals')
plt.xlabel("Countries")
plt.ylabel('Total Medals won in Olympics')
plt.title('Top 10 All-time Olympics')
plt.show()

# Top Performing Countries
summer_df['Golden_Ratio'] = summer_df['Gold_Summer'] / summer_df['Total_Summer']
summer_max_ratio=max(summer_df['Golden_Ratio'])
summer_country_gold=summer_df.loc[summer_df['Golden_Ratio'].idxmax(),'Country_Name']

winter_df['Golden_Ratio'] = winter_df['Gold_Winter'] / winter_df['Total_Winter']
winter_max_ratio = max(winter_df['Golden_Ratio'])
winter_country_gold = winter_df.loc[winter_df['Golden_Ratio'].idxmax(),'Country_Name']

top_df['Golden_Ratio'] = top_df['Gold_Total'] / top_df['Total_Medals']
top_max_ratio = max(top_df['Golden_Ratio'])
top_country_gold = top_df.loc[top_df['Golden_Ratio'].idxmax(),'Country_Name']

# Best in the world 
data_1 = data
data_1['Total_Points'] = data_1['Gold_Total']*3 + data_1['Silver_Total']*2 + data_1['Bronze_Total']

data_1 = data_1.sort_values(by=['Total_Points'],ascending=False)
most_points = data_1['Total_Points'].max()
best_country = data_1.iloc[0]['Country_Name']
print(best_country)

# Plotting the best
best = data[ data['Country_Name']==best_country ]
best = best.take([12,13,14],axis = 1)
print(best)
best.plot.bar(stacked = True)
plt.xlabel('United States')
plt.ylabel('Medals Tally')
plt.xticks(rotation = 45)



