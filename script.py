import codecademylib3_seaborn
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Import CSVs:
user_data = pd.read_csv("user_data.csv")
pop_data = pd.read_csv("pop_data.csv")

# Merged tables with location data:
new_df = pd.merge(user_data, pop_data)
new_df.loc[new_df.population_proper < 100000, "location"] = "rural"
new_df.loc[new_df.population_proper >= 100000, "location"] = "urban"

# Paste histogram code:
age = new_df["age"]
sns.displot(age)
 
plt.show()

# Paste mean age location code:
location_mean_age = new_df.groupby("location").age.mean() 
 
print(location_mean_age)

# Paste barplot code:
plt.close()
sns.barplot(
    data=new_df,
    x= "location",
    y= "age"
)
plt.show()

# Paste violinplot code:
plt.close()
sns.violinplot(x="location", y="age", data=new_df)
 
plt.show()
