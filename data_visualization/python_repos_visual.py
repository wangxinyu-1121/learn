import requests
from plotly.graph_objs import Bar
from plotly import offline

# 执行api调用并存储响应
url = 'https://api.github.com/search/repositories?q=language:python&shot=stars'
headers = {
    'Accept': 'application/vnd.github.v3+json'
}
resp = requests.get(url, headers=headers)
print(f'状态码：{resp.status_code}')
# 处理结果
resp_dict = resp.json()
repo_dicts = resp_dict['items']
repo_names, stars, labels = [], [], []
for repo_dict in repo_dicts:
    repo_names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])

    owner = repo_dict['owner']['login']
    description = repo_dict['description']
    label = f'{owner}</br />{description}'
    labels.append(label)

# 可视化
data = [{
    'type': 'bar',
    'x': repo_names,
    'y': stars,
    'hovertext': labels,
    'marker': {
        'color': 'rgb(60, 100, 150)',
        'line': {
            'width': 1.5,
            'color': 'rgb(25, 25, 25)',
        },
    },
    'opacity': 0.6,
}]
my_layout = {
    'title': 'Github上最受欢迎的python项目',
    'titlefont': {'size': 28},
    'xaxis': {
        'title': '项目',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},
    },
    'yaxis': {
        'title': '标星',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},
    },
}
fig = {
    'data': data,
    'layout': my_layout,
}
offline.plot(fig, filename='python_repos.html')
