 function downloadFile() {
        // 创建一个隐藏的链接元素
        var link = document.createElement('a');
        // link.href = './static/sensor.xlsx'; // 替换为你要下载的文件的路径
        link.href = './static/D2023_05_24.xls'; // 替换为你要下载的文件的路径
        // 设置下载的文件名
        link.download = 'data.xls'; // 替换为你要下载的文件名
        // 触发点击事件，执行文件下载
        link.click();
    }
