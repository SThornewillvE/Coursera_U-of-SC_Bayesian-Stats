# -*- coding: utf-8 -*-
"""
Created on Fri Feb  7 09:45:32 2020

@author: sthornewillvonessen
"""

# Import pandas
import pandas as pd

# Import csv
df = pd.read_csv("./dat/RENPHO-Simon_raw.csv")

# Rename columns
df.columns = ["timestamp", "mass_kg", "bmi", "body_fat_perc", 
              "fat_free_mass_kg", "subcutan_fat_perc", "viceral_fat", 
              "water_perc", "skeletal_mass_kg", "muscle_mass_kg", "bone_mass_kg", "protein_perc", 
              "bmr_kcal", "metabolic_age_yr"]

# Clean data of units
df["timestamp"] = pd.to_datetime(df["timestamp"])

for perc_metric in ["body_fat_perc", "subcutan_fat_perc", "water_perc", "protein_perc", ]:
    df[perc_metric] = df[perc_metric].apply(lambda x: float(x[:-1]))

for kg_metric in ["mass_kg", "fat_free_mass_kg", "skeletal_mass_kg", "muscle_mass_kg", "bone_mass_kg"]:
    df[kg_metric] = df[kg_metric].apply(lambda x: float(x[:-2]))
    
df["bmr_kcal"] = df["bmr_kcal"].apply(lambda x: int(x[:-4]))

# Unpack timestamps to interesting variables
nrow = len(df)

timestamps = df["timestamp"]
year = pd.Series([2020 for i in range(nrow)])
month = timestamps.apply(lambda x: x.month)
days_of_week = timestamps.apply(lambda x: x.dayofweek)
week_of_year = timestamps.apply(lambda x: x.weekofyear)

df_dateparse = pd.DataFrame({"timestamp": timestamps,
                             "year": year,
                             "month": month,
                             "days_of_week": days_of_week,
                             "week_of_year": week_of_year})

# Create dummy variables
df_dateparse_dummies = pd.get_dummies(df_dateparse, columns=["year", "month", "days_of_week", "week_of_year"])

# Join together with good ordering of cols
df_dateparse = df_dateparse.merge(df_dateparse_dummies, on="timestamp")
df_clean = df_dateparse.merge(df, on="timestamp")

# Save dataframe
df_clean.to_csv("./dat/RENPHO-Simon_clean.csv", index=False)
