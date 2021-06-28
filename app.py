import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd
import reader
app = dash.Dash()


app.layout = html.Div([
    html.Div([
        html.Div([
            html.Div([
                dcc.Dropdown(
                    id='filter',
                    options=[{'label': i, 'value': i} for i in ['Region', 'Undergraduate Major', 'School Type']],
                    value='Region',
                    style={'width': '80%'}
                ),

                dcc.Graph(id='avg_salary', figure=reader.get_salary_plot_by_region()),
                html.Br(),
            ], style={'width': '49%'}),
            html.Div([
                dcc.Dropdown(
                    id='stage-selector',
                    options=[{'label': i, 'value': i} for i in ['Starting Median Salary',
                                                               'Mid-Career 10th Percentile Salary',
                                                               'Mid-Career 25th Percentile Salary',
                                                               'Mid-Career Median Salary',
                                                               'Mid-Career 75th Percentile Salary',
                                                               'Mid-Career 90th Percentile Salary']],
                    value='Starting Median Salary',
                    style={'width': '80%', 'margin-left': '5%'}
                ),
                dcc.Graph(id='selected_part')
            ], style={'width': '49%'})
        ], style={'display': 'flex'}),
        html.Div([
            dcc.Dropdown(id='distribution-selector',
                         options=[{'label': i, 'value': i} for i in ['Region', 'School Type']],
                         value='Region',
                         style={'width': '80%'}
                         ),

            dcc.Graph(id='distribution')
        ], style={'width': '50%'})
    ])
])

@app.callback(
    dash.dependencies.Output('distribution', 'figure'),
    dash.dependencies.Input('distribution-selector', 'value')
)
def update_distribution(dis):
    if dis == 'Region':
        return reader.get_sunbrast()
    else:
        return reader.get_sunbrast_by_school_type()


@app.callback(
    dash.dependencies.Output('avg_salary', 'figure'),
    dash.dependencies.Input('filter', 'value')
)
def update_avg_fig(filter):
    # print(filter.options)
    if filter == 'Region':
        return reader.get_salary_plot_by_region()
    elif filter == 'School Type':
        return reader.get_salary_plot_by_school_type()

    return reader.get_salary_plot_by_degree()


@app.callback(
    dash.dependencies.Output('selected_part', 'figure'),
    [dash.dependencies.Input('stage-selector', 'value'),
     dash.dependencies.Input('filter', 'value')]
)
def update_avg_fig(stage, filter):
    # ['Region', 'Undergraduate Major', 'School Type']
    if filter == 'Region':
        df = pd.read_csv('dataset/college-salaries/salaries-by-region.csv')
    elif filter == 'Undergraduate Major':
        df = pd.read_csv('dataset/college-salaries/degrees-that-pay-back.csv')
    else:
        df = pd.read_csv('dataset/college-salaries/salaries-by-college-type.csv')
    for i in range(len(df.columns)):
        if df.columns[i] != 'School Name' and df.columns[i] != filter:
            df[df.columns[i:]] = df[df.columns[i:]].replace('[\$,]', '', regex=True).astype(float)
    data = []
    group = df.groupby(filter)
    for idx, item in group:
        trace = go.Box(y=item[stage], name=idx)
        data.append(trace)
    layout = dict(title='Salary distribution of ' + stage + ' by ' + filter)

    # 将data与layout组合为一个图像
    fig = dict(data=data, layout=layout)
    return fig

app.css.append_css({
    'external_url': 'https://codepen.io/chriddyp/pen/bWLwgP.css'
})


if __name__ == '__main__':
    app.run_server(debug=True, host='localhost')