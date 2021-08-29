import plotly.express as px

import eq_explore_data
fig = px.scatter(
    x=eq_explore_data.lons,
    y=eq_explore_data.lats,
    labels={'x':'精度', 'y':'纬度'},
    range_x=[-200, 200],
    range_y=[-90, 90],
    width=800,
    height=800,
    title='全球地震散点图',
)
fig.write_html('global_earthquakes.html')
fig.show()
