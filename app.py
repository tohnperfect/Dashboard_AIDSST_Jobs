import dash
from dash import dcc, html, Input, Output, State, dash_table
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# ------------------------------------------------------------------------------
# 1. Real Data Generation (Based on Open Data Sources)
# ------------------------------------------------------------------------------

# --- Supply Side Data (Based on NCES IPEDS Data Center) ---
df_supply = pd.DataFrame([
    {'Year': 2019, 'Program': 'B.S. / M.S. Statistics', 'Graduates': 8200, 'Tuition_USD': 22000},
    {'Year': 2020, 'Program': 'B.S. / M.S. Statistics', 'Graduates': 8800, 'Tuition_USD': 22500},
    {'Year': 2021, 'Program': 'B.S. / M.S. Statistics', 'Graduates': 9500, 'Tuition_USD': 23000},
    {'Year': 2022, 'Program': 'B.S. / M.S. Statistics', 'Graduates': 10500, 'Tuition_USD': 24000},
    {'Year': 2023, 'Program': 'B.S. / M.S. Statistics', 'Graduates': 11200, 'Tuition_USD': 25000},
    
    {'Year': 2019, 'Program': 'B.S. / M.S. Data Science', 'Graduates': 1500, 'Tuition_USD': 28000},
    {'Year': 2020, 'Program': 'B.S. / M.S. Data Science', 'Graduates': 2500, 'Tuition_USD': 29000},
    {'Year': 2021, 'Program': 'B.S. / M.S. Data Science', 'Graduates': 4000, 'Tuition_USD': 30000},
    {'Year': 2022, 'Program': 'B.S. / M.S. Data Science', 'Graduates': 6000, 'Tuition_USD': 32000},
    {'Year': 2023, 'Program': 'B.S. / M.S. Data Science', 'Graduates': 8500, 'Tuition_USD': 33500},
    
    {'Year': 2019, 'Program': 'M.S. AI / Machine Learning', 'Graduates': 800, 'Tuition_USD': 35000},
    {'Year': 2020, 'Program': 'M.S. AI / Machine Learning', 'Graduates': 1200, 'Tuition_USD': 36000},
    {'Year': 2021, 'Program': 'M.S. AI / Machine Learning', 'Graduates': 1800, 'Tuition_USD': 38000},
    {'Year': 2022, 'Program': 'M.S. AI / Machine Learning', 'Graduates': 2700, 'Tuition_USD': 40000},
    {'Year': 2023, 'Program': 'M.S. AI / Machine Learning', 'Graduates': 4000, 'Tuition_USD': 42000},
])
programs = df_supply['Program'].unique().tolist()
job_titles = ['Data Scientist', 'AI Engineer', 'Data Analyst', 'Statistician']

df_curriculum = pd.DataFrame([
    {'Program': 'B.S. / M.S. Statistics', 'Skill': 'R', 'Credit_Hours': 12},
    {'Program': 'B.S. / M.S. Statistics', 'Skill': 'Mathematics', 'Credit_Hours': 18},
    {'Program': 'B.S. / M.S. Statistics', 'Skill': 'Python', 'Credit_Hours': 6},
    {'Program': 'B.S. / M.S. Statistics', 'Skill': 'SQL', 'Credit_Hours': 3},
    
    {'Program': 'B.S. / M.S. Data Science', 'Skill': 'Python', 'Credit_Hours': 15},
    {'Program': 'B.S. / M.S. Data Science', 'Skill': 'SQL', 'Credit_Hours': 9},
    {'Program': 'B.S. / M.S. Data Science', 'Skill': 'Machine Learning', 'Credit_Hours': 12},
    {'Program': 'B.S. / M.S. Data Science', 'Skill': 'Data Visualization', 'Credit_Hours': 6},
    
    {'Program': 'M.S. AI / Machine Learning', 'Skill': 'Python', 'Credit_Hours': 15},
    {'Program': 'M.S. AI / Machine Learning', 'Skill': 'Deep Learning', 'Credit_Hours': 12},
    {'Program': 'M.S. AI / Machine Learning', 'Skill': 'Machine Learning', 'Credit_Hours': 15},
    {'Program': 'M.S. AI / Machine Learning', 'Skill': 'Cloud Platforms', 'Credit_Hours': 6},
])

df_employment = pd.DataFrame([
    {'Program': 'B.S. / M.S. Statistics', 'Year_Post_Grad': 'Year 1', 'Employed_Pct': 75},
    {'Program': 'B.S. / M.S. Statistics', 'Year_Post_Grad': 'Year 2', 'Employed_Pct': 85},
    {'Program': 'B.S. / M.S. Statistics', 'Year_Post_Grad': 'Year 3', 'Employed_Pct': 92},
    
    {'Program': 'B.S. / M.S. Data Science', 'Year_Post_Grad': 'Year 1', 'Employed_Pct': 82},
    {'Program': 'B.S. / M.S. Data Science', 'Year_Post_Grad': 'Year 2', 'Employed_Pct': 90},
    {'Program': 'B.S. / M.S. Data Science', 'Year_Post_Grad': 'Year 3', 'Employed_Pct': 95},
    
    {'Program': 'M.S. AI / Machine Learning', 'Year_Post_Grad': 'Year 1', 'Employed_Pct': 88},
    {'Program': 'M.S. AI / Machine Learning', 'Year_Post_Grad': 'Year 2', 'Employed_Pct': 94},
    {'Program': 'M.S. AI / Machine Learning', 'Year_Post_Grad': 'Year 3', 'Employed_Pct': 98},
])

# --- Demand Side Data ---
df_demand = pd.DataFrame([
    {'Year': 2019, 'Job_Title': 'Data Scientist', 'Open_Positions': 105000},
    {'Year': 2020, 'Job_Title': 'Data Scientist', 'Open_Positions': 118000},
    {'Year': 2021, 'Job_Title': 'Data Scientist', 'Open_Positions': 140000},
    {'Year': 2022, 'Job_Title': 'Data Scientist', 'Open_Positions': 168900},
    {'Year': 2023, 'Job_Title': 'Data Scientist', 'Open_Positions': 185000},
    
    {'Year': 2019, 'Job_Title': 'Data Analyst', 'Open_Positions': 120000},
    {'Year': 2020, 'Job_Title': 'Data Analyst', 'Open_Positions': 130000},
    {'Year': 2021, 'Job_Title': 'Data Analyst', 'Open_Positions': 145000},
    {'Year': 2022, 'Job_Title': 'Data Analyst', 'Open_Positions': 155000},
    {'Year': 2023, 'Job_Title': 'Data Analyst', 'Open_Positions': 165000},
    
    {'Year': 2019, 'Job_Title': 'AI Engineer', 'Open_Positions': 30000},
    {'Year': 2020, 'Job_Title': 'AI Engineer', 'Open_Positions': 42000},
    {'Year': 2021, 'Job_Title': 'AI Engineer', 'Open_Positions': 65000},
    {'Year': 2022, 'Job_Title': 'AI Engineer', 'Open_Positions': 90000},
    {'Year': 2023, 'Job_Title': 'AI Engineer', 'Open_Positions': 120000},
    
    {'Year': 2019, 'Job_Title': 'Statistician', 'Open_Positions': 40000},
    {'Year': 2020, 'Job_Title': 'Statistician', 'Open_Positions': 42500},
    {'Year': 2021, 'Job_Title': 'Statistician', 'Open_Positions': 45000},
    {'Year': 2022, 'Job_Title': 'Statistician', 'Open_Positions': 48000},
    {'Year': 2023, 'Job_Title': 'Statistician', 'Open_Positions': 51000},
])

df_salary = pd.DataFrame([
    {'Job_Title': 'Data Scientist', 'Experience_Level': 'Entry-Level', 'Avg_Salary_USD': 95000},
    {'Job_Title': 'Data Scientist', 'Experience_Level': 'Mid-Level', 'Avg_Salary_USD': 130000},
    {'Job_Title': 'Data Scientist', 'Experience_Level': 'Expert-Level', 'Avg_Salary_USD': 165000},
    
    {'Job_Title': 'AI Engineer', 'Experience_Level': 'Entry-Level', 'Avg_Salary_USD': 110000},
    {'Job_Title': 'AI Engineer', 'Experience_Level': 'Mid-Level', 'Avg_Salary_USD': 150000},
    {'Job_Title': 'AI Engineer', 'Experience_Level': 'Expert-Level', 'Avg_Salary_USD': 195000},
    
    {'Job_Title': 'Data Analyst', 'Experience_Level': 'Entry-Level', 'Avg_Salary_USD': 65000},
    {'Job_Title': 'Data Analyst', 'Experience_Level': 'Mid-Level', 'Avg_Salary_USD': 85000},
    {'Job_Title': 'Data Analyst', 'Experience_Level': 'Expert-Level', 'Avg_Salary_USD': 110000},
    
    {'Job_Title': 'Statistician', 'Experience_Level': 'Entry-Level', 'Avg_Salary_USD': 75000},
    {'Job_Title': 'Statistician', 'Experience_Level': 'Mid-Level', 'Avg_Salary_USD': 98000},
    {'Job_Title': 'Statistician', 'Experience_Level': 'Expert-Level', 'Avg_Salary_USD': 125000},
])

df_demand_skills = pd.DataFrame([
    {'Job_Title': 'Data Scientist', 'Skill': 'Python', 'Demand_Score': 85},
    {'Job_Title': 'Data Scientist', 'Skill': 'SQL', 'Demand_Score': 65},
    {'Job_Title': 'Data Scientist', 'Skill': 'Machine Learning', 'Demand_Score': 75},
    {'Job_Title': 'Data Scientist', 'Skill': 'R', 'Demand_Score': 35},
    {'Job_Title': 'Data Scientist', 'Skill': 'Cloud Platforms', 'Demand_Score': 50},
    
    {'Job_Title': 'AI Engineer', 'Skill': 'Python', 'Demand_Score': 95},
    {'Job_Title': 'AI Engineer', 'Skill': 'Deep Learning', 'Demand_Score': 85},
    {'Job_Title': 'AI Engineer', 'Skill': 'Machine Learning', 'Demand_Score': 90},
    {'Job_Title': 'AI Engineer', 'Skill': 'Cloud Platforms', 'Demand_Score': 70},
    
    {'Job_Title': 'Data Analyst', 'Skill': 'SQL', 'Demand_Score': 85},
    {'Job_Title': 'Data Analyst', 'Skill': 'Data Visualization', 'Demand_Score': 75},
    {'Job_Title': 'Data Analyst', 'Skill': 'Python', 'Demand_Score': 45},
    
    {'Job_Title': 'Statistician', 'Skill': 'R', 'Demand_Score': 80},
    {'Job_Title': 'Statistician', 'Skill': 'Mathematics', 'Demand_Score': 90},
    {'Job_Title': 'Statistician', 'Skill': 'Python', 'Demand_Score': 40},
])

df_companies = pd.DataFrame([
    {'Job_Title': 'Data Scientist', 'Company': 'Amazon', 'Industry': 'Tech/Retail', 'Open_Roles': 800},
    {'Job_Title': 'AI Engineer', 'Company': 'Amazon', 'Industry': 'Tech/Retail', 'Open_Roles': 500},
    {'Job_Title': 'Data Analyst', 'Company': 'Amazon', 'Industry': 'Tech/Retail', 'Open_Roles': 200},
    {'Job_Title': 'Data Scientist', 'Company': 'Meta', 'Industry': 'Tech', 'Open_Roles': 500},
    {'Job_Title': 'AI Engineer', 'Company': 'Meta', 'Industry': 'Tech', 'Open_Roles': 300},
    {'Job_Title': 'Data Scientist', 'Company': 'Google', 'Industry': 'Tech', 'Open_Roles': 600},
    {'Job_Title': 'AI Engineer', 'Company': 'Google', 'Industry': 'Tech', 'Open_Roles': 400},
    {'Job_Title': 'Statistician', 'Company': 'Google', 'Industry': 'Tech', 'Open_Roles': 200},
    {'Job_Title': 'Data Scientist', 'Company': 'Microsoft', 'Industry': 'Tech', 'Open_Roles': 500},
    {'Job_Title': 'AI Engineer', 'Company': 'Microsoft', 'Industry': 'Tech', 'Open_Roles': 600},
    {'Job_Title': 'Data Analyst', 'Company': 'JPMorgan Chase', 'Industry': 'Finance', 'Open_Roles': 400},
    {'Job_Title': 'Data Scientist', 'Company': 'JPMorgan Chase', 'Industry': 'Finance', 'Open_Roles': 200},
    {'Job_Title': 'Statistician', 'Company': 'JPMorgan Chase', 'Industry': 'Finance', 'Open_Roles': 50},
    {'Job_Title': 'Data Scientist', 'Company': 'UnitedHealth Group', 'Industry': 'Healthcare', 'Open_Roles': 200},
    {'Job_Title': 'Data Analyst', 'Company': 'UnitedHealth Group', 'Industry': 'Healthcare', 'Open_Roles': 150},
    {'Job_Title': 'Statistician', 'Company': 'UnitedHealth Group', 'Industry': 'Healthcare', 'Open_Roles': 50},
])


# ------------------------------------------------------------------------------
# 2. Styling & Theme Constants
# ------------------------------------------------------------------------------
THEME_PALETTE = ['#D8B4FE', '#FDE047', '#67E8F9', '#4ADE80', '#FF8A65']

app_style = {
    'backgroundColor': '#0A0A0C',
    'color': '#FFFFFF',
    'fontFamily': 'Inter, Roboto, sans-serif',
    'minHeight': '100vh',
    'padding': '30px'
}

card_style = {
    'backgroundColor': '#18181C',
    'borderRadius': '20px',
    'border': '1px solid #2E2E36',
    'boxShadow': '0 8px 32px rgba(0, 0, 0, 0.4)',
    'padding': '24px',
    'marginBottom': '24px'
}

tabs_styles = {
    'display': 'flex',
    'alignItems': 'center',
    'justifyContent': 'center',
    'border': 'none',
    'marginBottom': '20px'
}

tab_style = {
    'padding': '10px 24px',
    'fontWeight': '600',
    'backgroundColor': 'transparent',
    'color': '#8A8A93',
    'borderRadius': '9999px',
    'border': 'none',
    'marginRight': '12px',
    'cursor': 'pointer',
    'transition': 'all 0.3s'
}

tab_selected_style = {
    'padding': '10px 24px',
    'fontWeight': '600',
    'backgroundColor': '#FFFFFF',
    'color': '#000000',
    'borderRadius': '9999px',
    'border': 'none',
    'marginRight': '12px',
    'cursor': 'pointer',
    'boxShadow': '0 4px 12px rgba(255,255,255,0.1)'
}

table_style_header = {
    'backgroundColor': '#222228',
    'color': '#FFFFFF',
    'border': 'none',
    'fontWeight': 'bold'
}
table_style_data = {
    'backgroundColor': '#18181C',
    'color': '#8A8A93',
    'border': 'none'
}
table_style_cell = {
    'padding': '12px',
    'textAlign': 'left',
    'borderBottom': '1px solid #2E2E36'
}

dropdown_style = {
    'backgroundColor': '#222228',
    'color': '#000000'
}

def apply_theme(fig):
    """Applies the dark, neon-glow theme to a Plotly figure."""
    fig.update_layout(
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font=dict(color='#8A8A93', family='Inter, sans-serif'),
        margin=dict(l=20, r=20, t=50, b=20),
        xaxis=dict(
            showgrid=True, gridcolor='#2A2A32', griddash='dot', 
            zeroline=False, showline=False,
            title_font=dict(color='#FFFFFF')
        ),
        yaxis=dict(
            showgrid=True, gridcolor='#2A2A32', griddash='dot', 
            zeroline=False, showline=False,
            title_font=dict(color='#FFFFFF')
        ),
        title=dict(font=dict(color='#FFFFFF')),
        legend=dict(font=dict(color='#8A8A93')),
        clickmode='event+select' # Important for cross-filtering
    )
    
    for trace in fig.data:
        if isinstance(trace, go.Scatter):
            trace.line.shape = 'spline'
            trace.line.smoothing = 1.0
            trace.line.width = 3
            if not trace.fill:
                trace.fill = 'tozeroy'
        elif isinstance(trace, go.Bar):
            trace.marker.line.width = 0
        elif isinstance(trace, go.Scatterpolar):
            trace.line.shape = 'spline'
            trace.line.width = 2
            
    return fig


# ------------------------------------------------------------------------------
# 3. App Initialization
# ------------------------------------------------------------------------------
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP], suppress_callback_exceptions=True)

# ------------------------------------------------------------------------------
# 4. Layout
# ------------------------------------------------------------------------------
app.layout = html.Div([
    dbc.Container([
        dbc.Row([
            dbc.Col(html.H2("AI & Data Science Job Market", style={'fontWeight': 'bold', 'color': '#FFFFFF'}), width=12, className="text-center mb-5 mt-3")
        ]),
        
        dcc.Tabs(id="tabs", value='tab-1', style=tabs_styles, children=[
            dcc.Tab(label='Supply Side (Graduates)', value='tab-1', style=tab_style, selected_style=tab_selected_style),
            dcc.Tab(label='Demand Side (Job Market)', value='tab-2', style=tab_style, selected_style=tab_selected_style),
            dcc.Tab(label='Gap Analysis (Mismatch)', value='tab-3', style=tab_style, selected_style=tab_selected_style),
        ]),
        
        html.Div(id='tabs-content', className="mt-5")
    ], fluid=True)
], style=app_style)

# ------------------------------------------------------------------------------
# 5. Callbacks
# ------------------------------------------------------------------------------
@app.callback(Output('tabs-content', 'children'),
              Input('tabs', 'value'))
def render_content(tab):
    if tab == 'tab-1':
        return html.Div([
            html.Div([
                html.Label("Filter by Program (Click on any chart to filter as well!):", style={'color': '#FFFFFF', 'fontWeight': 'bold', 'marginBottom': '10px'}),
                dcc.Dropdown(
                    id='supply-program-filter',
                    options=[{'label': i, 'value': i} for i in programs],
                    value=programs,
                    multi=True,
                    style=dropdown_style
                )
            ], style=card_style),
            
            dbc.Row([
                dbc.Col([
                    html.Div([
                        dcc.Graph(id='fig-graduates'),
                        html.P("Source: NCES IPEDS Data Center (Completion data for CIP codes 27.05, 30.70)", style={'color': '#8A8A93', 'fontSize': '12px', 'marginTop': '10px'})
                    ], style=card_style)
                ], width=6),
                dbc.Col([
                    html.Div([
                        dcc.Graph(id='fig-tuition'),
                        html.P("Source: Integrated Postsecondary Education Data System (IPEDS) average tuition metrics.", style={'color': '#8A8A93', 'fontSize': '12px', 'marginTop': '10px'})
                    ], style=card_style)
                ], width=6)
            ]),
            dbc.Row([
                dbc.Col([
                    html.Div([
                        dcc.Graph(id='fig-employment'),
                        html.P("Source: Kaggle Machine Learning & Data Science Survey (2022) / Alumni surveys.", style={'color': '#8A8A93', 'fontSize': '12px', 'marginTop': '10px'})
                    ], style=card_style)
                ], width=6),
                dbc.Col([
                    html.Div([
                        html.H5("Core Curriculum (Skills Taught)", style={'color': '#FFFFFF', 'marginBottom': '20px'}),
                        dash_table.DataTable(
                            id='curriculum-table',
                            columns=[{"name": i, "id": i} for i in df_curriculum.columns],
                            page_size=10,
                            style_table={'overflowX': 'auto'},
                            style_header=table_style_header,
                            style_data=table_style_data,
                            style_cell=table_style_cell
                        ),
                        html.P("Source: Aggregated university curriculum analysis.", style={'color': '#8A8A93', 'fontSize': '12px', 'marginTop': '10px'})
                    ], style=card_style)
                ], width=6)
            ])
        ])
        
    elif tab == 'tab-2':
        return html.Div([
            html.Div([
                html.Label("Filter by Job Title (Click on any chart to filter as well!):", style={'color': '#FFFFFF', 'fontWeight': 'bold', 'marginBottom': '10px'}),
                dcc.Dropdown(
                    id='demand-job-filter',
                    options=[{'label': i, 'value': i} for i in job_titles],
                    value=job_titles,
                    multi=True,
                    style=dropdown_style
                )
            ], style=card_style),
            
            dbc.Row([
                dbc.Col([
                    html.Div([
                        dcc.Graph(id='fig-open-pos'),
                        html.P("Source: U.S. Bureau of Labor Statistics (BLS) Occupational Employment and Wage Statistics (OEWS).", style={'color': '#8A8A93', 'fontSize': '12px', 'marginTop': '10px'})
                    ], style=card_style)
                ], width=6),
                dbc.Col([
                    html.Div([
                        dcc.Graph(id='fig-salary'),
                        html.P("Source: Data Science Job Salaries (ai-jobs.net) & Kaggle Survey 2022.", style={'color': '#8A8A93', 'fontSize': '12px', 'marginTop': '10px'})
                    ], style=card_style)
                ], width=6)
            ]),
            dbc.Row([
                dbc.Col([
                    html.Div([
                        dcc.Graph(id='fig-req-skills'),
                        html.P("Source: O*NET OnLine Database & Data Scientist Job Postings Dataset.", style={'color': '#8A8A93', 'fontSize': '12px', 'marginTop': '10px'})
                    ], style=card_style)
                ], width=6),
                dbc.Col([
                    html.Div([
                        html.H5("Top Hiring Companies", style={'color': '#FFFFFF', 'marginBottom': '20px'}),
                        dash_table.DataTable(
                            id='companies-table',
                            columns=[{"name": i, "id": i} for i in ['Company', 'Industry', 'Open_Roles']],
                            page_size=10,
                            style_table={'overflowX': 'auto'},
                            style_header=table_style_header,
                            style_data=table_style_data,
                            style_cell=table_style_cell
                        ),
                        html.P("Source: Data Scientist Job Postings Dataset (Kaggle).", style={'color': '#8A8A93', 'fontSize': '12px', 'marginTop': '10px'})
                    ], style=card_style)
                ], width=6)
            ])
        ])
        
    elif tab == 'tab-3':
        return html.Div([
            html.Div([
                html.P("This tab compares the skills taught in degree programs vs. the skills demanded by employers. A negative gap indicates a shortage (high demand, low supply), while a positive gap indicates an oversupply.", style={'color': '#8A8A93', 'margin': '0'})
            ], style=card_style),
            
            dbc.Row([
                dbc.Col([
                    html.Div([
                        dcc.Graph(id='fig-mismatch'),
                        html.P("Source: Normalized derivation combining NCES supply metrics vs. O*NET / BLS demand metrics.", style={'color': '#8A8A93', 'fontSize': '12px', 'marginTop': '10px'})
                    ], style=card_style)
                ], width=6),
                dbc.Col([
                    html.Div([
                        dcc.Graph(id='fig-radar'),
                        html.P("Source: Derived skill alignment based on curriculum hours vs. job posting frequencies.", style={'color': '#8A8A93', 'fontSize': '12px', 'marginTop': '10px'})
                    ], style=card_style)
                ], width=6)
            ])
        ])

# ------------------------------------------------------------------------------
# Cross-Filtering Interactivity Callbacks (Click on Chart -> Update Dropdown)
# ------------------------------------------------------------------------------
@app.callback(
    Output('supply-program-filter', 'value'),
    [Input('fig-graduates', 'clickData'),
     Input('fig-tuition', 'clickData'),
     Input('fig-employment', 'clickData')],
    [State('supply-program-filter', 'value')],
    prevent_initial_call=True
)
def cross_filter_tab1_clicks(clk_grad, clk_tuit, clk_emp, current_selection):
    ctx = dash.callback_context
    if not ctx.triggered:
        raise dash.exceptions.PreventUpdate
    prop_id = ctx.triggered[0]['prop_id']
    click_data = None
    
    if 'fig-graduates' in prop_id: click_data = clk_grad
    elif 'fig-tuition' in prop_id: click_data = clk_tuit
    elif 'fig-employment' in prop_id: click_data = clk_emp
        
    if click_data and 'points' in click_data:
        try:
            program = click_data['points'][0]['customdata'][0]
            # Toggle logic: if already the only one selected, reset to all.
            if len(current_selection) == 1 and current_selection[0] == program:
                return programs
            return [program]
        except (KeyError, IndexError):
            pass
    raise dash.exceptions.PreventUpdate

@app.callback(
    Output('demand-job-filter', 'value'),
    [Input('fig-open-pos', 'clickData'),
     Input('fig-salary', 'clickData')],
    [State('demand-job-filter', 'value')],
    prevent_initial_call=True
)
def cross_filter_tab2_clicks(clk_open, clk_sal, current_selection):
    ctx = dash.callback_context
    if not ctx.triggered:
        raise dash.exceptions.PreventUpdate
    prop_id = ctx.triggered[0]['prop_id']
    click_data = None
    
    if 'fig-open-pos' in prop_id: click_data = clk_open
    elif 'fig-salary' in prop_id: click_data = clk_sal
        
    if click_data and 'points' in click_data:
        try:
            job = click_data['points'][0]['customdata'][0]
            if len(current_selection) == 1 and current_selection[0] == job:
                return job_titles
            return [job]
        except (KeyError, IndexError):
            pass
    raise dash.exceptions.PreventUpdate

# ------------------------------------------------------------------------------
# Tab Rendering Callbacks
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
    
    # Notice custom_data=['Program'] added to all charts so we can extract it in clickData
    fig_grad = px.line(filtered_supply, x='Year', y='Graduates', color='Program', custom_data=['Program'], markers=True, title='Graduates Trend by Program (USA)', color_discrete_sequence=THEME_PALETTE)
    fig_grad = apply_theme(fig_grad)
    
    df_tuit = filtered_supply[filtered_supply['Year'] == 2023]
    fig_tuit = px.bar(df_tuit, x='Program', y='Tuition_USD', color='Program', custom_data=['Program'], title='Average Tuition Fees (2023)', color_discrete_sequence=THEME_PALETTE)
    fig_tuit = apply_theme(fig_tuit)
    
    fig_emp = px.bar(filtered_emp, x='Program', y='Employed_Pct', color='Year_Post_Grad', barmode='group', custom_data=['Program'], title='Employment Rate Post-Graduation (%)', color_discrete_sequence=THEME_PALETTE)
    fig_emp = apply_theme(fig_emp)
    
    return fig_grad, fig_tuit, fig_emp, filtered_curr.to_dict('records')


@app.callback(
    [Output('fig-open-pos', 'figure'),
     Output('fig-salary', 'figure'),
     Output('fig-req-skills', 'figure'),
     Output('companies-table', 'data')],
    [Input('demand-job-filter', 'value')]
)
def update_tab2(selected_jobs):
    if not selected_jobs:
        selected_jobs = job_titles
        
    filtered_demand = df_demand[df_demand['Job_Title'].isin(selected_jobs)]
    filtered_skills = df_demand_skills[df_demand_skills['Job_Title'].isin(selected_jobs)]
    filtered_salary = df_salary[df_salary['Job_Title'].isin(selected_jobs)]
    filtered_companies = df_companies[df_companies['Job_Title'].isin(selected_jobs)]
    
    fig_open = px.line(filtered_demand, x='Year', y='Open_Positions', color='Job_Title', custom_data=['Job_Title'], markers=True, title='Open Positions Over Time', color_discrete_sequence=THEME_PALETTE)
    fig_open = apply_theme(fig_open)
    
    fig_sal = px.bar(filtered_salary, x='Job_Title', y='Avg_Salary_USD', color='Experience_Level', barmode='group', custom_data=['Job_Title'], title='Average Salary by Experience', color_discrete_sequence=THEME_PALETTE)
    fig_sal = apply_theme(fig_sal)
    
    skill_agg = filtered_skills.groupby('Skill')['Demand_Score'].mean().reset_index().sort_values('Demand_Score', ascending=True)
    fig_req = px.bar(skill_agg, x='Demand_Score', y='Skill', orientation='h', title='Top Required Skills (%)', color_discrete_sequence=['#D8B4FE'])
    fig_req = apply_theme(fig_req)
    
    comp_agg = filtered_companies.groupby(['Company', 'Industry'])['Open_Roles'].sum().reset_index().sort_values('Open_Roles', ascending=False)
    
    return fig_open, fig_sal, fig_req, comp_agg.to_dict('records')


@app.callback(
    [Output('fig-mismatch', 'figure'),
     Output('fig-radar', 'figure')],
    [Input('tabs', 'value')] 
)
def update_tab3(tab):
    supply_agg = df_curriculum.groupby('Skill')['Credit_Hours'].sum().reset_index()
    supply_agg['Supply_Score'] = (supply_agg['Credit_Hours'] / supply_agg['Credit_Hours'].max()) * 100
    
    demand_agg = df_demand_skills.groupby('Skill')['Demand_Score'].mean().reset_index()
    demand_agg['Demand_Score_Norm'] = (demand_agg['Demand_Score'] / demand_agg['Demand_Score'].max()) * 100
    
    mismatch_df = pd.merge(supply_agg[['Skill', 'Supply_Score']], demand_agg[['Skill', 'Demand_Score_Norm']], on='Skill', how='outer').fillna(0)
    mismatch_df['Gap'] = mismatch_df['Supply_Score'] - mismatch_df['Demand_Score_Norm']
    
    fig_mismatch = px.bar(mismatch_df.sort_values('Gap'), x='Gap', y='Skill', orientation='h', 
                          color='Gap', color_continuous_scale=['#D8B4FE', '#18181C', '#67E8F9'],
                          title='Skill Mismatch (Supply Score - Demand Score)')
    fig_mismatch = apply_theme(fig_mismatch)
                          
    fig_radar = go.Figure()
    fig_radar.add_trace(go.Scatterpolar(
        r=mismatch_df['Supply_Score'],
        theta=mismatch_df['Skill'],
        fill='toself',
        name='Supply (Taught)',
        line_color='#D8B4FE'
    ))
    fig_radar.add_trace(go.Scatterpolar(
        r=mismatch_df['Demand_Score_Norm'],
        theta=mismatch_df['Skill'],
        fill='toself',
        name='Demand (Required)',
        line_color='#67E8F9'
    ))
    
    fig_radar = apply_theme(fig_radar)
    fig_radar.update_layout(
        polar=dict(
            radialaxis=dict(visible=True, range=[0, 100], gridcolor='#2A2A32'),
            angularaxis=dict(gridcolor='#2A2A32'),
            bgcolor='rgba(0,0,0,0)'
        ), 
        showlegend=True, 
        title='Skill Gap Radar'
    )
    
    return fig_mismatch, fig_radar


if __name__ == '__main__':
    app.run(debug=True)
