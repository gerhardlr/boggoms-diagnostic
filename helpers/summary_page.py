import plotly.express as px



def make_plot():
    df = px.data.iris()
    fig = px.scatter(df, x="sepal_width", y="sepal_length", color="species")
    return fig.to_html(full_html=False)  # This gives you embeddable HTML/JS
