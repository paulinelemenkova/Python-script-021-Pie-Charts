#!/usr/bin/env python
# coding: utf-8

# In[82]:


# library
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import os
os.chdir('/Users/pauline/Documents/Python')
dfM = pd.read_csv("Tab-Morph.csv")
 
# dataset
df = pd.DataFrame({'Pacific Plate':dfM.plate_pacif, 
                   'Philippine Plate':dfM.plate_phill,
                   'Mariana Plate':dfM.plate_maria, 
                   'Caroline Plate':dfM.plate_carol},
                  index=dfM.profile)

#ax = plt.subplot(111) 
#wedges, texts = ax.pie(np.abs(np.random.randn(5)))
#for w in wedges:
 #   w.set_linewidth(3)
 #   w.set_edgecolor('r')

#plt.rcParams['patch.linewidth'] = 3 
#plt.rcParams['patch.edgecolor'] = 'white'

# plot chart
df.plot(kind='pie', subplots=True, figsize=(10, 10),  legend=False, table=False, 
        fontsize=8, 
        sort_columns=True,
        layout=(2, 2), colormap='tab20b', 
        title='Mariana Trench: Pie Charts for the \nBathymetry distribution by tectonic plates', 
       )

plt.show()


# In[ ]:





# In[ ]:




