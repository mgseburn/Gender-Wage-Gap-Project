import pandas as pd
import streamlit as st
import plotly.express as px
st.set_page_config(layout="wide")
df=pd.read_excel("Women_Earnings_as_a_percentage.xlsx")

df_melted = df.melt(id_vars="Year", var_name="Age Range", value_name="Percentage")
colors = px.colors.qualitative.Set1[:len(df_melted['Age Range'].unique())]
col1, col2, col3 = st.columns([5, 5, 5])

with col1:
    fig1 = px.line(df_melted, x='Year', y='Percentage', color='Age Range',
              color_discrete_map=dict(zip(df_melted['Age Range'].unique(), colors)),
              title='Yearly Percentage for Different Age Ranges')
    fig1.update_xaxes(title_text='Year')
    fig1.update_yaxes(title_text='Percentage')
    fig1.add_hline(y=100, line_dash="dash")
    st.plotly_chart(fig1, use_container_width=True)


df2 = pd.read_excel('Map.xlsx')
us_state_to_abbrev = {
    "Alabama": "AL",
    "Alaska": "AK",
    "Arizona": "AZ",
    "Arkansas": "AR",
    "California": "CA",
    "Colorado": "CO",
    "Connecticut": "CT",
    "Delaware": "DE",
    "Florida": "FL",
    "Georgia": "GA",
    "Hawaii": "HI",
    "Idaho": "ID",
    "Illinois": "IL",
    "Indiana": "IN",
    "Iowa": "IA",
    "Kansas": "KS",
    "Kentucky": "KY",
    "Louisiana": "LA",
    "Maine": "ME",
    "Maryland": "MD",
    "Massachusetts": "MA",
    "Michigan": "MI",
    "Minnesota": "MN",
    "Mississippi": "MS",
    "Missouri": "MO",
    "Montana": "MT",
    "Nebraska": "NE",
    "Nevada": "NV",
    "New Hampshire": "NH",
    "New Jersey": "NJ",
    "New Mexico": "NM",
    "New York": "NY",
    "North Carolina": "NC",
    "North Dakota": "ND",
    "Ohio": "OH",
    "Oklahoma": "OK",
    "Oregon": "OR",
    "Pennsylvania": "PA",
    "Rhode Island": "RI",
    "South Carolina": "SC",
    "South Dakota": "SD",
    "Tennessee": "TN",
    "Texas": "TX",
    "Utah": "UT",
    "Vermont": "VT",
    "Virginia": "VA",
    "Washington": "WA",
    "West Virginia": "WV",
    "Wisconsin": "WI",
    "Wyoming": "WY",
    "District of Columbia": "DC",
    "American Samoa": "AS",
    "Guam": "GU",
    "Northern Mariana Islands": "MP",
    "Puerto Rico": "PR",
    "United States Minor Outlying Islands": "UM",
    "U.S. Virgin Islands": "VI",
}
grouped_df2 = df2.groupby('States')[['F_Med_Week_Earnings', 'M_Med_Week_Earnings']].mean()
grouped_df2 = grouped_df2.reset_index().rename(columns={'F_Med_Week_Earnings': 'Female Median Weekly Earnings', 
                                                        'M_Med_Week_Earnings': 'Male Median Weekly Earnings'})
grouped_df2["StatesAbb"] = grouped_df2["States"].map(us_state_to_abbrev)
grouped_df2["Proportion"]=grouped_df2["Female Median Weekly Earnings"]/grouped_df2["Male Median Weekly Earnings"]
with col2:
    fig2 = px.choropleth(locations=grouped_df2["StatesAbb"],
                    locationmode="USA-states",
                    scope="usa",
                    color=grouped_df2["Proportion"],
                    color_continuous_scale="Viridis",
                    title="2022 Weekly Proportional Earnings by States")
    st.plotly_chart(fig2, use_container_width=True)

df=pd.read_excel("Education.xlsx")
new_column_names = {
    'F_Less_than_HS_diploma\n': 'Female Less than a HS diploma',
    'F_HS_grad_ no_college': 'Female Hs graduate no college',
    'F_Associate_degree': 'Female Associate degree',
    'F_Bach_degree_<': 'Female Bach degree or more',
    'M_Less_than_HS_diploma\n': 'Male Less than a HS diploma',
    'M_HS_grad_ no_college': 'Male Hs graduate no college',
    'M_Associate_degree': 'Male Associate degree',
    'M_Bach_degree_<': 'Male Bach degree or more'}
df.rename(columns=new_column_names, inplace=True)
df_melted = df.melt(id_vars="Year", var_name="Education level by Gender", value_name="Median Earns")
color_map = {
    'Female Less than a HS diploma': '#FFC0CB',
    'Male Less than a HS diploma': '#ADD8E6',
    'Female Hs graduate no college': '#FF69B4',
    'Male Hs graduate no college': '#87CEFA',
    'Female Associate degree': '#DB7093',
    'Male Associate degree': '#6495ED',
    'Female Bach degree or more': '#C71585',
    'Male Bach degree or more': '#0000FF'}
colors = df_melted['Education level by Gender'].map(color_map)
with col3:
    fig3 = px.line(df_melted, x='Year', y='Median Earns', color='Education level by Gender',
              color_discrete_map=color_map,  
              title='Yearly Median Earnings by Education Level')
    fig3.update_xaxes(title_text='Year')
    fig3.update_yaxes(title_text='Median Weekly Earnings')
    st.plotly_chart(fig3, use_container_width=True)