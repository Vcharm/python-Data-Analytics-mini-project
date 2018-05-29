import pandas as pd
from matplotlib import pyplot as plt
data = pd.read_csv("D:/dataset/Suicide Statistics in Indian States.csv")

#Data Cleaning 
#print(data['Female Involved'].isnull())
data['Female Involved']=data['Female Involved'].fillna(0)
data['Male Involved']=data['Male Involved'].astype('float')




#Data Wrangling
print("Top 5 states on the basis of male and female\n")
df_ML = pd.DataFrame(data,columns=['State/UT','Male Involved','Female Involved'])
sorted_df = df_ML.sort_values(by=['Male Involved','Female Involved'],ascending=False)


#Top 5 states/ut  on Male and Female 
print(sorted_df.iloc[:5])
print("\n\nTop 5 states")


#Top 5 states on Total basis
df_ST = pd.DataFrame(data,columns=['Category','State/UT','Total'])
sort_state = df_ST.sort_values(by=['Total'],ascending=False)
print(sort_state.iloc[:5])



#Visualization

#male Suicide
fig = plt.figure(figsize=(10,60))
fig.subplots_adjust(hspace=5)
ax1 = plt.subplot(311)

plt.bar(sorted_df['State/UT'],sorted_df['Male Involved'],align = 'center',color = 'r')
plt.xlabel("States/UT")
plt.xticks(rotation=90)
plt.ylabel("Male Invloved")
plt.show


#Female Suicide
fig = plt.figure(figsize=(10,60))
fig.subplots_adjust(hspace=5)
ax2 = plt.subplot(312, sharex=ax1)
plt.bar(sorted_df['State/UT'],sorted_df['Female Involved'],align = 'center')
plt.xlabel("States/UT")
plt.xticks(rotation=90)
plt.ylabel("Female Invloved")
plt.show

#total suicides
fig = plt.figure(figsize=(10,60))
fig.subplots_adjust(hspace=5)
ax3 = plt.subplot(313, sharex=ax1, sharey=ax1)
plt.bar(sort_state['State/UT'],sort_state['Total'],align = 'center',color='g')
plt.xlabel("States/UT")
plt.xticks(rotation=90)
plt.ylabel("Total Suicides")
plt.show


    






