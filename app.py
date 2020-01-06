#!/usr/bin/env python
# coding: utf-8

# In[6]:


from pyecharts import options as opts
from pyecharts.globals import ChartType, SymbolType
from pyecharts.charts import Bar,Tab,Line,Map,Timeline,Scatter,Grid,Page
from pyecharts.components import Table
import pandas as pd

# import cufflinks as cf
# import plotly as py
# import plotly.graph_objs as go

# 总表
df_z = pd.read_csv('/home/huangyuhui/mysite/data/number-with-depression-by-country.csv', dtype=str, encoding = 'gbk')

# 总人数
df_zrs = pd.read_csv('/home/huangyuhui/mysite/data/number-with-depression-by-country-zrs.csv', keep_default_na=False, na_values='na_rep', dtype=str)
# 患病率
df_hbl = pd.read_csv('/home/huangyuhui/mysite/data/number-with-depression-by-country-hbl.csv', keep_default_na=False, na_values='na_rep')
# 男性患病人数
df_man = pd.read_csv('/home/huangyuhui/mysite/data/number-with-depression-by-country-man.csv', keep_default_na=False, na_values='na_rep')
# 女性患病人数
df_woman = pd.read_csv('/home/huangyuhui/mysite/data/number-with-depression-by-country-woman.csv', keep_default_na=False, na_values='na_rep')
# 学历与就业状况
df = pd.read_csv('/home/huangyuhui/mysite/data/depression-by-level-of-education-employment-z.csv', encoding='utf-8')

# 每个妇女生育孩子数
df_fn = pd.read_csv('/home/huangyuhui/mysite/data/children-per-woman-new.csv')

# 国家人均GDP
df_gdp = pd.read_csv('/home/huangyuhui/mysite/data/world_gdp.csv')

# 失业率
df1 = pd.read_csv('/home/huangyuhui/mysite/data/Unemployment_new_test.csv',encoding = 'utf-8')
df2 = df1.set_index('region')

df0 = df_hbl.set_index('region')

# cf.set_config_file(offline=True, theme="polar")
# py.offline.init_notebook_mode()

# 1总人数轮播图pyecharts
def timeline_map_zrs():
    tl = Timeline()
    for i in range(2008, 2018):
        map0 = (
            Map()
            .add(
                "世界抑郁症总人数", list(zip(list(df_zrs.region.unique()),list(df_zrs["{}".format(i)]))), "world", is_map_symbol_show = False
            )
            .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
            .set_global_opts(
                title_opts=opts.TitleOpts(title="{}年世界抑郁症总人数".format(i)),
                visualmap_opts=opts.VisualMapOpts(min_= 0,
                                                  max_= df_zrs["2017"].max(),
                                                  series_index=0),
            )
        )

        tl.add(map0,"{}年".format(i))
    return tl

Timeline_map_zrs = timeline_map_zrs()
Timeline_map_zrs.render('世界抑郁症总人数.html')# 输出 世界抑郁症总人数.html

# 2患病率轮播图pyecharts
def timeline_map_hbl():
    tl = Timeline()
    for i in range(2008, 2018):
        map0 = (
            Map()
            .add(
                "世界抑郁症患病率", list(zip(list(df_hbl.region.unique()),list(df_hbl["{}".format(i)]))), "world",is_map_symbol_show = False
            )
            .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
            .set_global_opts(
                title_opts=opts.TitleOpts(title="{}年世界抑郁症患病率".format(i)),
                visualmap_opts=opts.VisualMapOpts(
                    min_= df_hbl["2016"].min(),
                    max_=df_hbl["2008"].max(),
                    series_index=0,
                    is_piecewise=True),
            )
        )

        tl.add(map0,"{}年".format(i))
    return tl

Timeline_map_hbl = timeline_map_hbl()
Timeline_map_hbl.render('世界抑郁症患病率.html')# 输出 世界抑郁症患病率.html

# 3男性和女性抑郁症人数对比轮播条形图pyecharts
def timeline_bar():
    x = list(df_man.region)
    tl = Timeline()
    for i in range(2008, 2018):
        bar = (
            Bar()
            .add_xaxis(x)
            .add_yaxis("女性患病人数", list(df_woman["{}".format(i)]))
            .add_yaxis("男性患病人数", list(df_man["{}".format(i)]))
            .reversal_axis()
            .set_global_opts(title_opts=opts.TitleOpts("{}年世界男性和女性抑郁症人数对比".format(i)),
                            datazoom_opts=opts.DataZoomOpts(orient="vertical",range_start="50",range_end="60"))
            .set_series_opts(
            label_opts=opts.LabelOpts(is_show=False),
        )
        )
        tl.add(bar, "{}年".format(i))
    return tl

Timeline_bar = timeline_bar()
Timeline_bar.render('男性和女性抑郁症人数对比.html')# 输出 男性和女性抑郁症人数对比.html

# 推导式 处理x轴
x_z = [int(x) for x in df0.columns.values[1:]]
x_z_zx = [str(x) for x in x_z]
# 4患病率与失业率对比图折线图pyecharts
def line_base1():
    c = (
        Line()
        .add_xaxis(x_z_zx)
        .add_yaxis("Morocco", list(df0.loc["Morocco"].values)[1:])
        .add_yaxis("Lesotho", list(df0.loc["Lesotho"].values)[1:])
        .add_yaxis("Uganda", list(df0.loc["Uganda"].values)[1:])
        .add_yaxis("Finland", list(df0.loc["Finland"].values)[1:11])
        .add_yaxis("Australia", list(df0.loc["Australia"].values)[1:])
        .add_yaxis("United States", list(df0.loc["United States"].values)[1:])
        .add_yaxis("Pakistan", list(df0.loc["Pakistan"].values)[1:])
        .add_yaxis("Portugal", list(df0.loc["Portugal"].values)[1:])
        .add_yaxis("Sweden", list(df0.loc["Sweden"].values)[1:])
        .add_yaxis("Ireland", list(df0.loc["Ireland"].values)[1:])
        .set_global_opts(title_opts=opts.TitleOpts(title="抑郁症患病率", subtitle="世界抑郁症患病率前十国家"),
                        legend_opts=opts.LegendOpts(pos_left="30%"))
        .set_series_opts(
            label_opts=opts.LabelOpts(is_show=False),
        )
    )
    return c

def line_base2():
    c = (
        Line()
        .add_xaxis(x_z_zx)
        .add_yaxis("Morocco", list(df2.loc["Morocco"].values)[1:])
        .add_yaxis("Lesotho", list(df2.loc["Lesotho"].values)[1:])
        .add_yaxis("Uganda", list(df2.loc["Uganda"].values)[1:])
        .add_yaxis("Finland", list(df2.loc["Finland"].values)[1:11])
        .add_yaxis("Australia", list(df2.loc["Australia"].values)[1:])
        .add_yaxis("United States", list(df2.loc["United States"].values)[1:])
        .add_yaxis("Pakistan", list(df2.loc["Pakistan"].values)[1:])
        .add_yaxis("Portugal", list(df2.loc["Portugal"].values)[1:])
        .add_yaxis("Sweden", list(df2.loc["Sweden"].values)[1:])
        .add_yaxis("Ireland", list(df2.loc["Ireland"].values)[1:])
        .set_global_opts(title_opts=opts.TitleOpts(title="失业率", subtitle="世界各国失业率前十"),
                        legend_opts=opts.LegendOpts(pos_left="30%"))
        .set_series_opts(
            label_opts=opts.LabelOpts(is_show=False),
        )
    )
    return c


page = Page()
page.add(line_base1(), line_base2())
page.render('患病率与失业率对比图.html')# 输出 患病率与失业率对比图.html

# 5每个妇女生育孩子数地图pyecharts
def timeline_map_fn():
    tl = Timeline()
    for i in range(2006, 2016):
        map0 = (
            Map()
            .add(
                "世界每个妇女生育孩子数", list(zip(list(df_fn.region.unique()),list(df_fn["{}".format(i)]))), "world",is_map_symbol_show = False
            )
            .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
            .set_global_opts(
                title_opts=opts.TitleOpts(title="{}年世界每个妇女生育孩子数".format(i)),
                visualmap_opts=opts.VisualMapOpts(min_= 0,
                                                  max_= 8,
                                                  series_index=0),
            )
        )

        tl.add(map0,"{}年".format(i))
    return tl

Timeline_map_fn = timeline_map_fn()
Timeline_map_fn.render('每个妇女生育孩子数.html')

# 6国家人均GDP地图pyecharts
def timeline_map_gdp():
    tl = Timeline()
    for i in range(2008, 2018):
        map0 = (
            Map()
            .add(
                "世界人均GDP", list(zip(list(df_gdp.region.unique()),list(df_gdp["{}".format(i)]))), "world",is_map_symbol_show = False
            )
            .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
            .set_global_opts(
                title_opts=opts.TitleOpts(title="{}年世界人均GDP".format(i)),
                visualmap_opts=opts.VisualMapOpts(min_= 0,
                                                  max_= df_gdp["2017"].max(),
                                                  series_index=0),
            )
        )

        tl.add(map0,"{}年".format(i))
    return tl

Timeline_map_gdp = timeline_map_gdp()
Timeline_map_gdp.render('世界国家人均GDP.html')


def log_request(req:'flask_request',res:str):
    with open('vsearch.log','a') as log:
        print(req.form, req.remote_addr, req.user_agent, res,file=log,sep='|')
        # print(str(dir(req)),res,file=log)



# 开始Flask框架处理
from flask import Flask, render_template, request, escape

app = Flask(__name__)

# 总表的下拉菜单 按年份（未定）
# regions_available_loaded_0 = list(df_z.年份.unique())

#首页
@app.route('/')
@app.route('/entry',methods=['GET'])
def index():
    # 将总表以数据框形式列出
    data_str = df_z.to_html()

    title = '世界抑郁症情况及其相关因素研究'
    return render_template('entry.html',
                           the_title = title,
                           the_res = data_str,
                          )

# 世界总人数地图页
@app.route('/world_number',methods=['POST'])
def yi_yu_select_1():
    with open("世界抑郁症总人数.html", encoding="utf8", mode="r") as f1:
        plot_all_1 = "".join(f1.readlines())
    the_region = request.form["the_region_selected_1"]
    print(the_region)
    title = '世界抑郁症情况及其相关因素研究'

    # contents_0 = []
    # with open('data/number-with-depression-by-country.csv', encoding='gbk') as data01:
    #     ignore = data01.readline()
    #     countries_0 = {}
    #     for line in data01:
    #         contents_0.append([])
    #         for item_0 in line.strip().split(','):
    #             contents_0[-1].append(item_0)
    # titles_0 = ('地区','年份', '总人数', '患病率', '男性患病人数', '女性患病人数')
    return render_template('world_number.html',
                            the_plot_all_1 = plot_all_1,
                            the_title = title,
                            # the_row_titles=titles_0,
                            # the_data=contents_0,
                            )

# @app.route('/search_0', methods=['POST'])
# def do_search_0():
#     search = request.form['place_0']
# #     with open('data/number-with-depression-by-country.csv', encoding='gbk') as data02:
# #         # ignore = data02.readline()
# #         countries = {}
# #         for line in data02:
# #             k, v, d, e, r, t = line.strip().split(',')
# #             countries[k] = k, v, d, e, r, t

# # #     if search in countries.keys():
# # #         contents = [countries[search]]
# # #     else:
# # #         contents = ['您搜索的结果不存在！！']

# #     contents = [countries[search] if search in countries.keys() else '您搜索的结果不存在！！']

#     # log_request(request, contents)
#     # titles = ('地区','年份', '总人数', '患病率', '男性患病人数', '女性患病人数')
#     return render_template('world_number_result.html',
#                           the_title='搜索结果',
#                         #   the_row_titles=titles,
#                         #   the_data=contents,
#                           )


@app.route('/world_hbl',methods=['POST'])
def yi_yu_select_2():
    with open("世界抑郁症患病率.html", encoding="utf8", mode="r") as f2:
        plot_all_2 = "".join(f2.readlines())
    the_region = request.form["the_region_selected_2"]
    print(the_region)
    title = '世界抑郁症情况及其相关因素研究'
    contents = []
    with open('/home/huangyuhui/mysite/data/number-with-depression-by-country-hbl.csv', encoding='utf-8') as data1:
        ignore = data1.readline()
        countries = {}

        for line in data1:
            contents.append([])
            for item in line.strip().split(','):
                contents[-1].append(item)

    titles = ('地区', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017')
    return render_template('world_hbl.html',
                            the_plot_all_2 = plot_all_2,
                            the_title = title,
                            the_row_titles=titles,
                            the_data=contents,
                            )


@app.route('/search', methods=['POST'])
def do_search_1():
    search = request.form['place']
    with open('/home/huangyuhui/mysite/data/number-with-depression-by-country-hbl.csv', encoding='utf-8') as data2:
        ignore = data2.readline()
        countries = {}
        for line in data2:
            k, v, d, e, r, t, y, b, f, c, n = line.strip().split(',')
            countries[k] = k, v, d, e, r, t, y, b, f, c, n

    if search in countries.keys():
        contents = [countries[search]]
    else:
        contents = ['您搜索的结果不存在！！']

    # contents = [countries[search] if search in countries.keys() else '您搜索的结果不存在！！']

    log_request(request, contents)
    titles = ('地区', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017')
    return render_template('world_hbl_result.html',
                          the_title='搜索结果',
                          the_row_titles=titles,
                          the_data=contents,
                          )


@app.route('/world_man_woman',methods=['POST'])
def yi_yu_select_3():
    with open("男性和女性抑郁症人数对比.html", encoding="utf8", mode="r") as f3:
        plot_all_3 = "".join(f3.readlines())
    the_region = request.form["the_region_selected_3"]
    print(the_region)
    title = '世界抑郁症情况及其相关因素研究'
    return render_template('world_man_woman.html',
                            the_plot_all_3 = plot_all_3,
                            the_title = title,)

@app.route('/world_unemployment',methods=['POST'])
def yi_yu_select_4():
    with open("患病率与失业率对比图.html", encoding="utf8", mode="r") as f4:
        plot_all_4 = "".join(f4.readlines())
    the_region = request.form["the_region_selected_4"]
    print(the_region)
    title = '世界抑郁症情况及其相关因素研究'
    return render_template('world_unemployment.html',
                            the_plot_all_4 = plot_all_4,
                            the_title = title,)

# regions_available_loaded = list(df.region.unique())
# # plotly画图
# @app.route('/world_education',methods=['POST'])
# def yi_yu_select_5():
#     fig = df.set_index('region').T.iplot(kind="bar",  xTitle="地区/受教育程度类别",yTitle="抑郁症患病率", title="受教育程度和就业状况影响的抑郁症的情况", asFigure=True)
#     py.offline.plot(fig, filename="学历就业1.html",auto_open=False)
#     with open("学历就业1.html", encoding="utf8", mode="r") as f5:
#         plot_all_5 = "".join(f5.readlines())
#     the_region = request.form["the_region_selected_5"]
#     print(the_region)

#     data_str5 = df.to_html()

#     regions_available = regions_available_loaded
#     title = '世界抑郁症情况及其相关因素研究'
#     return render_template('world_education.html',
#                           the_plot_all_5 = plot_all_5,
#                           the_title = title,
#                           the_res_5 = data_str5,
#                           the_select_region = regions_available)



# @app.route('/world_education_result',methods=['POST'])
# def yi_yu_select_6():
#     the_region = request.form["the_region_selected_6"]
#     print(the_region)

#     dfs = df.query("region in ['{}']".format(the_region))

#     data_str6 = dfs.to_html()

#     fig = dfs.set_index('region').T.iplot(kind="bar",  xTitle="受教育程度类别",yTitle="抑郁症患病率", title="受教育程度和就业状况影响的抑郁症的情况", asFigure=True)
#     py.offline.plot(fig, filename="学历就业结果.html",auto_open=False)
#     with open("学历就业结果.html", encoding="utf8", mode="r") as f6:
#         plot_all_6 = "".join(f6.readlines())

#     title = '世界抑郁症情况及其相关因素研究'
#     return render_template('world_education_result.html',
#                             the_plot_all_6 = plot_all_6,
#                             the_title = title,
#                             the_res_6 = data_str6,)

@app.route('/world_give_birth',methods=['POST'])
def yi_yu_select_7():
    with open("每个妇女生育孩子数.html", encoding="utf8", mode="r") as f7:
        plot_all_7 = "".join(f7.readlines())
    the_region = request.form["the_region_selected_7"]
    print(the_region)
    title = '世界抑郁症情况及其相关因素研究'
    return render_template('world_give_birth.html',
                            the_plot_all_7 = plot_all_7,
                            the_title = title,)

@app.route('/world_gdp',methods=['POST'])
def yi_yu_select_8():
    with open("世界国家人均GDP.html", encoding="utf8", mode="r") as f8:
        plot_all_8 = "".join(f8.readlines())
    the_region = request.form["the_region_selected_8"]
    print(the_region)
    title = '世界抑郁症情况及其相关因素研究'
    return render_template('world_gdp.html',
                            the_plot_all_8 = plot_all_8,
                            the_title = title,)

@app.route('/summary',methods=['POST'])
def yi_yu_select_9():
    the_region = request.form["the_region_selected_9"]
    print(the_region)
    title = '世界抑郁症情况及其相关因素研究'
    return render_template('summary.html',
                            the_title = title,)


@app.route('/viewlog')
def view_the_log() -> 'html':
    contents=[]
    with open('vsearch.log') as log:
        for line in log:
            contents.append([])
            for item in line.split('|'):
                contents[-1].append(escape(item))
    titles = ('Form Data', 'Remote_addr', 'User_agent', 'Results')
    return render_template('viewlog.html',
                          the_title = 'View Log',
                          the_row_titles = titles,
                          the_data = contents,)




if __name__ == '__main__':
    app.run(port = 8004)   # debug=True, 在py使用, 在ipynb不使用


# In[ ]:





# In[ ]:




