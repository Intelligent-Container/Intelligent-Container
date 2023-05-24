    // 基于准备好的dom，初始化echarts实例
    var myChartWd = echarts.init(document.getElementById('mainWd'));
    var myChartSd = echarts.init(document.getElementById('mainSd'));
    var myChartYw = echarts.init(document.getElementById('mainYw'));
    var myChartZt = echarts.init(document.getElementById('mainZt'));
    var myChartWsd = echarts.init(document.getElementById('mainWsd'));

    //使用刚指定的配置项和数据显示图表。
    myChartWd.setOption(optionWd);
    myChartSd.setOption(optionSd);
    myChartYw.setOption(optionYw);
    myChartZt.setOption(optionZt);
    myChartWsd.setOption(optionWsd);