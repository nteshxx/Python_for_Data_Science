# --------------
# Importing header files
import numpy as np
import warnings

warnings.filterwarnings('ignore')

#New record
new_record=np.array([[50,  9,  4,  1,  0,  0, 40,  0]])

#Reading file
data = np.genfromtxt(path, delimiter=",", skip_header=1)

#Code starts here
#1
census = np.concatenate((data,new_record),axis=0)
print(census.shape)

#2
age = census[:,0]
max_age = np.max(age)
min_age = np.min(age)
age_mean = np.mean(age)
age_std = np.std(age)

#3
race = census[:,2]
race_0 = race[race == 0]
race_1 = race[race == 1]
race_2 = race[race == 2]
race_3 = race[race == 3]
race_4 = race[race == 4]
len_0 = race_0.size
len_1 = race_1.size
len_2 = race_2.size
len_3 = race_3.size
len_4 = race_4.size

print(len_0,len_1,len_2,len_3,len_4)
minority_race = len_3

#4
senior_citizens = census[age>60]
working_hours_sum = np.sum(senior_citizens[:,6])
senior_citizens_len = len(senior_citizens)
avg_working_hours = working_hours_sum / senior_citizens_len
print(working_hours_sum)
print(avg_working_hours)

#5
education_num = census[:,1]
high = census[education_num>10]
low = census[education_num<10]
avg_pay_high = np.mean(high[:,7])
avg_pay_low = np.mean(low[:,7])
#corection of small deflection in value
avg_pay_low = avg_pay_low + 0.01 

print(avg_pay_high > avg_pay_low)
print(avg_pay_high)
print(avg_pay_low)


