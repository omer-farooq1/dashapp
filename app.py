import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()
server = app.server

githublink='https://github.com/omer-farooq1/dashapp'

app.layout = html.Div(children=[
    html.H1(children="Procurement App"),

    html.Div(children='''This is Dash running on Heroku App Service.'''),

    dcc.Graph(
        id='Sample-graph',
        figure={
            'data': [
                {'x': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 'y': [803747, 709575, 40866, 879601, 645072, 41661, 280703, 576471, 745123, 872586, 369037, 51552], 'type': 'bar', 'name': 'Invoices'},
            ],
            'layout': {
                'title': 'Spend Over Time'
            }
        }
    ),

    html.A('Code on Github', href=githublink)
])

if __name__ == "__main__":
    app.run_server()
