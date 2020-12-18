import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import pandas as pd
import plotly.graph_objs as go
from dash.dependencies import Input, Output

data = pd.DataFrame(
    {
        "item": [
            "Red square",
            "Red circle",
            "Blue square",
            "Blue circle",
            "Green square",
            "Green circle",
        ],
        "color": ["red", "red", "blue", "blue", "green", "green"],
        "shape": ["square", "circle", "square", "circle", "square", "circle"],
        "qty": [3, 2, 5, 3, 2, 6],
    }
)

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = dbc.Container(
    [
        dbc.DropdownMenu(
            [
                dbc.DropdownMenuItem("All", id="all"),
                dbc.DropdownMenuItem(divider=True),
                dbc.DropdownMenuItem("Color", header=True),
                dbc.DropdownMenuItem("Red", id="red"),
                dbc.DropdownMenuItem("Blue", id="blue"),
                dbc.DropdownMenuItem("Green", id="green"),
                dbc.DropdownMenuItem(divider=True),
                dbc.DropdownMenuItem("Shape", header=True),
                dbc.DropdownMenuItem("Square", id="square"),
                dbc.DropdownMenuItem("Circle", id="circle"),
            ],
            label="Filter plot",
            className="mb-3",  # add bottom margin
        ),
        dcc.Graph(id="graph"),
    ]
)


@app.callback(
    Output("graph", "figure"),
    [
        Input("all", "n_clicks"),
        Input("red", "n_clicks"),
        Input("blue", "n_clicks"),
        Input("green", "n_clicks"),
        Input("square", "n_clicks"),
        Input("circle", "n_clicks"),
    ],
)
def make_graph(*args):
    ctx = dash.callback_context

    if not ctx.triggered:
        button_id = "all"
    else:
        button_id = ctx.triggered[0]["prop_id"].split(".")[0]

    if button_id in ["red", "blue", "green"]:
        df = data.loc[data["color"] == button_id, :]
    elif button_id in ["square", "circle"]:
        df = data.loc[data["shape"] == button_id, :]
    else:
        df = data

    return go.Figure(data=[go.Pie(labels=df["item"], values=df["qty"])])


if __name__ == "__main__":
    app.run_server()
