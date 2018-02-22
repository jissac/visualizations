import matplotlib.pyplot as plt
import seaborn as sb
import pandas as pd
import numpy as np

sb.set_style('white')

''' Hepatitus A cases heatmap'''
hepatitus_data = pd.read_csv('C:\Users\JISSAC3\Desktop\HEPATITIS_A_Cases_1966-2012.csv', skiprows=2, na_values='-')
hepatitus_years = list(hepatitus_data['YEAR'].unique())
hepatitus_states = hepatitus_data.drop(['YEAR', 'WEEK'], axis=1).columns.values
hepatitus_states = [state.title() for state in hepatitus_states]

hepatitus_data.drop(['WEEK'], axis=1, inplace=True)
hepatitus_data = hepatitus_data.groupby('YEAR').sum()
hepatitus_data = hepatitus_data.transpose().values
                                  
plt.figure(figsize= (12,12))
sb.heatmap(hepatitus_data, cmap='Reds', robust=True, 
           xticklabels=[year if year%5 == 0 or year ==max(hepatitus_years)
           else '' for year in hepatitus_years],
           yticklabels=hepatitus_states)
plt.plot([hepatitus_years.index(1995) + 0.425, hepatitus_years.index(1995) + 0.425],
          [0, 51],
          color='black', lw=2.5)

cax = plt.gcf().axes[-1]
cax.set_yticklabels([600, 1200, 1800, 2400, '3000+'])
cax.tick_params(labelsize=12)

plt.xticks(fontsize=12)
plt.yticks(fontsize=12)

plt.text(0, 51.5, 'Hepatitus A cases in the United States', fontsize=14)
plt.text(hepatitus_years.index(1995) + 0.15, 51.5, 'Vaccine introduced', fontsize=12, weight='bold')
plt.text(-8, -4, 'Data source: Project Tycho (tycho.pitt.edu) ', fontsize=10)
plt.savefig('hepatitusA-cases-heatmap-sequential-colormap.png', bbox_inches='tight')

''' Hepatitus cases line plot'''
hepatitus_data = pd.read_csv('C:\Users\JISSAC3\Desktop\HEPATITIS_A_Cases_1966-2012.csv', skiprows=2, na_values='-').fillna(0.)
hepatitus_data.drop(['WEEK'], axis=1, inplace=True)
hepatitus_data = hepatitus_data.groupby('YEAR').sum()

maxval = max(hepatitus_data.values.flatten())
hepatitus_data.plot(color='#3F5D7D', alpha = 0.50, lw=0.5, legend=False, figsize=(10,7))
plt.plot([1995,1995], color='black', lw=1.5)

hepatitus_data.transpose().median().plot(color='#3F5D7D', lw=2)
plt.yticks(fontsize=12)
plt.xticks(fontsize=12)
plt.ylim([0,maxval])
plt.xlabel('')
plt.ylabel('# cases per 100,000 people', fontsize=14)

plt.text(1928.5, 163, 'Polio cases in the United States', fontsize=14)
plt.text(1954.75, 163, 'Vaccine introduced', fontsize=12, weight='bold')
plt.text(1924, -17, 'Data source: Project Tycho (tycho.pitt.edu) '
         '| Author: Randy Olson (randalolson.com / @randal_olson)',
         fontsize=10)