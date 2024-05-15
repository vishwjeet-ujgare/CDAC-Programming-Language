import pandas as pd 
import numpy as np 

iris = pd.read_csv("/home/hpcap/Desktop/Analytics and Statistics/Day_01/iris.csv")
exp_sals = pd.read_csv("/home/hpcap/Desktop/Analytics and Statistics/Day_01/Exp_Salaries.csv")

iris['Sepal.Length'].mean()
iris['Sepal.Length'].median()

a = np.array([45, 48, 56, 42, 35, 38, 40])
print(a.mean())
print(np.median(a))

a = np.array([45, 48, 500, 42, 35, 38, 40])
print(a.mean())
print(np.median(a))

exp_sals['Salary'].mean()
males = exp_sals[exp_sals['Gender']=='Male']
fem = exp_sals[exp_sals['Gender']=='Female']
males['Salary'].mean()
fem['Salary'].mean()
# or
print(exp_sals.groupby('Gender')['Salary'].mean())

print(exp_sals.groupby('Department')['Salary'].mean())

