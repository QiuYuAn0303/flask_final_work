# Python期末项目——探究影响各地个体就业数量的因素及其相关关系

## Github仓库、pythonanywhere项目部署
- [pythonanywhere](https://sandman999.pythonanywhere.com)
- [Github](https://github.com/QiuYuAn0303/flask_final_work/tree/master)

## 项目页面说明
#### 本项目一共有6个页面，URL如下:
- [首页(研究内容简述)](https://sandman999.pythonanywhere.com/home)
- [各省个体就业数量(地图)](https://sandman999.pythonanywhere.com/map)
- [各省的个体就业数量与高校毕业生数量(折线图)](https://sandman999.pythonanywhere.com/line)
- [各省城镇失业率情况(条形图)](https://sandman999.pythonanywhere.com/bar)
- [各省个体就业情况与各省城镇化情况(复合图)](https://sandman999.pythonanywhere.com/jielun2)
- [总结](https://sandman999.pythonanywhere.com/end)

## HTML档描述:
- 为整体页面布局增加了css层叠样式表，使界面看起来更加舒适。
- home,bar,map,line,render,end.html文件分别为6个不同url的内容。
- 每个页面都有下拉菜单方便用户跳转到其他也米娜，其中map,bar,line,render.html含有交互式数据图案以及数据表格。

## python档
- 主要采用flask进行制作。
- 引用pyecharts进行图标展示。
- 实现了数据的传输与交互。

## web动作描述
- 提供下拉菜单方便用户查看不同页面展示的数据。
- 用户可以与图标进行互动，方便用户找到想要查看的内容.
