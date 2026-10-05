import dash
from dash import dcc, html, Input, Output
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np

# ------------------------------------------------------------------------------
# 1. Mock Data Generation
# ------------------------------------------------------------------------------
np.random.seed(42)

# Supply Side Data
programs = ['B.S. Data Science', 'M.S. AI', 'B.S. Statistics', 'M.S. Data Science']
years = [2019, 2020, 2021, 2022, 2023]

supply_df = pd.DataFrame({
    'Program': np.random.choice(programs, 100),
    'Year': np.random.choice(years, 100),
    'Graduates': np.random.randint(50, 300, 100),
    'Tuition_USD': np.random.randint(10000, 50000, 100),
})

# Demand Side Data
experience_levels = ['Entry-Level', 'Mid-Level', 'Expert-Level']
skills = ['Python', 'SQL', 'R', 'Machine Learning', 'Cloud Platforms', 'Deep Learning', 'Tableau', 'Spark']

demand_df = pd.DataFrame({
    'Experience_Level': np.random.choice(experience_levels, 200),
    'Job_Title': np.random.choice(['Data Scientist', 'AI Engineer', 'Data Analyst', 'Statistician'], 200),
    'Open_Positions': np.random.randint(10, 100, 200),
    'Avg_Salary_USD': np.random.randint(60000, 200000, 200)
})

# Skills Data
skills_taught = pd.DataFrame({
    'Program': np.random.choice(programs, 100),
    'Skill': np.random.choice(skills, 100),
    'Proficiency_Score': np.random.randint(1, 10, 100)
})

skills_demanded = pd.DataFrame({
    'Job_Title': np.random.choice(['Data Scientist', 'AI Engineer', 'Data Analyst', 'Statistician'], 100),
    'Skill': np.random.choice(skills, 100),
    'Importance_Score': np.random.randint(1, 10, 100)
})


# ------------------------------------------------------------------------------
# 2. App Initialization
# ------------------------------------------------------------------------------
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# ------------------------------------------------------------------------------
# 3. Layout
# ------------------------------------------------------------------------------
app.layout = dbc.Container([
    dbc.Row([
        dbc.Col(html.H1("AI & Data Science Job Market Dashboard", className="text-center my-4"), width=12)
    ]),
    
    dcc.Tabs(id="tabs", value='tab-1', children=[
        dcc.Tab(label='Tab 1: Supply Side', value='tab-1'),
        dcc.Tab(label='Tab 2: Demand Side', value='tab-2'),
        dcc.Tab(label='Tab 3: Gap Analysis', value='tab-3'),
    ]),
    
    html.Div(id='tabs-content', className="mt-4")
], fluid=True)

# ------------------------------------------------------------------------------
# 4. Callbacks
# ------------------------------------------------------------------------------
@app.callback(Output('tabs-content', 'children'),
              Input('tabs', 'value'))
def render_content(tab):
    if tab == 'tab-1':
        fig = px.bar(supply_df.groupby(['Year', 'Program'])['Graduates'].sum().reset_index(), 
                     x='Year', y='Graduates', color='Program', barmode='group',
                     title='Graduates Trend by Program')
        return html.Div([
            html.H3('Supply Side: Graduates and Learned Skills'),
            dcc.Graph(figure=fig)
        ])
    elif tab == 'tab-2':
        return html.Div([
            html.H3('Demand Side: Job Market and Required Skills'),
            # Placeholder for Tab 2 content
            html.P("Demand side charts will be rendered here.")
        ])
    elif tab == 'tab-3':
        return html.Div([
            html.H3('Gap Analysis: Skill Mismatch'),
            # Placeholder for Tab 3 content
            html.P("Skill mismatch analysis charts will be rendered here.")
        ])

if __name__ == '__main__':
    app.run_server(debug=True)
