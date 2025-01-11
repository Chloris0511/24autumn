import folium
from folium.plugins import HeatMap
import pandas as pd

# 加载数据
file_path = "C:/Users/Chlor/OneDrive/桌面/工程导论期末大作业/Shanghai_Park.xlsx"
df = pd.read_excel(file_path, sheet_name='www.geocoding.tech')

# 提取经纬度和公园名称
locations = df[['纬度WGS84', '经度WGS84', 'park_name']].dropna()

# 创建上海市地图（以平均经纬度为中心）
shanghai_map = folium.Map(location=[31.23, 121.47], zoom_start=10)

# 标注公园位置
for _, row in locations.iterrows():
    folium.Marker(
        location=[row['纬度WGS84'], row['经度WGS84']],
        popup=row['park_name'],
    ).add_to(shanghai_map)

# 保存公园位置图
shanghai_map.save('Shanghai_Park_Locations.html')

# 生成热力图
heatmap_map = folium.Map(location=[31.23, 121.47], zoom_start=10)
heat_data = locations[['纬度WGS84', '经度WGS84']].values.tolist()
HeatMap(heat_data).add_to(heatmap_map)

# 保存热力图
heatmap_map.save('Shanghai_Park_Heatmap.html')