import json
import plotly.express as px

# 探索数据结构
filename = 'eq_data_1_day_m1.json'
with open(filename) as f:
    all_eq_data = json.load(f)

readable_file = 'readable_eq_data.json'
with open(readable_file, 'w') as f:
    # indent表示让dump（）使用与数据结构匹配的缩进量来设置格式
    json.dump(all_eq_data, f, indent=4)
# 创建地震列表
all_eq_dicts = all_eq_data['features']
# print(len(all_eq_dicts))
# 提取震级
mags, titles, lons, lats = [], [], [], []
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    title = eq_dict['properties']['title']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    mags.append(mag)
    titles.append(titles)
    lons.append(lon)
    lats.append(lat)

# print(mags[:10])
# print(titles[:2])
# print(lons[:5])
# print(lats[:5])


fig = px.scatter(
    x=lons,
    y=lats,
    labels={'x': '精度', 'y': '纬度'},
    range_x=[-200, 200],
    range_y=[-90, 90],
    width=800,
    height=800,
    title='全球地震散点图',
)
fig.write_html('global_earthquakes.html')
fig.show()
