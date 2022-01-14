import pandas as pd
data = pd.read_excel("F:/GithubBITS/Msdhoni data/MS_Dhoni_ODI_record.xlsx")
#print(data.head(5))

# Converting the date column to datetime format
data["date"]=pd.to_datetime(data["date"])

#  print(data.columns)

# Only using number to represent odi_number
for i in range(len(data)):
    data.odi_number[i]=int(str(data.odi_number[i])[6:])

print(data.odi_number.head(5))
ru=s4=s6=sr=0
for i in range(0, len(data)):
    ru=ru+int(data["runs_scored"][i])
    sr=sr+int(data["strike_rate"][i])
    s4=s4+int(data["fours"][i])
    s6=s6+int(data["sixes"][i])
print(f"Runs:{ru}\nFours:{s4}\nSixes:{s6}\nAverage Strike rate={sr/len(data)}\nMatches Batted in:{len(data)}")

import matplotlib.pyplot as plt
import numpy as np

plt.pie(np.array([s4*4,s6*6,ru-s4*4-s6*6]),labels=["4s","6s","Runs w/o 4s and 6s"],normalize=True,explode = [0.1,0.2,0],autopct='%1.0f%%')
plt.show()

ru=s4=s6=0
opp=str(input("Enter the opposition name: "))
for i in range(0, len(data)):
    if(data.opposition[i][2:]==opp):

        ru=ru+int(data["runs_scored"][i])
        s4=s4+int(data["fours"][i])
        s6=s6+int(data["sixes"][i])
print(f"Runs:{ru}\nFours:{s4}\nSixes:{s6}")

plt.pie(np.array([s4*4,s6*6,ru-s4*4-s6*6]),labels=["4s","6s","Runs w/o 4s and 6s"],normalize=True,explode = [0.1,0.2,0],autopct='%1.0f%%')
plt.show()

ru=s4=s6=0
gnd=str(input("Enter the ground name: "))
for i in range(0, len(data)):
    if(data.ground[i]==gnd):

        ru=ru+int(data["runs_scored"][i])
        s4=s4+int(data["fours"][i])
        s6=s6+int(data["sixes"][i])
print(f"Runs:{ru}\nFours:{s4}\nSixes:{s6}")

plt.pie(np.array([s4*4,s6*6,ru-s4*4-s6*6]),labels=["4s","6s","Runs w/o 4s and 6s"],normalize=True,explode = [0.1,0.2,0],autopct='%1.0f%%')
plt.show()
