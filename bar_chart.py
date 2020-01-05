from pyecharts.charts import Bar
from pyecharts import options as opts

def bar_base() -> Bar:
  c = (
      Bar()
          .add_xaxis(
          ['北京', '天津', '河北', '山西', '内蒙古', '辽宁', '吉林', '黑龙江', '上海', '江苏', '浙江', '安徽', '福建', '江西', '山东', '河南', '湖北', '湖南',
           '广东', '广西', '海南', '重庆', '四川', '贵州', '云南', '西藏', '陕西', '甘肃', '青海', '宁夏', '新疆'])
          .add_yaxis("城镇失业率",
                     [7.91, 25.81, 38.04, 24.56, 27.04, 44.41, 26.82, 39.41, 19.41, 34.37, 34.07, 28.07, 17.33, 35.11,
                      46.54, 48.6, 36.14, 40.35, 36.55, 16.71, 5.51, 13.09, 53.31, 15.06, 20.88, 2.11, 24.12, 9.95,
                      4.65, 5.39, 9.55],color='green')
      .set_global_opts(title_opts=opts.TitleOpts(title="各省城镇失业率情况"),
                       datazoom_opts=opts.DataZoomOpts(type_="inside"),)
  )
  return c
c = bar_base()

c.render('barchart.html')