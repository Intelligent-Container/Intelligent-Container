// const WebSocket = require('ws');

// 定义服务器地址和端口
const HOST = '192.168.123.60';  // 服务器的IP地址或主机名
const PORT = 9000;  // 服务器的端口号

// 创建WebSocket对象
const clientSocket = new WebSocket(`ws://${HOST}:${PORT}`);

// 连接成功时的回调函数
clientSocket.onopen = () => {
    console.log('连接到服务器');
    const message = 'Hello';
    clientSocket.send(message);
    console.log(`发送消息：${message}`);

    // 每2秒发送一次消息
    timeoutId = setInterval(getData,2000);

};

function getData() {
        const message = 'get';
        clientSocket.send(message);
        console.log(`发送消息：${message}`);
}

// 接收消息时的回调函数
clientSocket.onmessage = (event) => {
    const receivedData = event.data;
    var parsedData = JSON.parse(receivedData);

    temperatureData = parsedData.wd;
    humidityData = parsedData.sd;
    smokeData = parsedData.yw;

    console.log(`接收到来自服务器的消息：${receivedData}`);


};

// 连接关闭时的回调函数
clientSocket.onclose = () => {
    clearTimeout(timeoutId);
    console.log('与服务器的连接已关闭');
};
