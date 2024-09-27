# import packages
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
# show the title
st.title('Titanic App by Zihan Zhou')
# read csv and show the dataframe
df = pd.read_csv('train.csv')
st.write(df)
# create a figure with three subplots, size should be (15, 5)
# show the box plot for ticket price with different classes
# you need to set the x labels and y labels
# a sample diagram is shown below
fig, axs = plt.subplots(1, 3, figsize=(15, 5))

axs[0].boxplot(df[df['Pclass'] == 1]['Fare'])
axs[0].set_title('Box Plot of Ticket Prices for 1st Class')
axs[0].set_ylabel('Ticket Price (Fare)')
axs[0].set_xticklabels(['1st Class'])

axs[1].boxplot(df[df['Pclass'] == 2]['Fare'])
axs[1].set_title('Box Plot of Ticket Prices for 2nd Class')
axs[1].set_ylabel('Ticket Price (Fare)')
axs[1].set_xticklabels(['2nd Class'])

axs[2].boxplot(df[df['Pclass'] == 3]['Fare'])
axs[2].set_title('Box Plot of Ticket Prices for 3rd Class')
axs[2].set_ylabel('Ticket Price (Fare)')
axs[2].set_xticklabels(['3rd Class'])

plt.tight_layout()
plt.show()
st.pyplot(fig)
