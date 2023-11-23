#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install plotly')


# In[2]:


get_ipython().system('pip install cufflinks')


# In[3]:


get_ipython().system('pip install chart_studio')


# # Import

# In[4]:


import pandas as pd
import numpy as np
import chart_studio.plotly as py
import cufflinks as cf
import seaborn as sns
import plotly.express as px
get_ipython().run_line_magic('matplotlib', 'inline')


#plotly to work in jupyter notebook
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
init_notebook_mode(connected= True)
#to everything work locally,
cf.go_offline()


# # Basics

# In[5]:


arr_1 = np.random.rand(50,4)
df_1 = pd.DataFrame(arr_1,columns=['A','B','C','D'])
df_1.head()


# In[36]:


#to compare the old plots
df_1.iplot()


# # Line Plots

# In[7]:


import plotly.graph_objects as go
df_stock = px.data.stocks() #this data is built in plotly
df_stock.head()


# In[8]:


px.line(df_stock,x='date',y='GOOG',labels={'x':'Date','y':'Price'})


# In[9]:


px.line(df_stock,x='date',y=['GOOG','AAPL'], labels={'x':'Date','y':'price'},title = 'Apple Vs. Google')


# In[10]:


fig = go.Figure()
fig.add_trace(go.Scatter(x=df_stock['date'],y=df_stock['AAPL'],mode='lines',name='Apple'))
fig.add_trace(go.Scatter(x=df_stock['date'],y=df_stock['AMZN'],mode='lines+markers',name='Amazon'))
fig.add_trace(go.Scatter(x=df_stock['date'],y=df_stock['GOOG'],mode='lines+markers',name='Google',line=dict(color='firebrick',width=2,dash='dashdot')))
fig.update_layout(title = 'Stock Price Data 2018-2020', xaxis_title='Date',yaxis_title='Price')


# In[11]:


#with a new layout
fig = go.Figure()
fig.add_trace(go.Scatter(x=df_stock['date'],y=df_stock['AAPL'],mode='lines',name='Apple'))
fig.add_trace(go.Scatter(x=df_stock['date'],y=df_stock['AMZN'],mode='lines+markers',name='Amazon'))
fig.add_trace(go.Scatter(x=df_stock['date'],y=df_stock['GOOG'],mode='lines+markers',name='Google',line=dict(color='firebrick',width=2,dash='dashdot')))
# fig.update_layout(title = 'Stock Price Data 2018-2020', xaxis_title='Date',yaxis_title='Price')

fig.update_layout(
xaxis=dict(
showline=True,showgrid=False,showticklabels=True,linecolor='rgb(204,204,204)',linewidth=2,ticks='outside',tickfont=dict(
family='Arial', size=12,color='rgb(82,82,82)')),

yaxis=dict(showgrid=False,zeroline=False,showline=False,showticklabels=False),autosize=False,margin=dict(autoexpand=False,l=100,r=20,t=110,),
showlegend=False,plot_bgcolor='white')


# # Bar Charts

# In[12]:


df_us = px.data.gapminder().query("country=='United States'")
df_us


# In[13]:


px.bar(df_us,x='year',y='pop')


# In[14]:


#stracked bar graph
df_tips = px.data.tips()
df_tips


# In[15]:


px.bar(df_tips,x='day',y='tip',color='sex',title='Tips by Gender on each day',labels={'tip':"Tip Amount",'day':'Day of the week'})


# In[16]:


px.bar(df_tips,x='sex',y='total_bill',color='smoker',barmode='group')


# In[17]:


df_europe = px.data.gapminder().query("continent=='Europe' and year == 2007 and pop > 2.e6")
df_europe


# In[18]:


fig = px.bar(df_europe, y='pop', x='country', text='pop',color='country')
fig
fig.update_traces(texttemplate='%{text:.2s}',textposition='outside')
fig.update_layout(uniformtext_minsize=8)
fig.update_layout(xaxis_tickangle=-45)


# # Scatter Plots

# In[19]:


df_iris = px.data.iris()
df_iris


# In[20]:


px.scatter(df_iris,x='sepal_width',y='sepal_length',color='species',size='petal_length',hover_data=['petal_width'])


# In[21]:


fig = go.Figure()
fig.add_trace(go.Scatter(x=df_iris.sepal_width,y=df_iris.sepal_length,mode='markers',marker_color=df_iris.sepal_width,text=df_iris['species'],marker=dict(showscale=True)))
fig.update_traces(marker_line_width=2,marker_size=10)


# In[22]:


fig = go.Figure(data=go.Scattergl(
x=np.random.randn(10000),
y=np.random.randn(10000),
mode='markers',
marker=dict(color=np.random.randn(10000),
           colorscale='Viridis',
           line_width=1)))
fig


# # Pie Charts

# In[23]:


#to get largest nations in Asia
df_asia = px.data.gapminder().query("year == 2007").query("continent== 'Asia'")
df_asia


# In[24]:


px.pie(df_asia,values='pop',names='country',title= 'Population of Asian Continent',
      color_discrete_sequence=px.colors.sequential.RdBu)


# In[25]:


colors = ['blue','green','black','purple','red','brown']
fig = go.Figure(data=[go.Pie(labels=['Water','Grass','Normal','Psychic','Fire','Groud'],
                            values=[110,90,80,80,70,60])])
fig


# In[26]:


fig.update_traces(hoverinfo = 'label+percent',textfont_size=20,textinfo='label+percent',pull=[0.1,0,0.2,0,0,0],
                 marker=dict(colors=colors, line=dict(color='#ff0000')))
fig


# # Histogram

# In[27]:


dice_1 = np.random.randint(1,7,5000)
dice_2 = np.random.randint(1,7,5000)
dice_sum = dice_1 + dice_2
fig = px.histogram(dice_sum,nbins=11,
                   labels={'value':'Dice Roll'},
                  title='5000 Dice Roll Histogram',
                  marginal = 'violin',
                  color_discrete_sequence = ['green'])
fig


# In[28]:


fig.update_layout(
xaxis_title_text = 'Dice Roll',
yaxis_title_text = 'Dice sum',
bargap=0.2,showlegend= False)
fig


# In[29]:


df_tips = px.data.tips()
px.histogram(df_tips,x='total_bill',color='sex')


# # Box Plots

# In[30]:


df_tips=px.data.tips()
px.box(df_tips,x='sex',y='tip',points='all')


# In[31]:


px.box(df_tips,x='day',y='tip',color='sex')


# In[32]:


fig = go.Figure()
fig.add_trace(go.Box(x=df_tips.sex,y=df_tips.tip,
                     marker_color='blue',
                    boxmean='sd'))


# In[33]:


df_stocks = px.data.stocks()
fig = go.Figure()
fig.add_trace(go.Box(y=df_stocks.AAPL,boxpoints='all',
                    fillcolor='blue',jitter =0.5,
                    whiskerwidth=0.2))
fig.add_trace(go.Box(y=df_stocks.GOOG,boxpoints='all',
                    fillcolor='red',jitter =0.5,
                    whiskerwidth=0.2))
fig.update_layout(title="Apple Vs. Google",
                 yaxis= dict(gridcolor='rgb(255,255,255)',
                            gridwidth=3),
                 paper_bgcolor='rgb(243,243,243)',
                 plot_bgcolor='rgb(243,243,243)')


# # Violin Plots

# In[34]:


df_tips = px.data.tips()
px.violin(df_tips, y='total_bill',box=True,points='all')


# In[38]:


px.violin(df_tips,y='tip',x='smoker',color='sex',box=True,points='all',hover_data=df_tips.columns)


# In[41]:


#whether customer smokes or not
fig = go.Figure()
fig.add_trace(go.Violin(x=df_tips['day'][df_tips['smoker']=='Yes'],y=df_tips['total_bill'][df_tips['smoker']=='Yes'],
                        legendgroup='Yes',scalegroup='Yes',name='Yes',
                       side='negative',line_color='purple'))
fig.add_trace(go.Violin(x=df_tips['day'][df_tips['smoker']=='No'],y=df_tips['total_bill'][df_tips['smoker']=='No'],
                        legendgroup='Yes',scalegroup='Yes',name='No',
                       side='positive',line_color='red'))


# # Density Heatmap

# In[42]:


flights = sns.load_dataset('flights')
flights


# In[43]:


fig = px.density_heatmap(flights,x='year', y='month',
                        z='passengers',
                        color_continuous_scale='Viridis',
                        marginal_x='histogram',
                        )
fig


# # 3D Scatter Plots

# In[46]:


fig = px.scatter_3d(flights,x='year',y='month',z='passengers',
                   color='year',opacity=0.7)
fig


# In[48]:


fig = px.line_3d(flights,x='year',y='month',z='passengers',
                   color='year')
fig


# # Scatter Matrix

# In[50]:


fig = px.scatter_matrix(flights,color='month')
fig


# # Map scatter Plots

# In[52]:


df = px.data.gapminder().query("year==2007")
fig = px.scatter_geo(df,locations='iso_alpha',
                    color='continent',
                    hover_name='country',
                    size='pop',
                    projection = 'orthographic')
fig


# # Polar charts

# In[53]:


#these charts display data radially
df_wind = px.data.wind()
df_wind


# In[54]:


px.scatter_polar(df_wind, r="frequency", theta='direction',color='strength',size='frequency',
                symbol='strength')


# In[55]:


px.line_polar(df_wind, r="frequency", theta='direction',color='strength',line_close=True,template='plotly_dark')


# # Ternary Plot

# In[56]:


df_exp = px.data.experiment()
df_exp


# In[57]:


px.scatter_ternary(df_exp,a='experiment_1',
                  b='experiment_2',
                  c='experiment_3',
                  hover_name='group',color='gender')


# # Facet Plot

# In[62]:


df_tips = px.data.tips()
px.scatter(df_tips,x='total_bill',y='tip',color='smoker',facet_col='sex')
px.histogram(df_tips,x='total_bill',y='tip',color='sex',facet_row='time',
            facet_col='day',
            category_orders={"day":['Thu','Fri','Sat','Sun'],
                            "time":['Lunch','dinner',]})
att_df = sns.load_dataset("attention")
fig =px.line(att_df,x="solutions",y='score',facet_col='subject',
            facet_col_wrap=5,title="Scores based on attention")
fig


# # Animated plots

# In[63]:


#create a scatter plot and it will cycle through gdp and life expectancy changes by year
df_cnt = px.data.gapminder()
df_cnt


# In[66]:


px.scatter(df_cnt,x='gdpPercap',y='lifeExp',
          animation_frame='year',
          animation_group='country',
          size='pop',
          color='continent',
          hover_name='country', log_x= True,size_max=55,range_x=[100,100000],
          range_y=[25,90])


# In[68]:


px.bar(df_cnt,x='continent',y='pop',color='continent',
      animation_frame='year',
      animation_group='country',
       range_y=[0,40000000])


# In[ ]:





# In[ ]:




