
optionSd = {
  series: [
    {
      type: 'gauge',
      startAngle: 200,
      endAngle: -20,
      center: ['50%', '60%'],
      radius: '90%',
      min: 0,
      max: 1,
      splitNumber: 8,
      axisLine: {
        lineStyle: {
          width: 6,
          color: [
            [0.25, '#FF6E76'],
            [0.5, '#FDDD60'],
            [0.75, '#58D9F9'],
            [1, '#7CFFB2']
          ]
        }
      },
      pointer: {
        icon: 'path://M12.8,0.7l12,40.1H0.7L12.8,0.7z',
        length: '12%',
        width: 20,
        offsetCenter: [0, '-60%'],
        itemStyle: {
          color: 'inherit'
        }
      },
      axisTick: {
        length: 12,
        lineStyle: {
          color: 'inherit',
          width: 2
        }
      },
      splitLine: {
        length: 20,
        lineStyle: {
          color: 'inherit',
          width: 5
        }
      },
      axisLabel: {
        color: '#999',
        fontSize: 15,
        distance: -50,
        rotate: 'tangential',
        formatter: function (value) {
          if (value === 1) {
            return '100%';
          } else if (value === 0.75) {
            return '75%';
          } else if (value === 0.50) {
            return '50%';
          } else if (value === 0.25) {
            return '25%';
          }else if (value === 0.0) {
            return '0%';
          }
          return '';
        }
      },
      title: {
        offsetCenter: [0, '-10%'],
        fontSize: 20
      },
      detail: {
        fontSize: 40,
        offsetCenter: [0, '-15%'],
        valueAnimation: true,
        formatter: function (value) {
          return Math.round(value * 100) + '';
        },
        color: 'inherit'
      },
      data: [
        {
          value: 0.7,
          name: ' '
        }
      ]
    }
  ]
};


setInterval(function () {
    myChartSd.setOption({
    series: [
      {
        data: [
          {
            value: humidityData/100
          }
        ]
      }
    ]
  });
}, 1000);
