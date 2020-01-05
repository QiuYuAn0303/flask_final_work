from flask import Flask, render_template, request, escape

app = Flask(__name__, static_folder="templates")


@app.route("/")
@app.route("/home")
def entry_page() -> 'html':
  return render_template('home.html',
                         the_title='选择查看影响各地个体就业数量的因素及其相关关系')
@app.route("/bar")
def bar1() -> 'html':
  return render_template('bar_chart.html',
                    the_title='各省城镇失业率情况')

@app.route("/line")
def line() -> 'html':
  return  render_template('line.html',
                          the_title='各省个体就业人数与高校毕业人数对比')

@app.route("/map")
def map_1() -> 'html':
  return render_template('map.html',
                    the_title='各省个体就业数量')



@app.route("/jielun2")
def jielun() -> 'html':
  return  render_template('render.html',
                          the_title='各省个体就业数与各省第二、三产业加值情况')

@app.route("/end")
def end() -> 'html':
    return render_template('1.html',
                           the_title='总结')

if __name__ == "__main__":
  app.run()