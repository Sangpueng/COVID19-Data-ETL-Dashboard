import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd
import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('C:/tmp/healthcare_data.db')

# Read the data from the covid19_data table into a pandas DataFrame
df = pd.read_sql_query("SELECT * FROM covid19_data", conn)

# Close the database connection
conn.close()

# Transform the DataFrame for visualization
df_melted = df.melt(id_vars=["Country/Region", "Province/State"], 
                    var_name="Date", 
                    value_name="Cases")

# Combine 'Country/Region' and 'Province/State' into a single column if needed
df_melted['Location'] = df_melted['Country/Region'] + ', ' + df_melted['Province/State'].fillna('')

# Apply a 7-day rolling average to smooth out the data
df_melted['Cases'] = df_melted.groupby('Location')['Cases'].transform(lambda x: x.rolling(window=7, min_periods=1).mean())

# Create the Dash application
app = dash.Dash(__name__)

# Define the layout of the dashboard with a dropdown for location selection
app.layout = html.Div([
    html.H1("COVID-19 Dashboard"),
    html.Div("A dashboard to display COVID-19 data."),
    dcc.Dropdown(
        id='location-dropdown',
        options=[{'label': loc, 'value': loc} for loc in df_melted['Location'].unique()],
        value=['US, 0', 'India, 0', 'Brazil, 0','Thailand, 0'],  # Default selected locations
        multi=True
    ),
    dcc.Graph(id='covid-graph'),
    dcc.RangeSlider(
        id='date-slider',
        min=0,
        max=len(df_melted['Date'].unique()) - 1,
        value=[0, len(df_melted['Date'].unique()) - 1],
        marks={i: date for i, date in enumerate(df_melted['Date'].unique()[::30])},  # Adjust the step for marks
        step=None
    )
])

# Callback to update the graph based on selected locations and date range
@app.callback(
    dash.dependencies.Output('covid-graph', 'figure'),
    [dash.dependencies.Input('location-dropdown', 'value'),
     dash.dependencies.Input('date-slider', 'value')]
)
def update_figure(selected_locations, date_range):
    filtered_df = df_melted[df_melted['Location'].isin(selected_locations)]
    filtered_df = filtered_df[(filtered_df['Date'] >= df_melted['Date'].unique()[date_range[0]]) &
                              (filtered_df['Date'] <= df_melted['Date'].unique()[date_range[1]])]
    fig = px.line(filtered_df, x='Date', y='Cases', color='Location', title="COVID-19 Cases Over Time")
    
    # Customize the figure
    fig.update_layout(
        xaxis_title="Date",
        yaxis_title="Number of Cases (7-day Average)",
        hovermode="x unified",
        legend_title_text='Location',
        yaxis_type="log"  # Apply logarithmic scale
    )
    fig.update_traces(mode='lines+markers', marker=dict(size=4))
    return fig

# Run the application
if __name__ == '__main__':
    app.run_server(debug=True, host='0.0.0.0', port=8050)
