import requests

# 执行api调用并存储响应
url = 'https://api.github.com/search/repositories?q=language:python&shot=stars'
headers = {
    'Accept': 'application/vnd.github.v3+json'
}
resp = requests.get(url, headers=headers)
print(f'状态码：{resp.status_code}')
# 将api响应的结果赋予一个变量
resp_dict = resp.json()
# 处理结果
print(resp_dict.keys())
print(f'返回总数:{resp_dict["total_count"]}')
# 探索有关仓库的信息
repo_dict = resp_dict["items"]
print(f'仓库相关信息:{len(repo_dict)}')
# 研究第一个结果
repo_dict = repo_dict[0]
print(f'\n键数量：{len(repo_dict)}')
for key in sorted(repo_dict.keys()):
    print(key)

