# Streamit dashboard

import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# Loading data
@st.cache_data
def load_data():
    df = pd.read_csv('outputs/rfm_final.csv')
    return df
 
df = load_data()

# Titre
st.title("RFM Customer Segmentation Dashboard")
st.markdown("🎉 **Welcome to the RFM Dashboard for Retail Banking!**")

# Sidebar - filters
segment = st.sidebar.multiselect("Select Segments(s):", options=df['Cluster_label'].unique(), default = df['Cluster_label'].unique())

filtered_df = df[df['Cluster_label'].isin(segment)]

# Ajout
# Avant (version de base)
st.dataframe(filtered_df)

# Après (version responsive)
st.dataframe(filtered_df, use_container_width=True)
#st.data_editor(filtered_df, use_container_width=True, height=400)
# fin ajout

#KPIs
st.metric("📦 Total Customers", len(filtered_df))
st.metric("💰 Total Monetary Value", int(filtered_df['Monetary'].sum()))

# Distribution per segment
st.subheader("Customer Distribution per Segment")
seg_counts = filtered_df['Cluster_label'].value_counts()
st.bar_chart(seg_counts)

#RFM mean graphic per segment
st.subheader("📊 Mean RFM per Segment")
avg_rfm = filtered_df.groupby('Cluster_label')[['Recency', 'Frequency', 'Monetary']].mean()
st.dataframe(avg_rfm.round(2))

# Raw Data
st.subheader("📄 Customer Data")
st.dataframe(filtered_df)