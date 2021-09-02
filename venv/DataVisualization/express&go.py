import plotly.express as px
import plotly.graph_objects as go

fig = px.scatter(person, x=cat1, y=cat2, color=person[cat1],
                 title=f"Career Relationship of {name}'s in {cat1} & {cat2}")
fig.show()

fig = go.Figure(data=go.Scatter(x=person[cat1], y=person[cat2], mode='markers',
                                marker=dict(size=20, color=person[cat2], showscale=True, line_width=1)))
fig.show()
