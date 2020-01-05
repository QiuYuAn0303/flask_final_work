from pyecharts.faker import Faker
from pyecharts import options as opts
from pyecharts.charts import Bar, Tab, Pie, Line
from pyecharts.components import Table


def bar_datazoom_slider() -> Bar:
    c = (
        Bar()
        .add_xaxis(['北京', '天津', '河北', '山西', '内蒙古', '辽宁', '吉林', '黑龙江', '上海', '江苏', '浙江', '安徽', '福建', '江西', '山东', '河南', '湖北', '湖南', '广东', '广西', '海南', '重庆', '四川', '贵州', '云南', '西藏', '陕西', '甘肃', '青海', '宁夏', '新疆'])
        .add_yaxis("个体就业数", Faker.days_values)
        .set_global_opts(
            title_opts=opts.TitleOpts(title="各省个体就业数"),
            datazoom_opts=[opts.DataZoomOpts()],
        )
    )
    return c


def line_markpoint() -> Line:
    c = (
        Line()
        .add_xaxis(['北京', '天津', '河北', '山西', '内蒙古', '辽宁', '吉林', '黑龙江', '上海', '江苏', '浙江', '安徽', '福建', '江西', '山东', '河南', '湖北', '湖南', '广东', '广西', '海南', '重庆', '四川', '贵州', '云南', '西藏', '陕西', '甘肃', '青海', '宁夏', '新疆'])
        .add_yaxis(
            "第二产业",
            [5647.65, 7609.81, 16040.06, 7089.19, 6807.3, 10025.1, 6410.85, 4030.94, 9732.54, 41248.52, 23505.88, 13842.09, 17232.36, 10250.21, 33641.72, 22034.83, 17088.95, 14453.54, 40695.15, 8072.94, 1095.79, 8328.79, 15322.72, 5755.54, 6957.44, 628.37, 12157.48, 2794.67, 1247.06, 1650.26, 4922.97],
            markpoint_opts=opts.MarkPointOpts(data=[opts.MarkPointItem(type_="min")]),
        )
        .add_yaxis(
            "第三产业",
            [24553.64, 11027.12, 16632.21, 8988.28, 8728.1, 13256.95, 7503.02, 9329.72, 22842.96, 47205.16, 30724.26, 13526.72, 16191.86, 9857.24, 37877.43, 21731.65, 18730.09, 18888.65, 52751.18, 9260.2, 2736.15, 10656.13, 20928.75, 6891.37, 8424.82, 719.01, 10450.65, 4530.1, 1350.07, 1775.07, 5584.02],
            markpoint_opts=opts.MarkPointOpts(data=[opts.MarkPointItem(type_="max")]),
        )
        .set_global_opts(title_opts=opts.TitleOpts(title="各省第二、三产业加值情况"))
    )
    return c

tab = Tab()
tab.add(bar_datazoom_slider(), "各省个体就业数")
tab.add(line_markpoint(), "各省第二、三产业加值情况")

tab.render('render.html')





