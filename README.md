|Document owner|黄煜惠|
|---|:---:|
|Document status|正在完善中|
|Wechat|HUANGYUHUIYUHUI|

<div align="center">
    <h1>:bulb: 世界抑郁症患病情况及其相关因素的分析 :bulb:</h1>
    <a href='http://huangyuhui.pythonanywhere.com/'>点击查看pythonanywhere链接</a>
</div>

### :envelope:项目背景
当今世界，抑郁症已成为一种常见的心理疾病，原因主要归结于个人属性、社会与经济状况、环境因素。现代社会复杂、发展快、竞争大，人们或多或少会因为家庭、事业、人际交往等方面的原因产生焦虑、抑郁的情绪，当这些情绪积聚到一定程度而无法自我排解时，人们就很容易患上抑郁症。

**何为抑郁症？**
> 抑郁症又称抑郁障碍，以显著而持久的心境低落为主要临床特征，是心境障碍的主要类型。临床可见心境低落与其处境不相称，情绪的消沉可以从闷闷不乐到悲痛欲绝，自卑抑郁，甚至悲观厌世，可有自杀企图或行为；甚至发生木僵；部分病例有明显的焦虑和运动性激越；严重者可出现幻觉、妄想等精神病性症状。

- 参考文献：[《健康时报网抑郁症报道研究（2008-2018）》](https://kns.cnki.net/KCMS/detail/detail.aspx?dbcode=CMFD&dbname=CMFD201902&filename=1019870403.nh&uid=WEEvREcwSlJHSldRa1FhdXNzY2Z1OVRyNFBoREhOSGdYME1hd2pDUHlZbz0=$9A4hF_YAuvQ5obgVAqNKPCYcEjKensW4IQMovwHtwkF4VYPoHbKxJw!!&v=MDIxMThSOGVYMUx1eFlTN0RoMVQzcVRyV00xRnJDVVI3cWZadVpwRnl6aFViN0JWRjI2Rjd1L0h0WE1ySkViUEk=)
- 参考文献：[《抑郁症被低估是世界问题》](https://kns.cnki.net/KCMS/detail/detail.aspx?dbcode=CCND&dbname=CCNDLAST2014&filename=JKSB201408280071&uid=WEEvREcwSlJHSldRa1FhdXNzY2Z1OVRyNFBoREhOSGdYME1hd2pDUHlZbz0=$9A4hF_YAuvQ5obgVAqNKPCYcEjKensW4IQMovwHtwkF4VYPoHbKxJw!!&v=MTY3MzBkaG5qOThUbmpxcXhkRWVNT1VLcmlmWmVadkZ5bmlVN3ZNSkY0UUx5YlliTEc0SDlYTXA0MU5aT3NJRFJOS3Vo)

### :clipboard:核心价值与目标
通过收集和清洗世界抑郁症的相关数据，实现具有交互功能的图表，从中了解世界抑郁症患病的情况及有可能影响抑郁症的相关因素，得出一个数据故事，提出有价值的观点，并希望以此引起人们对抑郁症的重视。

### :pencil:设想的因素
- 就业（失业）压力
- 经济情况
- 性别
- 妇女生育

[（点击下载数据）](https://github.com/uweier/interactive_data_visualization/tree/master/data)

## :eyes:数据清洗与数据来源
- [数据世界](https://ourworldindata.org/)
- [世界银行](https://data.worldbank.org.cn/)

## :speech_balloon:交互式图
可跳转至:point_right:[pythonanywhere](http://huangyuhui.pythonanywhere.com/)上查看:white_check_mark:

**世界抑郁症整体情况**

:one:由【世界抑郁症总人数】图中可以得知，抑郁症患病人数在近十年内变化不大，部分国家的抑郁症患病人数在逐年上升。而抑郁症患者人数较多的国家多分布在北美洲、亚洲、大洋洲和南美洲。
![世界抑郁症总人数情况](https://github.com/uweier/interactive_data_visualization/blob/master/iv_image/total_number.png)

:two:由【世界抑郁症患病率】图中可以得知，抑郁症患病率在近十年内变化不大，部分国家抑郁症患病率在逐年下降，抑郁症患病人数较少的格陵兰却是患病率较高的国家之一，而中国、俄罗斯、巴西等国家的情况与之相反。
![世界抑郁症患病率情况](https://github.com/uweier/interactive_data_visualization/blob/master/iv_image/hbl_map.png)

:three:由【世界男性、女性患病人数对比】图中可以得知，世界女性抑郁症患者多于男性。

女性在产前、产后容易患抑郁症，加上现代女性的身上承担着越来越多的事情，压力也由此增大。
![世界抑郁症男女人数对比](https://github.com/uweier/interactive_data_visualization/blob/master/iv_image/man_woman_number.png)

**既然女性患抑郁症的人数较多，那么女性患抑郁症是否与生育数量存在关系？**

:four:下图为世界每位妇女所生育的孩子的数量情况。

由图中可以得知，近十年在世界整体上，每位妇女所生育的孩子数量向着减少的趋势发展。相比于其他地区，非洲每位妇女所生育的孩子数量较多。

也就是说，随着时代的发展，大多数人的生育观发生了变化，而劳动力已不再是一个国家最重要的力量，大多数妇女还是选择少生或不生孩子。

Uganda的抑郁症患病率较高，其妇女的生育数量也较多；Chad、Ethiopia、Angola、Nigeria等非洲国家的抑郁症患病率也较高，同时其妇女的生育数量也较多。因此，女性抑郁症患病率与妇女生育数量存在一定的关系。
![世界每名妇女生育数情况](https://github.com/uweier/interactive_data_visualization/blob/master/iv_image/give_birth.png)

**那么经济状况是否也与抑郁症存在关系？**

:five:由【世界人均GDP】图中可以得知，北美国家，如美国、加拿大、格陵兰，澳大利亚，还有部分欧洲国家的人均GDP较高。

美国、加拿大、格陵兰、澳大利亚恰好也是抑郁症患病率较高的国家。

将【世界抑郁症患病率】地图与【世界人均GDP】地图进行对比，发现两者的情况较为相似，抑郁症患病率较高的国家，人均GDP恰好也较高。

所以，抑郁症患病率在很大程度上与国家经济发展情况有一定的关系。
![世界人均GDP情况](https://github.com/uweier/interactive_data_visualization/blob/master/iv_image/gdp.png)

**失业率或许与患病率有相关性？**

:six:图一为世界抑郁症患病率前十的国家近十年的患病率趋势。图二为世界抑郁症患病率前十的国家近十年的失业率趋势。

以这十个国家为例，可以看得出抑郁症患病率变化不大，而失业率的变化也不大，所以暂时也难以判断两者是否存在相关性。
![患病率](https://github.com/uweier/interactive_data_visualization/blob/master/iv_image/hbl_line.png)
![失业率](https://github.com/uweier/interactive_data_visualization/blob/master/iv_image/unemployment.png)


## :books:数据故事与观点
由以上的分析可初步得出抑郁症患病与妇女生育情况、国家经济发展有关，且女性患病人数比男性多。

女性在怀孕时，身体会分泌一些化学因子，因此在生育前后心理和生理上都会存在一些变化，加上女性情感较细腻，所以更容易患上抑郁症。

而国家发展越快，经济状况越好，各方面的竞争会随之变大，压力也会随之变大，抑郁症也随之而来。

针对抑郁症，可以从以下方面做出一些改变：
- 在政策上，国家可为孕妇提供免费的心理辅导
- 在宣传上，相关组织可以实施以下措施：
    - 通过建立社群、交流平台，组织相关活动，帮助抑郁症患者解决当前存在的一些心理问题
    - 举办心理讲座，讲解何为抑郁症、抑郁症发病特征，患上抑郁症应该怎么做等
    - 组织抑郁症康复者帮助正患有抑郁症的人
    - 开放免费的负能量宣泄场所

抑郁症其实不可怕，可怕的是你无法正视它，战胜它。在健康面前，万事皆小，无论身边有多少不良因素，也要随时保持良好心情，争取健康的身心。

### :date:项目计划进程
1. 选定项目，搜集数据，PRD写作
2. 数据清洗，作表，画图
3. 前后端数据传递，描述过程
4. CSS样式
5. 整体完善
6. 上传pythonanywhere

### :raising_hand:所需合作人员
- 对作业上心、认真、尽力完成（不划水）
- 不怕困难，愿意一起加油，一起除bug
- 对Flask框架熟悉，熟悉html、css
- 有基本python能力，能完成前后端交互的代码、数据传递等
- 必要时敢于向他人求助

### :dancers:项目人员
黄煜惠  丁晓莹
