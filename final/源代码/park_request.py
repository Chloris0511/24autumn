import requests
import json
import pandas as pd

# 定义接口 URL 和请求头
url = "https://data.sh.gov.cn/interface/1407/6692"  # 更新为实际的接口 URL
headers = {
    "Content-Type": "application/json",
    "Cache-Control": "no-cache",
    "token": "667f3db85cfcdcff0929b70b923286fd"  # 替换为有效的 token
}

# 构造请求体
payload = {
    "data_year": "2023",  # 替换为实际的年份
    "limit": 2000,  # 可选，查询数量，默认 20
    "offset": 0  # 可选，查询起始位置，默认 0
}

try:
    # 发送 POST 请求
    response = requests.post(url, headers=headers, json=payload)

    # 检查响应状态码
    if response.status_code == 200:
        # 解析返回的 JSON 数据
        response_data = response.json()

        # 检查是否成功
        if response_data.get("code") == "000000":
            print("接口调用成功，正在处理数据...")

            # 提取实际的 'data' 字段，并解析为 Python 对象
            data = json.loads(response_data.get("data"))

            # 提取公园信息
            parks_data = data.get("data", [])

            # 将提取的数据转换为 DataFrame
            df = pd.DataFrame(parks_data)

            # 保存为 CSV 文件
            df.to_csv('park_data.csv', index=False, encoding='utf-8')

            # 输出 DataFrame 查看结果
            print("数据已成功保存为 CSV 文件：park_data.csv")
            print(df)
        else:
            print(f"接口调用失败，错误信息：{response_data.get('message')}")
    else:
        print(f"请求失败，HTTP 状态码：{response.status_code}")
        print("返回内容：")
        print(response.text)

except Exception as e:
    print(f"发生错误：{e}")
