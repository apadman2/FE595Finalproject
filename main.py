import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
from results import Analysis
from sentiment import Senti
from plotting import Plot

# Stylesheet
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
app.config['suppress_callback_exceptions'] = True

# Figure
fig = {}

# Layout
app.layout = html.Div(children=[
    html.Div(
        children='IMDB Rating Predictor',
        style={'fontSize': 60,
               'color': 'White',
               'background': '#000000'
               }),
    html.Br(),
    html.Div(children=['Budget: ',
                       dcc.Slider(
                           id='budget_slider',
                           min=100,
                           max=300,
                           step=50,
                           value=200,
                           marks={
                               100: '100', 150: '150', 200: '200', 250: '250', 300: '300'
                           },
                       )],
             style={'fontSize': 30,
                    }),
    html.Div(
        id='budget_result',
        style={'fontSize': 40,
               'color': 'Black'
               }),
    html.Br(),
    html.Div(
        dcc.Checklist(
            id='genre_checklist',
            value=[1, 2],
            options=[
                {'label': 'Action', 'value': 1},
                {'label': 'Comedy', 'value': 2},
                {'label': 'Crime', 'value': 3},
                {'label': 'Drama', 'value': 4},
                {'label': 'Sci-Fi', 'value': 5},
                {'label': 'Adventure', 'value': 6},
                {'label': 'Family', 'value': 7},
                {'label': 'Thriller', 'value': 8},
                {'label': 'Fantasy', 'value': 9},
                {'label': 'Horror', 'value': 10},
                {'label': 'Mystery', 'value': 11},
                {'label': 'Animation', 'value': 12},
                {'label': 'Romance', 'value': 13},
                {'label': 'Historical', 'value': 14},
                {'label': 'Sports', 'value': 15},
                {'label': 'Music', 'value': 16},
                {'label': 'War', 'value': 17},
                {'label': 'Western', 'value': 18},
            ],
            labelStyle={'display': 'inline-block',
                        'width': '10%'}
        ), style={'fontSize': 20,
                  }),
    html.Br(),
    html.Div(children=['Sex/ Nudity:',
                       html.Br(),
                       dcc.Slider(
                           id='nudity_slider',
                           min=0,
                           max=10,
                           step=1,
                           value=5,
                           marks={
                               0: '0', 1: '1', 2: '2', 3: '3', 4: '4',
                               5: '5', 6: '6', 7: '7', 8: '8', 9: '9',
                               10: '10'
                           },
                       )],
             style={'fontSize': 30,
                    }),
    html.Div(
        children='5',
        id='nudity_result',
        style={'fontSize': 40,
               'color': 'Black'
               }),
    html.Br(),
    html.Div(children=['Violence:',
                       html.Br(),
                       dcc.Slider(
                           id='violence_slider',
                           min=0,
                           max=10,
                           step=1,
                           value=5,
                           marks={
                               0: '0', 1: '1', 2: '2', 3: '3', 4: '4',
                               5: '5', 6: '6', 7: '7', 8: '8', 9: '9',
                               10: '10'
                           },
                       )],
             style={'fontSize': 30,
                    }),
    html.Div(
        children='5',
        id='violence_result',
        style={'fontSize': 40,
               'color': 'Black'
               }),
    html.Div(children=['Language:',
                       html.Br(),
                       dcc.Slider(
                           id='language_slider',
                           min=0,
                           max=10,
                           step=1,
                           value=5,
                           marks={
                               0: '0', 1: '1', 2: '2', 3: '3', 4: '4',
                               5: '5', 6: '6', 7: '7', 8: '8', 9: '9',
                               10: '10'
                           },
                       )],
             style={'fontSize': 30,
                    }),
    html.Div(
        children='5',
        id='language_result',
        style={'fontSize': 40,
               'color': 'Black'
               }),
    html.Br(),
    html.Div(children=['Plot of the movie: ',
                       dbc.Input(id='plot_input',
                                 value='The quick brown fox jumped over the lazy dog',
                                 type='text',
                                 size='lg')],
             style={'fontSize': 30,
                    }),
    html.Div(
        [
            dbc.Button('Submit',
                       id='submit',
                       n_clicks=0,
                       size='lg',
                       color='success')
        ],
    ),
    html.Br(),
    html.Div(
        id='imdb_result',
        children='IMDB Rating:',
        style={'fontSize': 60,
               'color': 'White',
               'text-align': 'left',
               'background': '#000000',
               }),
    html.Div(
        dcc.Graph(id='graph_results', figure=fig),
    )
], style={'padding': '0px',
          'font-family': 'Trebuchet MS, sans-serif',
          'color': 'White',
          'background': '#00bd81',
          'text-align': 'center'})

@app.callback(
    Output('budget_result', 'children'),
    Input('budget_slider', 'value')
)
def update_output2(value):
    return '{} Million'.format(value)

@app.callback(
    Output('nudity_result', 'children'),
    Input('nudity_slider', 'value')
)
def update_output4(value):
    return '{}'.format(value)


@app.callback(
    Output('violence_result', 'children'),
    Input('violence_slider', 'value')
)
def update_output5(value):
    return '{}'.format(value)


@app.callback(
    Output('language_result', 'children'),
    Input('language_slider', 'value')
)
def update_output6(value):
    return '{}'.format(value)


@app.callback(
    Output('imdb_result', 'children'),
    Input('submit', 'n_clicks'),
    State('budget_slider', 'value'),
    State('genre_checklist', 'value'),
    State('nudity_slider', 'value'),
    State('violence_slider', 'value'),
    State('language_slider', 'value'),
    State('plot_input', 'value')
)
def clicks(n, budget, genre, nudity, violence, language, plot):
    plot_senti = Senti(str(plot))
    plot_senti = plot_senti.sentiment()
    og_data = Analysis(budget * 1000000, list(genre), nudity, violence, language, float(plot_senti))
    og_data1 = og_data.rating()
    return "IMDB Rating: {}".format(og_data1)

@app.callback(
    Output('graph_results', 'figure'),
    Input('submit', 'n_clicks'),
    State('budget_slider', 'value'),
    State('genre_checklist', 'value'),
    State('nudity_slider', 'value'),
    State('violence_slider', 'value'),
    State('language_slider', 'value'),
    State('plot_input', 'value')
)
def plottt(n, budget, genre, nudity, violence, language, plot):
    plot_senti = Senti(str(plot))
    plot_senti = plot_senti.sentiment()
    dtf = Plot(budget, genre, nudity, violence, language, plot_senti)
    fig = dtf.figure()
    return fig


if __name__ == '__main__':
    app.run_server()
