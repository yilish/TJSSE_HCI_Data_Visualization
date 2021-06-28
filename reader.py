import numpy as np
import pandas as pd

# 加载plotly包
# import plotly.plotly as py
from plotly.offline import init_notebook_mode, iplot
# init_notebook_mode(connected=True)
import plotly.graph_objs as go

# 云词库

# 加载matplotlib包
import matplotlib.pyplot as plt
import plotly.graph_objs as go
import plotly.express as px


def get_salary_plot_by_region():
    df = pd.read_csv('dataset/college-salaries/salaries-by-region.csv')
    for i in range(len(df.columns)):
        if df.columns[i] != 'School Name' and df.columns[i] != 'Region':
            df[df.columns[i:]] = df[df.columns[i:]].replace('[\$,]', '', regex=True).astype(float)

    group = df.groupby('Region').mean() # type: pd.DataFrame
    data = []
    # print(group.columns)
    l = ['Starting Median Salary',
           'Mid-Career 10th Percentile Salary',
           'Mid-Career 25th Percentile Salary',
           'Mid-Career Median Salary',
           'Mid-Career 75th Percentile Salary',
           'Mid-Career 90th Percentile Salary']
    idx = [0, 2, 3, 1, 4, 5]
    # print((group.iloc[0].name))
    for i in range(len(group)):
        trace = go.Scatter(x=l, y=group.iloc[i][idx],
                            name=group.iloc[i].name,
                           showlegend=True)
        data.append(trace)
    layout = dict(title='Average salaries of different stages of career by region')

    # 将data与layout组合为一个图像
    fig = dict(data = data, layout = layout)
    return fig

def get_salary_plot_by_school_type():
    df = pd.read_csv('dataset/college-salaries/salaries-by-college-type.csv')
    for i in range(len(df.columns)):
        if df.columns[i] != 'School Name' and df.columns[i] != 'School Type':
            df[df.columns[i:]] = df[df.columns[i:]].replace('[\$,]', '', regex=True).astype(float)

    group = df.groupby('School Type').mean() # type: pd.DataFrame
    data = []
    # print(group.columns)
    l = ['Starting Median Salary',
           'Mid-Career 10th Percentile Salary',
           'Mid-Career 25th Percentile Salary',
           'Mid-Career Median Salary',
           'Mid-Career 75th Percentile Salary',
           'Mid-Career 90th Percentile Salary']
    idx = [0, 2, 3, 1, 4, 5]
    # print((group.iloc[0].name))
    for i in range(len(group)):
        trace = go.Scatter(x=l, y=group.iloc[i][idx],
                            name=group.iloc[i].name,
                           showlegend=True)
        data.append(trace)
    layout = dict(                  title='Average salaries of different stages of career by school type')

    # 将data与layout组合为一个图像
    fig = dict(data = data, layout = layout)
    return fig
# fig = get_salary_plot_by_school_type()
# iplot(fig)
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
    layout = dict(title='Average salaries of different stages of career by school type')

    # 将data与layout组合为一个图像
    fig = dict(data=data, layout=layout)
    return fig

def get_salary_plot_by_degree():
    df = pd.read_csv('dataset/college-salaries/degrees-that-pay-back.csv')
    for i in range(len(df.columns)):
        if df.columns[i] != 'School Name' and df.columns[i] != 'Undergraduate Major':
            df[df.columns[i:]] = df[df.columns[i:]].replace('[\$,]', '', regex=True).astype(float)

    group = df.groupby('Undergraduate Major').mean() # type: pd.DataFrame
    data = []
    # print(group.columns)
    l = ['Starting Median Salary',
           'Mid-Career 10th Percentile Salary',
           'Mid-Career 25th Percentile Salary',
           'Mid-Career Median Salary',
           'Mid-Career 75th Percentile Salary',
           'Mid-Career 90th Percentile Salary']
    idx = [0, 3, 4, 1, 5, 6]
    # print((group.iloc[0].name))
    for i in range(len(group)):
        trace = go.Scatter(x=l, y=group.iloc[i][idx],
                            name=group.iloc[i].name,
                           showlegend=True)
        data.append(trace)
    layout = dict(                  title='Average salaries of different stages of career by degree major')

    # 将data与layout组合为一个图像
    fig = dict(data = data, layout = layout)
    return fig

def get_sunbrast():
    df = pd.read_csv('dataset/college-salaries/salaries-by-region.csv')
    for i in range(len(df.columns)):
        if df.columns[i] != 'School Name' and df.columns[i] != 'Region':
            df[df.columns[i:]] = df[df.columns[i:]].replace('[\$,]', '', regex=True).astype(float)

    fig = px.sunburst(df, path=['Region', 'School Name'], values='Mid-Career Median Salary',
                      color='Mid-Career Median Salary',
                      color_continuous_scale='RdBu'
                      )

    return fig
def get_sunbrast_by_school_type():
    df = pd.read_csv('dataset/college-salaries/salaries-by-college-type.csv')
    for i in range(len(df.columns)):
        if df.columns[i] != 'School Name' and df.columns[i] != 'School Type':
            df[df.columns[i:]] = df[df.columns[i:]].replace('[\$,]', '', regex=True).astype(float)

    fig = px.sunburst(df, path=['School Type', 'School Name'], values='Mid-Career Median Salary',
                      color='Mid-Career Median Salary',
                      color_continuous_scale='RdBu'
                      )

    return fig
# if __name__ == '__main__':
#     fig = get_sunbrast_by_school_type()
#     iplot(fig)
