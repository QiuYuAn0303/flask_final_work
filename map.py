from pyecharts.charts import Map
from pyecharts import options as opts
locate = ['北京', '天津', '河北', '山西', '内蒙古', '辽宁', '吉林', '黑龙江', '上海', '江苏', '浙江', '安徽', '福建', '江西', '山东', '河南', '湖北', '湖南', '广东', '广西', '海南', '重庆', '四川', '贵州', '云南', '西藏', '陕西', '甘肃', '青海', '宁夏', '新疆']
个体就业数 = [40.22, 106.54, 410.63, 261.16, 226.83, 296.69, 242.76, 346.92, 42.72, 834.82, 590.56, 635.59, 758.26, 311.18, 467.0, 691.9, 584.32, 324.04, 991.44, 304.27, 73.67, 267.98, 340.09, 175.77, 220.3, 44.17, 417.87, 114.87, 65.09, 57.09, 195.52]



list = [[locate[i],个体就业数[i]] for i in range(len(locate))]

map_1 = Map()

map_1.set_global_opts(
    title_opts=opts.TitleOpts(title="各省个体就业数量"),
    visualmap_opts=opts.VisualMapOpts(max_=1000)  #最大数据范围
    )
map_1.add("个体就业数", list, maptype="china")
map_1.render('map.html')
