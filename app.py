import dash
from dash import dcc, html, Input, Output, dash_table
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np

# ------------------------------------------------------------------------------
# 1. Mock Data Generation
# ------------------------------------------------------------------------------
np.random.seed(42)

# --- Supply Side Data ---
programs = ['B.S. Data Science', 'M.S. AI', 'B.S. Statistics', 'M.S. Data Science']
years = [2019, 2020, 2021, 2022, 2023]

# 1.1 & 1.4 Graduates and Tuition
supply_data = []
for p in programs:
    base_tuition = np.random.randint(15000, 45000)
    for y in years:
        supply_data.append({
            'Program': p,
            'Year': y,
            'Graduates': np.random.randint(50, 300) + (y - 2019)*20,
            'Tuition_USD': base_tuition + (y - 2019)*1000
        })
df_supply = pd.DataFrame(supply_data)

# 1.2 Core Curriculum
skills = ['Python', 'SQL', 'R', 'Machine Learning', 'Cloud Platforms', 'Deep Learning', 'Tableau', 'Spark', 'Mathematics', 'Data Visualization']
curriculum_data = []
for p in programs:
    taught = np.random.choice(skills, 5, replace=False)
    for s in taught:
        curriculum_data.append({
            'Program': p,
            'Skill': s,
            'Credit_Hours': np.random.randint(3, 12)
        })
df_curriculum = pd.DataFrame(curriculum_data)

# 1.3 Employment Tracking
emp_tracking_data = []
for p in programs:
    emp_tracking_data.append({'Program': p, 'Year_Post_Grad': 'Year 1', 'Employed_Pct': np.random.uniform(60, 80)})
    emp_tracking_data.append({'Program': p, 'Year_Post_Grad': 'Year 2', 'Employed_Pct': np.random.uniform(75, 90)})
    emp_tracking_data.append({'Program': p, 'Year_Post_Grad': 'Year 3', 'Employed_Pct': np.random.uniform(85, 98)})
df_employment = pd.DataFrame(emp_tracking_data)

# --- Demand Side Data ---
experience_levels = ['Entry-Level', 'Mid-Level', 'Expert-Level']
job_titles = ['Data Scientist', 'AI Engineer', 'Data Analyst', 'Statistician']

# 2.1 & 2.4 Open Positions & Salaries
demand_data = []
for title in job_titles:
    for level in experience_levels:
        for y in years:
            demand_data.append({
                'Job_Title': title,
                'Experience_Level': level,
                'Year': y,
                'Open_Positions': np.random.randint(500, 5000) + (y - 2019)*500,
                'Avg_Salary_USD': np.random.randint(60000, 100000) if level == 'Entry-Level' else (np.random.randint(100000, 150000) if level == 'Mid-Level' else np.random.randint(150000, 250000))
            })
df_demand = pd.DataFrame(demand_data)

# 2.2 Required Skills
demand_skills_data = []
for title in job_titles:
    required = np.random.choice(skills, 7, replace=False)
    for s in required:
        demand_skills_data.append({
            'Job_Title': title,
            'Skill': s,
            'Demand_Score': np.random.randint(50, 100)
        })
df_demand_skills = pd.DataFrame(demand_skills_data)

# 2.3 Hiring Companies
companies = ['TechNova', 'DataCore', 'AI Solutions', 'Statistics Global', 'CloudNet', 'HealthAI']
hiring_data = []
for c in companies:
    hiring_data.append({
        'Company': c,
        'Industry': np.random.choice(['Tech', 'Finance', 'Healthcare', 'Retail']),
        'Open_Roles': np.random.randint(10, 100)
    })
df_companies = pd.DataFrame(hiring_data)


# ------------------------------------------------------------------------------
# 2. App Initialization
# ------------------------------------------------------------------------------
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP], suppress_callback_exceptions=True)

# ------------------------------------------------------------------------------
# 3. Layout
# ------------------------------------------------------------------------------
app.layout = dbc.Container([
    dbc.Row([
        dbc.Col(html.H1("AI & Data Science Job Market Dashboard", className="text-center my-4 text-primary"), width=12)
    ]),
    
    dcc.Tabs(id="tabs", value='tab-1', children=[
        dcc.Tab(label='Supply Side (Graduates)', value='tab-1'),
        dcc.Tab(label='Demand Side (Job Market)', value='tab-2'),
        dcc.Tab(label='Gap Analysis (Skill Mismatch)', value='tab-3'),
    ]),
    
    html.Div(id='tabs-content', className="mt-4 p-4 border rounded bg-light")
], fluid=True)

# ------------------------------------------------------------------------------
# 4. Callbacks
# ------------------------------------------------------------------------------
@app.callback(Output('tabs-content', 'children'),
              Input('tabs', 'value'))
def render_content(tab):
    if tab == 'tab-1':
        # --- TAB 1: Supply Side ---
        
        # 1.1 Graduates Trend
        fig_graduates = px.line(df_supply, x='Year', y='Graduates', color='Program', markers=True, title='Graduates Trend by Program')
        
        # 1.4 Tuition Fees (Taking the latest year for simplicity)
        df_tuition = df_supply[df_supply['Year'] == 2023]
        fig_tuition = px.bar(df_tuition, x='Program', y='Tuition_USD', color='Program', title='Tuition Fees (2023)')
        
        # 1.3 Employment Tracking
        fig_employment = px.bar(df_employment, x='Program', y='Employed_Pct', color='Year_Post_Grad', barmode='group', title='Employment Rate Post-Graduation (%)')
        
        return html.Div([
            dbc.Row([
                dbc.Col([
                    html.Label("Filter by Program:"),
                    dcc.Dropdown(
                        id='supply-program-filter',
                        options=[{'label': i, 'value': i} for i in programs],
                        value=programs,
                        multi=True
                    )
                ], width=12, className="mb-4")
            ]),
            dbc.Row([
                dbc.Col(dcc.Graph(id='fig-graduates', figure=fig_graduates), width=6),
                dbc.Col(dcc.Graph(id='fig-tuition', figure=fig_tuition), width=6)
            ]),
            dbc.Row([
                dbc.Col(dcc.Graph(id='fig-employment', figure=fig_employment), width=6),
                dbc.Col([
                    html.H5("Core Curriculum (Skills Taught)", className="mt-4 text-center"),
                    dash_table.DataTable(
                        id='curriculum-table',
                        columns=[{"name": i, "id": i} for i in df_curriculum.columns],
                        data=df_curriculum.to_dict('records'),
                        page_size=10,
                        style_table={'overflowX': 'auto'},
                        style_cell={'textAlign': 'left'}
                    )
                ], width=6)
            ])
        ])
        
    elif tab == 'tab-2':
        # --- TAB 2: Demand Side ---
        
        # 2.1 Open Positions Trend
        fig_open_pos = px.line(df_demand.groupby(['Year', 'Job_Title'])['Open_Positions'].sum().reset_index(), 
                               x='Year', y='Open_Positions', color='Job_Title', markers=True, title='Open Positions Over Time')
        
        # 2.2 Required Skills
        fig_skills = px.bar(df_demand_skills.groupby('Skill')['Demand_Score'].sum().reset_index().sort_values('Demand_Score', ascending=True), 
                            x='Demand_Score', y='Skill', orientation='h', title='Top Required Skills')
        
        # 2.4 Salary by Experience
        fig_salary = px.box(df_demand, x='Experience_Level', y='Avg_Salary_USD', color='Experience_Level', title='Salary Distribution by Experience')

        return html.Div([
            dbc.Row([
                dbc.Col([
                    html.Label("Filter by Job Title:"),
                    dcc.Dropdown(
                        id='demand-job-filter',
                        options=[{'label': i, 'value': i} for i in job_titles],
                        value=job_titles,
                        multi=True
                    )
                ], width=12, className="mb-4")
            ]),
            dbc.Row([
                dbc.Col(dcc.Graph(id='fig-open-pos', figure=fig_open_pos), width=6),
                dbc.Col(dcc.Graph(id='fig-salary', figure=fig_salary), width=6)
            ]),
            dbc.Row([
                dbc.Col(dcc.Graph(id='fig-req-skills', figure=fig_skills), width=6),
                dbc.Col([
                    html.H5("Top Hiring Companies", className="mt-4 text-center"),
                    dash_table.DataTable(
                        id='companies-table',
                        columns=[{"name": i, "id": i} for i in df_companies.columns],
                        data=df_companies.to_dict('records'),
                        page_size=10,
                        style_table={'overflowX': 'auto'},
                        style_cell={'textAlign': 'left'}
                    )
                ], width=6)
            ])
        ])
        
    elif tab == 'tab-3':
        # --- TAB 3: Gap Analysis ---
        
        # Calculate Skill Mismatch
        # Aggregate supply skills (taught)
        supply_agg = df_curriculum.groupby('Skill')['Credit_Hours'].sum().reset_index()
        # Normalize to 0-100 scale for comparison
        supply_agg['Supply_Score'] = (supply_agg['Credit_Hours'] / supply_agg['Credit_Hours'].max()) * 100
        
        # Aggregate demand skills (required)
        demand_agg = df_demand_skills.groupby('Skill')['Demand_Score'].sum().reset_index()
        demand_agg['Demand_Score_Norm'] = (demand_agg['Demand_Score'] / demand_agg['Demand_Score'].max()) * 100
        
        # Merge
        mismatch_df = pd.merge(supply_agg[['Skill', 'Supply_Score']], demand_agg[['Skill', 'Demand_Score_Norm']], on='Skill', how='outer').fillna(0)
        mismatch_df['Gap'] = mismatch_df['Supply_Score'] - mismatch_df['Demand_Score_Norm']
        
        fig_mismatch = px.bar(mismatch_df.sort_values('Gap'), x='Gap', y='Skill', orientation='h', 
                              color='Gap', color_continuous_scale='RdYlGn',
                              title='Skill Mismatch (Supply Score - Demand Score)')
                              
        fig_radar = go.Figure()
        fig_radar.add_trace(go.Scatterpolar(
            r=mismatch_df['Supply_Score'],
            theta=mismatch_df['Skill'],
            fill='toself',
            name='Supply (Taught)'
        ))
        fig_radar.add_trace(go.Scatterpolar(
            r=mismatch_df['Demand_Score_Norm'],
            theta=mismatch_df['Skill'],
            fill='toself',
            name='Demand (Required)'
        ))
        fig_radar.update_layout(polar=dict(radialaxis=dict(visible=True, range=[0, 100])), showlegend=True, title='Skill Gap Radar')

        return html.Div([
            dbc.Row([
                dbc.Col(html.P("This tab compares the skills taught in degree programs vs. the skills demanded by employers. A negative gap indicates a shortage (high demand, low supply), while a positive gap indicates an oversupply.", className="lead"), width=12)
            ]),
            dbc.Row([
                dbc.Col(dcc.Graph(id='fig-mismatch', figure=fig_mismatch), width=6),
                dbc.Col(dcc.Graph(id='fig-radar', figure=fig_radar), width=6)
            ])
        ])

# ------------------------------------------------------------------------------
# Tab 1 Cross-Filtering Callbacks
# ------------------------------------------------------------------------------
@app.callback(
    [Output('fig-graduates', 'figure'),
     Output('fig-tuition', 'figure'),
     Output('fig-employment', 'figure'),
     Output('curriculum-table', 'data')],
    [Input('supply-program-filter', 'value')]
)
def update_tab1(selected_programs):
    if not selected_programs:
        selected_programs = programs
        
    filtered_supply = df_supply[df_supply['Program'].isin(selected_programs)]
    filtered_emp = df_employment[df_employment['Program'].isin(selected_programs)]
    filtered_curr = df_curriculum[df_curriculum['Program'].isin(selected_programs)]
    
    fig_grad = px.line(filtered_supply, x='Year', y='Graduates', color='Program', markers=True, title='Graduates Trend by Program')
    
    df_tuit = filtered_supply[filtered_supply['Year'] == 2023]
    fig_tuit = px.bar(df_tuit, x='Program', y='Tuition_USD', color='Program', title='Tuition Fees (2023)')
    
    fig_emp = px.bar(filtered_emp, x='Program', y='Employed_Pct', color='Year_Post_Grad', barmode='group', title='Employment Rate Post-Graduation (%)')
    
    return fig_grad, fig_tuit, fig_emp, filtered_curr.to_dict('records')

# ------------------------------------------------------------------------------
# Tab 2 Cross-Filtering Callbacks
# ------------------------------------------------------------------------------
@app.callback(
    [Output('fig-open-pos', 'figure'),
     Output('fig-salary', 'figure'),
     Output('fig-req-skills', 'figure')],
    [Input('demand-job-filter', 'value')]
)
def update_tab2(selected_jobs):
    if not selected_jobs:
        selected_jobs = job_titles
        
    filtered_demand = df_demand[df_demand['Job_Title'].isin(selected_jobs)]
    filtered_skills = df_demand_skills[df_demand_skills['Job_Title'].isin(selected_jobs)]
    
    fig_open = px.line(filtered_demand.groupby(['Year', 'Job_Title'])['Open_Positions'].sum().reset_index(), 
                       x='Year', y='Open_Positions', color='Job_Title', markers=True, title='Open Positions Over Time')
    
    fig_sal = px.box(filtered_demand, x='Experience_Level', y='Avg_Salary_USD', color='Experience_Level', title='Salary Distribution by Experience')
    
    fig_req = px.bar(filtered_skills.groupby('Skill')['Demand_Score'].sum().reset_index().sort_values('Demand_Score', ascending=True), 
                     x='Demand_Score', y='Skill', orientation='h', title='Top Required Skills')
    
    return fig_open, fig_sal, fig_req

if __name__ == '__main__':
    app.run_server(debug=True)
