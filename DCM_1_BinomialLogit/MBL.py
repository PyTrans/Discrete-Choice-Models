
# coding: utf-8

# In[75]:

import random
import numpy as np
import pandas as pd
import os

directory = r"C:\Users\DANNY\Dropbox\Travel Demand Analysis 2_220B\HW\HW1\MNL Estimation"
os.chdir(directory)


dta = pd.read_csv("CEE220B_Exercise_1_Data.csv")


# In[82]:

dta.loc[dta["Chosen Alternative"]=="Bus", "y_bus"]=1
dta.loc[dta["Chosen Alternative"]=="Bus", "y_car"]=0
dta.loc[dta["Chosen Alternative"]=="Car", "y_car"]=1
dta.loc[dta["Chosen Alternative"]=="Car", "y_bus"]=0

dta["x_01"]=0.0
dta["x_02"]=1.0
# 

# In[ ]:

theta = 1
tempmatrix = pd.DataFrame(columns = ["U_bus","U_car","exp_U_bus","exp_U_car"])


theta_car = 1.0
theta_bus = 0.0

theta_t_car = 1.0
theta_t_bus = 1.0
tempmatrix["U_bus"] = theta_t_bus*dta["Time by Bus Minutes"]
tempmatrix["U_car"] = theta_t_car*dta["Time by Car (Minutes)"]+theta_car

tempmatrix["exp_U_bus"] = np.exp(tempmatrix["U_bus"])
tempmatrix["exp_U_car"] = np.exp(tempmatrix["U_car"])

tempmatrix["Pr_bus"] = tempmatrix["exp_U_bus"]/(tempmatrix["exp_U_bus"]+tempmatrix["exp_U_car"])
tempmatrix["Pr_car"] = tempmatrix["exp_U_car"]/(tempmatrix["exp_U_bus"]+tempmatrix["exp_U_car"])

f = [0.0,0.0]
x0 = {"car":1,"bus":0}
for n in range(0,len(tempmatrix)):
    for i in ["bus","car"]:
        y_i = dta["y_"+i][n]
        if i =="bus":
            x_i = dta["x_01"][n]
        elif i =="car":
            x_i = dta["x_02"][n]
        
        x_bus = dta["Time by Bus Minutes"][n]
        x_car = dta["Time by Car (Minutes)"][n]
        pr_bus = tempmatrix["Pr_bus"][n]
        pr_car = tempmatrix["Pr_car"][n]
        f0 = y_i*(x0[i]-x_0bus*pr_bus-x_0car*pr_car)
        f1 = y_i*(x0[i]-x_bus*pr_bus-x_car*pr_car)
        f[0] +=f0
        f[1] +=f1
        print n, i, f0, f1
                    
         
    
