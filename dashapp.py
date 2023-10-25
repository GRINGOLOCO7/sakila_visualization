import dash
from dash import html,dcc
from dash.dependencies import Input, Output
import pandas as pd
from sqlalchemy import create_engine
import pymysql

pymysql.install_as_MySQLdb()
# Connect to the Sakila database
engine = create_engine('mysql://root:Stambek7@localhost/sakila')

# Create the Dash app
app = dash.Dash(__name__)

# Define the layout of the app
app.layout = html.Div([
    html.H1("Sakila Rental Data Over Time"),
    
    # Dropdown to select a category
    dcc.Dropdown(
        id='category-dropdown',
        options=[
            {'label': 'Category 1', 'value': 1},
            {'label': 'Category 2', 'value': 2},
            # Add more options based on your data
        ],
        value=1  # Default selected option
    ),
    
    # Line chart to display data over time
    dcc.Graph(id='line-chart')   ############ copy it change it to a new chart and redo it with diffreent output and query
])
######### download inploxDB

# Define callback to update the line chart based on the selected category
@app.callback(
    Output('line-chart', 'figure'),   ########### sold match with dcc.Graph(id='line-chart')
    [Input('category-dropdown', 'value')]
)############# when category change reload
def update_line_chart(selected_category):
    # SQL query to retrieve data for the selected category over time
    query = f"""
    SELECT DATE(rental_date) AS rental_day, COUNT(rental_id) AS rental_count
    FROM rental, inventory, film, film_category
    WHERE rental.inventory_id = inventory.inventory_id AND
    inventory.film_id = film.film_id AND
    film.film_id = film_category.film_id AND
    category_id = {selected_category}
    GROUP BY rental_day;
    """

    rental_data = pd.read_sql(query, engine)

    # Create the line chart
    fig = {
        'data': [
            {
                'x': rental_data['rental_day'],
                'y': rental_data['rental_count'],
                'type': 'bar',  ################ bar/line/...
                'marker': {'color': 'blue'}
            }
        ],
        'layout': {
            'title': f'Rental Count for Category {selected_category}',
            'xaxis': {'title': 'Rental Day'},
            'yaxis': {'title': 'Rental Count'}
        }
    }

    return fig

if __name__ == '__main__':
    app.run_server(debug=True)
