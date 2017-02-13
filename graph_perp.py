import numpy as np
import plotly.graph_objs as go
import plotly.plotly as py

data = np.loadtxt("perp-200unit_30pct_45epoch.npy")
trace = go.Scatter(
    x=data[:, 0],
    y=data[:, 1],
    mode="markers"
)
layout = go.Layout(
    title='Perplexity of Country Bot',
    xaxis={
        "title": 'Number of Iterations'
    },
    yaxis={
        "title": 'Perplexity'
    }
)
fig = go.Figure(data=[trace], layout=layout)
plot_url = py.plot(fig, filename='perplexity')
print plot_url
