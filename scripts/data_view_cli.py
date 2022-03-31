import pandas as pd 
import matplotlib.pyplot as plt

grd = pd.read_csv("../data/graphene_data_final.csv")
#Graphene_percentage  FEED   RPM   DOC  MRR_gm_per_sec     Ra


for i in grd.columns[1:4]:
	print("Unique values of {} are {}".format(i,grd[i].unique()))

FEED_ = int(input("Enter the FEED: "))
RPM_ = int(input("Enter the rotation speed in RPM: "))
DOC_ = float(input("Enter the DOC: "))




grd2 =  grd[(grd["FEED"] == FEED_) & (grd['RPM'] == RPM_) & (grd['DOC'] == DOC_)]



plt.plot(grd2['Graphene_percentage'],grd2['MRR_gm_per_sec'])
plt.xlabel('Graphene_percentage')
plt.ylabel('Ra')
plt.subplot(1,2,1)

plt.plot(grd2['Graphene_percentage'],grd2['Ra'])
plt.xlabel('Graphene_percentage')
plt.ylabel('Ra')
plt.subplot(1,2,2)

plt.show()
