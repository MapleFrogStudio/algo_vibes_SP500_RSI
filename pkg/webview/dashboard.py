import os
import pandas as pd
import yfinance as yf

import plotly.graph_objs as go
from dash import Dash, dcc, html, Output, Input

#app = Dash(__name__, external_stylesheets=[os.path.join('pkg','webview','css', 'dashboard.css')])
app = Dash(__name__, assets_folder='assets')
# app.css.append_css({
#     "external_url": "dashboard.css"
# })

print(__name__)

df = yf.download('TSLA')
print(df)

candle_start = 200
candle_end = 500
candlestick = go.Candlestick(x = df.iloc[candle_start:candle_end].index,
                             open = df.iloc[candle_start:candle_end]["Open"],
                             high = df.iloc[candle_start:candle_end]["High"],
                             low  = df.iloc[candle_start:candle_end]["Low"],
                             close= df.iloc[candle_start:candle_end]["Close"])




main_graph = [
    html.P("Left Graph")
]

graph_stack = [
        html.Div("Graph 1", className="stacked"),
        html.Div("Graph 2", className="stacked"),
        html.Div("Graph 3", className="stacked"),
        html.Div("Graph 4", className="stacked"),
        html.Div("Graph 5", className="stacked"),
        html.Div("Graph 6", className="stacked")
]

app.layout = html.Div(
    [
        html.Div([
            html.P("Hello World!")
        ], className="header"),

        html.Div([
            html.Div([    
                dcc.Graph(
                    figure=go.Figure(
                        data=[candlestick],
                        layout={
                            "margin": {"t":0,"r":0,"b":0,"l":0},
                            "plot_bgcolor": "black",
                            "xaxis": {"showgrid": False, "gridcolor": "gray", "gridwidth": 0.5, "griddash":"dot"},
                            "yaxis": {"showgrid": False, "gridcolor": "gray", "gridwidth": 0.5, "griddash":"dot"},
                        }
                    ),
                    config={"displayModeBar": False}
            )], className="left_graph"),
            html.Div(graph_stack, className="right_graph"),
        ],className="graphs_2col_area"),

        html.Div([
            html.P("Footer area")
        ],className="footer")
    ], className="full-screen")


def main():
    app.run_server(debug=True, port=8086)

if __name__ == '__main__':
    main()