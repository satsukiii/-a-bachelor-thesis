
# coding: utf-8

# In[ ]:

import pandas as pd
from pandas import Series,DataFrame
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns


# In[15]:

path = "C:/Users/satsuki/Documents/labo/POS/政府統計/"
kakei =  pd.read_csv(path + "家計消費品目別1.csv",engine='python',encoding = "Shift-JIS",index_col=[0] )


# ##家計消費 一世帯当たり1か月間の支出

# In[42]:

kakei = kakei.T
kakei


# In[36]:

kakei.corr()


# In[41]:

sns.heatmap(kakei.corr(),annot=True)
plt.show()


# In[40]:

plt.imshow(kakei.corr(), interpolation='none')
plt.gray()
plt.show()


# In[ ]:



