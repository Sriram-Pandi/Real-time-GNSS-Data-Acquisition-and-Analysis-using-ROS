import bagpy
from bagpy  import bagreader
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

movbg=bagreader('/home/sriram/EECE5554/LAB1/src/data/movingbag1_2022-09-26-13-45-56.bag')
statbg=bagreader('/home/sriram/EECE5554/LAB1/src/data/statbag1_2022-09-26-13-37-12.bag')
data = movbg.message_by_topic('/gps')
data1 = statbg.message_by_topic('/gps')
df_mov = pd.read_csv(data)
df_stat = pd.read_csv(data1)

df_stat['UTM_northing_std']= df_stat['UTM_northing']- df_stat['UTM_northing'].min()
df_stat['UTM_easting_std']= df_stat['UTM_easting']- df_stat['UTM_easting'].min()

df_stat['Latitude_std']= df_stat['Latitude']- df_stat['Latitude'].min()
df_stat['Longitude_std']= df_stat['Longitude']- df_stat['Longitude'].min()

df_mov['UTM_northing_std']= df_mov['UTM_northing']- df_mov['UTM_northing'].min()
df_mov['UTM_easting_std']= df_mov['UTM_easting']- df_mov['UTM_easting'].min()

df_mov['Latitude_std']= df_mov['Latitude']- df_mov['Latitude'].min()
df_mov['Longitude_std']= df_mov['Longitude']- df_mov['Longitude'].min()


df_stat[['UTM_northing_std','UTM_easting_std']].plot.scatter(x='UTM_northing_std',y='UTM_easting_std')

df_stat[['Latitude_std','Longitude_std']].plot.scatter(x='Latitude_std',y='Longitude_std')

df_mov[['UTM_northing_std','UTM_easting_std']].plot.scatter(x='UTM_northing_std',y='UTM_easting_std')

fig, ax = bagpy.create_fig(1)
ax[0].scatter(x = 'Latitude_std', y = 'Longitude_std', data  = df_mov, s= 1, label = 'Latitude vs Longitude while walking')
ax[0].set(xlabel="Latitude_std",ylabel="Longitude_std")

plt.show()