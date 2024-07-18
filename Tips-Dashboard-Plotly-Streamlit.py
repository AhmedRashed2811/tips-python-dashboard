# ---------------------------------------------------------IMPORTING LIBRARIES
import pandas as pd
import numpy as np
import plotly.express as px
import streamlit as st



# ---------------------------------------------------------LOADING DATA
df = pd.read_csv('tips.csv')

# ---------------------------------------------------------DASHBOARD

# ------------------------------PAGE CONFIGURATION
st.set_page_config(page_title="Tips Dashboard",
                    layout="wide",
                    initial_sidebar_state="expanded",
                    )

# ------------------------------SIDE BAR
st.sidebar.markdown(
    "<h1 style='text-align: center;'>Tips Dashboard</h1>",
    unsafe_allow_html=True
)

st.sidebar.image("tip.png", use_column_width=True)

st.sidebar.markdown(
    "<h2 style='text-align: center;'>This Tips Dashboard is Made With Python.</h1>",
    unsafe_allow_html=True
)

st.sidebar.write("")

st.sidebar.markdown(
    "<h3 style='text-align: center;'>Filter Your Data:</h1>",
    unsafe_allow_html=True
)

# ----------------------FILTERS
categorical_filter = st.sidebar.selectbox("   Filter By:", [None, "sex","smoker","day", "time"])
numerical_filter = st.sidebar.selectbox("   Size By:", [None, "total_bill","tip"])
row_filter = st.sidebar.selectbox("   Row Filter:", [None, "sex","smoker","day", "time"])
column_filter = st.sidebar.selectbox("   Column Filter By:", [None, "sex","smoker","day", "time"])


st.sidebar.markdown("Made with :heart_eyes: by Eng. [Ahmed Rashed](https://www.novypro.com/profile_about/ahmed-rashed)")


# ------------------------------BODY

# ----------------------ROW A (Metrics)
a1, a2, a3, a4 = st.columns(4)

a1.metric("Max. Bill", df["total_bill"].max())
a2.metric("Avg. Bill", round(df["total_bill"].mean(), 2))
a3.metric("Max. Tip", df["tip"].max())
a4.metric("Avg. Tip", round(df["tip"].mean(), 2))


# ----------------------ROW B (ScatterPlot)

fig = px.scatter(
    df,
    x = "total_bill",
    y = "tip",
    color=categorical_filter,
    size=numerical_filter,
    facet_row= row_filter,
    facet_col=column_filter
    )

fig.update_layout(
    title = "Bills vs Tips",
    width=900,  
    height=400,  
    legend=dict(
        orientation='h',
        x=0.3,  
        y=1.2,  
        traceorder='normal',  
    )
)

st.plotly_chart(fig, use_container_width=True)


# ----------------------ROW C (Categorical Charts)
c1, c2, c3 = st.columns((4,3,3))

# --------------CHART 1 (Bar Chart)
with c1:
    sum_total_bill = df.groupby('sex')['total_bill'].sum().reset_index()

    fig = px.bar(
        data_frame= df, 
        x= 'sex',
        y='total_bill',
        color = categorical_filter,
        labels={'sex': 'Sex', 'total_bill': 'Total Bill'}
    )
    
    fig.update_layout(
        title ="Sex vs Total Bills",
        xaxis_title="Sex",
        yaxis_title="Total Bill",
        barmode='group',  
    )
    

    for i, row in sum_total_bill.iterrows():
        fig.add_annotation(
            x=row['sex'],
            y=row['total_bill'],
            text=f"{row['total_bill']}",
            showarrow=True,
        )
        
    st.plotly_chart(fig, use_container_width=True)

# --------------CHART 2 (Pie Chart)
with c2:
    fig = px.pie(
        data_frame= df, 
        names= 'smoker',
        values='tip'
    )
    
    fig.update_layout(
        title ="Smoker/Non-Smoker vs Tips",
    )
    
    st.plotly_chart(fig, use_container_width=True)

# --------------CHART 3 (Donut Chart)
with c3:
    fig = px.pie(
        data_frame= df, 
        names= 'day',
        values='tip',
        hole=0.4
    )
    
    fig.update_layout(
        title ="Days vs Tips",
    )
    
    st.plotly_chart(fig, use_container_width=True)