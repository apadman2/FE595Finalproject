from results import Analysis
import plotly.express as px

class Plot:
    def __init__(self, budget, genre, n, v, l, plot):
        self.budget = budget
        self.genre = genre
        self.nudity = n
        self.violence = v
        self.language = l
        self.plot = plot

    def figure(self):
        og_data = Analysis(self.budget * 1000000, list(self.genre), self.nudity
                           , self.violence, self.language, self.plot)
        og_data1 = og_data.data()
        imdb_rating = og_data.rating()
        fig = px.scatter(data_frame=og_data1, x='Index', y='IMDB Rating', size='Budget',
                         hover_name='Name', hover_data=['IMDB Rating', 'Budget'])
        fig.add_scatter(x=[800], y=[float(imdb_rating)], mode='markers', name='OUR MOVIE',
                        marker=dict(size=20, color='Red', symbol='cross'),
                        hovertemplate=
                        '<i><b>OUR MOVIE</b></i><br>'
                        '<br>' +
                        'IMDB Rating=%{y}<br>')
        fig.update_layout(plot_bgcolor='#00bd81',
                          paper_bgcolor='#00bd81',
                          font_color='Black', )
        fig.update_xaxes(gridcolor='Black')
        fig.update_yaxes(gridcolor='Black')
        return fig
