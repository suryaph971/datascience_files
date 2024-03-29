# -*- coding: utf-8 -*-
"""A/B Testing with python

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1zs-AQVsmCpAUJqoxjL0cs4n-uGRrjUCj
"""

import pandas as pd
import datetime
from datetime import date,timedelta
import plotly.graph_objects as go
import plotly.express as px
import plotly.io as pio
pio.templates.default="plotly_white"

control_group_dataset = pd.read_csv("/content/drive/MyDrive/archive/control_group.csv",sep=";")
test_group_dataset = pd.read_csv("/content/drive/MyDrive/archive/test_group.csv",sep=";")

control_group_dataset.head()

test_group_dataset.head()

control_group_dataset.columns = ['Campaign Name','Date','Amount Spent','No of Impressions','Reach','Website Clicks','Searchers Received','Content Viewed','Added to Cart','Purchases']
test_group_dataset.columns = ['Campaign Name','Date','Amount Spent','No of Impressions','Reach','Website Clicks','Searchers Received','Content Viewed','Added to Cart','Purchases']

print(control_group_dataset.isnull().sum())

print(test_group_dataset.isnull().sum())

control_group_dataset['No of Impressions'].fillna(value = control_group_dataset['No of Impressions'].mean(),inplace=True)
control_group_dataset['Reach'].fillna(value=control_group_dataset['Reach'].mean(),inplace=True)
control_group_dataset['Website Clicks'].fillna(value=control_group_dataset['Website Clicks'].mean(),inplace=True)
control_group_dataset['Searchers Received'].fillna(value=control_group_dataset['Searchers Received'].mean(),inplace=True)
control_group_dataset['Content Viewed'].fillna(value=control_group_dataset['Content Viewed'].mean(),inplace=True)
control_group_dataset['Added to Cart'].fillna(value=control_group_dataset['Added to Cart'].mean(),inplace=True)
control_group_dataset['Purchases'].fillna(value=control_group_dataset['Purchases'].mean(),inplace=True)

Group_dataset = control_group_dataset.merge(test_group_dataset,how='outer').sort_values(['Date'])
print(Group_dataset.head)

Group_dataset = Group_dataset.reset_index(drop=True)
print(Group_dataset.head())

Group_dataset['Campaign Name'].value_counts()

figure = px.scatter(data_frame = Group_dataset,
                    x="No of Impressions",
                    y="Amount Spent",
                    size = "Amount Spent",
                    color = "Campaign Name",
                    trendline = "ols")
figure.show()

"""No of impressions are higher for control campaings considering Amount spend"""

indicating_label = ['Search count for control campaign','Search count for test campaign']
counts = [sum(control_group_dataset['Searchers Received']),
          sum(test_group_dataset['Searchers Received'])]

colors = ['gold','lightgreen']
figure = go.Figure(data=[go.Pie(labels = indicating_label,values=counts)])

figure.update_layout(title_text = 'Control vs test : Searches')
figure.update_traces(hoverinfo='label+percent',textinfo='value',textfont_size=30,marker=dict(colors=colors,line=dict(color='black',width=3)))

figure.show()

"""Here Compared to controlled campaign , test campaign resulted more searches on the website"""

label = ['Website clicks for control campaign','Wesbite clicks for test campaign']
counts = [sum(control_group_dataset['Website Clicks']),
          sum(test_group_dataset['Website Clicks'])]

colors = ['red','blue']
figure = go.Figure(data = [go.Pie(labels=label,values=counts)])
figure.update_layout(title='Control vs test :  Website clicks')
figure.update_traces(hoverinfo='label+percent',textinfo='value',textfont_size=30,marker=dict(colors=colors,line=dict(color='black',width=3)))

figure.show()

"""Here test campaign resulted more website clicks as it has slightly higher rate of searches on the website compared to control campaigns"""

label = ['Content viewed for control campaign','Content viewed for test campaign']
counts = [sum(control_group_dataset['Content Viewed']),
          sum(test_group_dataset['Content Viewed'])]

colors = ['gold','lightgreen']
figure = go.Figure(data = [go.Pie(labels=label,values=counts)])
figure.update_layout(title='Control vs test :  Content viewed')
figure.update_traces(hoverinfo='label+percent',textinfo='value',textfont_size=30,marker=dict(colors=colors,line=dict(color='black',width=3)))

figure.show()

"""In this scenario most people viewed control campaign content on website though there is not much difference as website clicks for control campaign is low. People engagement to control campaign is more."""

label = ['Carts count  for control campaign','Carts count for test campaign']
counts = [sum(control_group_dataset['Added to Cart']),
          sum(test_group_dataset['Added to Cart'])]

colors = ['gold','lightgreen']
figure = go.Figure(data = [go.Pie(labels=label,values=counts)])
figure.update_layout(title='Control vs test :  Added to Cart')
figure.update_traces(hoverinfo='label+percent',textinfo='value',textfont_size=30,marker=dict(colors=colors,line=dict(color='black',width=3)))

figure.show()

"""Most people likely to add the products to the cart for the control campaign and it has a great acceptance rate for the content in control campaign"""

label = ['Purchases  for control campaign','Purchases for test campaign']
counts = [sum(control_group_dataset['Purchases']),
          sum(test_group_dataset['Purchases'])]

colors = ['gold','lightgreen']
figure = go.Figure(data = [go.Pie(labels=label,values=counts)])
figure.update_layout(title='Control vs test :  Purchases')
figure.update_traces(hoverinfo='label+percent',textinfo='value',textfont_size=30,marker=dict(colors=colors,line=dict(color='black',width=3)))

figure.show()

"""Even tough  test compaign has less content viewed and acceptance rate. Amount of purchases made on those campaign is good. But Control campaign has slight higher than test campaign"""

label = ['Amount Spent for control campaign','Amount Spent for test campaign']
counts = [sum(control_group_dataset['Amount Spent']),
          sum(test_group_dataset['Amount Spent'])]

colors = ['gold','lightgreen']
figure = go.Figure(data = [go.Pie(labels=label,values=counts)])
figure.update_layout(title='Control vs test :  Amount Spent')
figure.update_traces(hoverinfo='label+percent',textinfo='value',textfont_size=30,marker=dict(colors=colors,line=dict(color='black',width=3)))

figure.show()

"""Great thing about control campaign here is despite low website clicks, it showed great performance interms of convincing the audience.
Amount of spent on control campaign is less and it showed great sales in products.
"""

figure = px.scatter(data_frame=Group_dataset,
                    x='Content Viewed',
                    y='Website Clicks',
                   size='Website Clicks',
                    color = 'Campaign Name',
                    trendline='ols')
figure.show()

"""As we seen previous website clicks are more for test campaign. But engaging according to the content viewed is more for control campaigns."""

figure = px.scatter(data_frame=Group_dataset,
                    x='Added to Cart',
                    y='Content Viewed',
                   size='Added to Cart',
                    color = 'Campaign Name',
                    trendline='ols')
figure.show()

"""Observed more products added to cart for control campaign as the no. of people viewed the control campaign is more."""

figure = px.scatter(data_frame=Group_dataset,
                    x='Purchases',
                    y='Added to Cart',
                   size='Purchases',
                    color = 'Campaign Name',
                    trendline='ols')
figure.show()

"""Even though products added to cart are less for test campaign. The conversion rate is solid compared to control campaigns on the website."""





