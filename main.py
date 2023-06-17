import pandas as pd
import csv

score = [90.5,95,84,78.8]
students = ["Proud","Luke","Jim","Jack"]
##
##score_ser = pd.Series(score,index=students)
##print(score_ser)
##
##
##score_ser.name="score"
##print(score_ser)

##print(score_ser[["Proud","Jack"]])
##print(score_ser["Proud":"Jack"])
##
##print("*0:3是012*:",score_ser.iloc[3])

##print("average:",score_ser.mean())
##print("standard deviation:",score_ser.std())
##
##score_ser["nihao"] = 88.8
##print(score_ser)
##print(len(score_ser))
##print(score_ser.shape)
##################################################
##pop_data=[
##["Luke",95,"large"],
##["Proud",90.5,"large"],
##["Jim",84,"Medium"],
##["Jack",78.8,"small"]
##    ]
##header =["Name","Score","Class"]
##pop_df = pd.DataFrame(pop_data,columns=header)
##print(pop_df)
##
##pop_ser3 = pop_df["Name"]
##print(type(pop_ser3))
##print(pop_ser3)
##
##pop_ser4 = pop_df.iloc[:,1]
##print(pop_ser4)
##print(pop_df.iloc[0,1])
##
##pop_df = pop_df.set_index("Name")
##print("12111",pop_df)
##print(pop_df.loc[95]["Score"])
##print(pop_df["Name"]["Luke"])
########################################
pop_data = [
["Shanghai",26.8,"large"],
["Beijing",21.1,"large"],
["Hangzhou",7.9,"Medium"],
["Zibo",2.6,"Small"]
    ]
header = ["City","Population","Class"]
pop_df = pd.DataFrame(pop_data,columns=header)
print(pop_df)

pop_ser3 = pop_df["Population"]
print(type(pop_ser3))
print(pop_ser3)
pop_ser4 = pop_df.iloc[:,1]
print(pop_ser4)
print(pop_df.iloc[0,1])
pop_df = pop_df.set_index("City")
print(pop_df)
print(pop_df.loc["Shanghai"]["Population"])
print(pop_df["Population"]["Shanghai"])

regions_df =pd.read_csv("regions.csv",index_col=0)
print(regions_df)
merged_df = pop_df.merge(regions_df,on=["City"],how="outer")
print(merged_df)
##merged_df.to_csv("merged.csv")
##################################
grouped_by_class = merged_df.groupby("Class")
mean_pop_ser = grouped_by_class["Population"].mean()
print(mean_pop_ser)

mean_pop_ser.name = "Mean Population"
print(mean_pop_ser)
print()

large_df = grouped_by_class.get_group("large")
print(large_df)
print()
large_df2=\
            merged_df[merged_df["Class"] == "large"]
print(large_df2)

####################
print(merged_df["Class"].value_counts())
print()
merged_df=\
            merged_df.sort_values("Population",ascending=False)
print(merged_df)
print()
print(merged_df.isnull())
print(merged_df.isnull().sum())
print(merged_df.isnull().sum().sum())
