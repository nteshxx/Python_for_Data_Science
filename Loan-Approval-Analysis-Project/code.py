# --------------
# Importing header files
import numpy as np
import pandas as pd
from scipy.stats import mode 
 
import warnings
warnings.filterwarnings('ignore')


#Reading file
bank_data = pd.read_csv(path)


#Code starts here
#1
bank = pd.DataFrame(bank_data)
categorical_var = bank.select_dtypes(include = 'object')
#print(categorical_var.head())
numerical_var = bank.select_dtypes(include = 'number')
#print(numerical_var.head())
print(categorical_var.shape)
print(numerical_var.shape)

#2
banks = bank.drop(['Loan_ID'],axis=1)

#print(banks.isnull().sum())
bank_mode = banks.mode()
#print(bank_mode)

dict ={'Gender': 'Male', 'Married': 'Yes', 'Dependents': '0', 'Education': 'Graduate', 'Self_Employed': 'No', 'ApplicantIncome':2500, 'CoapplicantIncome': 0.0, 'LoanAmount': 120.0, 'Loan_Amount_Term': 360.0, 'Credit_History': 1.0, 'Property_Area': 'Semiurban', 'Loan_Status': 'Y'}

banks = banks.fillna(value = dict)
print(banks.shape)
print(banks.isnull().sum().values.sum())

#3
avg_loan_amount = banks.groupby(['Gender', 'Married', 'Self_Employed'])[['LoanAmount']].mean()
print(avg_loan_amount['LoanAmount'][1],2)

#4
loan_approved_se = len(banks[(banks["Self_Employed"]=="Yes" )& (banks['Loan_Status']=='Y')])
#print(loan_approved_se)
loan_approved_nse = len(banks[(banks["Self_Employed"]=="No") & (banks['Loan_Status']=='Y')])
#print(loan_approved_nse)
Loan_Status = 614
percentage_se = loan_approved_se / Loan_Status *100
print(percentage_se)
percentage_nse = loan_approved_nse / Loan_Status *100
print(percentage_nse)

#5
def convert(x):
    return x/12

loan_term = banks['Loan_Amount_Term'].apply(lambda x: convert(x))
#print(loan_term)

def separate(x):
    x=convert(x)
    if x>=25 :
        return x

big_loan_term = banks['Loan_Amount_Term'].apply(lambda x: separate(x))
big_loan_term = big_loan_term.dropna()
print(len(big_loan_term))

#6
loan_groupby = banks.groupby(['Loan_Status'])
loan_groupby = loan_groupby['ApplicantIncome', 'Credit_History']
mean_values = loan_groupby.mean()
print(mean_values.iloc[1,0], 2)


