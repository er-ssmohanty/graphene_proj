import pandas as pd 
import matplotlib.pyplot as plt


grd = pd.read_csv("data/graphene_data_final.csv")
#Graphene_percentage  FEED   RPM   DOC  MRR_gm_per_sec     Ra

###################TO DO###############################################################
#A plot with subplots showing Graphene and MRR relationsjip with all set of labels   
#######################################################################################
#grd[i].unique()

#for i in grd.columns[1:4]:
#	print("Unique values of {} are {}".format(i,grd[i].unique()))

#FEED_ = int(input("Enter the FEED: "))
#RPM_ = int(input("Enter the rotation speed in RPM: "))
#DOC_ = float(input("Enter the DOC: "))
count_=1
total_subs = len(grd["FEED"].unique())*len(grd["RPM"].unique())*len(grd["DOC"].unique())
for i in grd["FEED"].unique():
	for j in grd["RPM"].unique():
		for k in grd["DOC"].unique():
			grd2 =  grd[(grd["FEED"] == i) & (grd['RPM'] == j) & (grd['DOC'] == k)]
			plt.plot(grd2['Graphene_percentage'],grd2['MRR_gm_per_sec'])
			plt.title(str(i)+' '+str(j)+' '+str(k))
			plt.subplot(7,4,count_)
			count_=count_+1

#plt.ylabel('Ra')
"""
plt.plot(grd2['Graphene_percentage'],grd2['Ra'])
plt.xlabel('Graphene_percentage')
plt.ylabel('Ra')
plt.subplot(1,2,2)
"""
plt.suptitle('Graphene_percentage(X) Vs MRR_gm_per_sec(Y) for given [FEED, RPM, DOC]')
plt.show()
