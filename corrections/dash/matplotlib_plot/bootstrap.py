import dash_bootstrap_components as dbc
import dash_html_components as html
import dash

app = dash.Dash(__name__)

row = html.Div(
    [
        dbc.Row(dbc.Col(html.Div("A single, half-width column"), width=6)),
        dbc.Row(
            dbc.Col(html.Div("An automatically sized column"), width="auto")
        ),
        dbc.Row(
            [
                dbc.Col(html.Div("One of three columns"), width=3),
                dbc.Col(html.Div("One of three columns")),
                dbc.Col(html.Div("One of three columns"), width=3),
            ]
        ),
    ]
)

app.layout = row
 

if __name__ == '__main__':
    app.run_server(debug=True)