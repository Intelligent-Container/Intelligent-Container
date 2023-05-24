var xData = function() {
    var data = [];
    for (var i = 1; i < 25; i++) {
        data.push(i + "时");
    }
    return data;
}();

optionWsd = {
    backgroundColor: "#5d3131",

    tooltip: {
        trigger: "axis",
        axisPointer: {
            type: "shadow",
            textStyle: {
                color: "#fff"
            }

        },
    },
    grid: {
        borderWidth: 0,
        top: 110,
        bottom: 95,
        textStyle: {
            color: "#fff"
        }
    },
    legend: {
        x: '46%',
        top: '11%',
        textStyle: {
            color: '#90979c',
        },
        data: ['温度', '湿度']
    },


    calculable: true,
    xAxis: [{
        type: "category",
        axisLine: {
            lineStyle: {
                color: "rgba(204,187,225,0.5)",
            }
        },
        splitLine: {
            show: false
        },
        axisTick: {
            show: false
        },
        data: xData,
    }],

    yAxis: [{
        type: "value",
        splitLine: {
            show: false
        },
        axisLine: {
            show:true,
            lineStyle: {
                color: "rgba(204,187,225,0.5)",
            }
        },

    }],
    dataZoom: [{
        type:'slider',
            show:false,
            realtime:true,
            startValue:0,
            endValue:24
    }],
    series: [{
        name: "湿度",
        type: "line",
        symbolSize: 10,
        symbol: 'circle',
        itemStyle: {
            color: "#428675",
        },
        markPoint: {
            label: {
                normal: {
                    textStyle: {
                        color: '#fff'
                    }
                }
            },
            data: [{
                type: 'max',
                name: '最大值',

            }, {
                type: 'min',
                name: '最小值'
            }]
        },
        data: [
            59, 91, 25, 20, 19, 33, 34, 35,78, 29, 17,20,15,10,79,
            73,94,25,28,72,36,93,22,10,39,25,10,19,24,20
        ],
    }, {
        name: "温度",
        type: "line",
        symbolSize: 10,
        symbol: 'circle',
        itemStyle: {
            color: "#3170a7",
        },
        markPoint: {
            label: {
                normal: {
                    textStyle: {
                        color: '#fff'
                    }
                }
            },
            data: [{
                type: 'max',
                name: '最大值',

            }, {
                type: 'min',
                name: '最小值'
            }]
        },
        data: [
            26,33,22,30,-19,84,-15,23,35,-10,-19,33,44,85,8,32,
            34,39,38,35,49,-3,34,85,-8,32,84,95,23,65,48
        ]
    }, ]
}
var a = 1;

    setInterval(function () {
        if(a == (xData.length-10)){
            a=0;
        }
        myChartWsd.dispatchAction({
            type:'dataZoom',
            startValue:a,
            endValue:a+10
        });
        a++;
    },2000)