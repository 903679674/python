#!/usr/bin/env python3
import pandas as pd

# Read the data set into a pandas DataFrame
f1=open('北京2018年天气数据.csv')
Beijing = pd.read_csv(f1, sep=',', header=0)
Beijing.columns = Beijing.columns.str.replace(' ', '_')
print(Beijing.info())
print(Beijing.head())
print(Beijing.tail())
Beijing['MaximumTemperature'].fillna(Beijing['MaximumTemperature'].mean(),inplace=True)
Beijing['MinimumTemperature'].fillna(Beijing['MinimumTemperature'].mean(),inplace=True)

print(Beijing.describe())
print(sorted(Beijing.MaximumTemperature.unique()))
print(Beijing.MaximumTemperature.value_counts())
print(sorted(Beijing.MinimumTemperature.unique()))
print(Beijing.MinimumTemperature.value_counts())

# Read the data set into a pandas 
f2=open('大连2018年天气数据.csv')
Dalian = pd.read_csv(f2, sep=',', header=0)
Dalian.columns = Dalian.columns.str.replace(' ', '_')
print(Dalian.info())
print(Dalian.head())
print(Dalian.tail())
Dalian['MaximumTemperature'].fillna(Dalian['MaximumTemperature'].mean(),inplace=True)
Dalian['MinimumTemperature'].fillna(Dalian['MinimumTemperature'].mean(),inplace=True)

print(Dalian.describe())
print(sorted(Dalian.MaximumTemperature.unique()))
print(Dalian.MaximumTemperature.value_counts())
print(sorted(Dalian.MinimumTemperature.unique()))
print(Dalian.MinimumTemperature.value_counts())