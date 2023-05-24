from flask import Flask, send_file
import time
import io
app = Flask(__name__)


@app.route('/download')
def download_file():
    # 读取需要下载的文件内容
    filename = time.strftime("D%Y_%m_%d", time.localtime()) +'.xls'
    path = '/home/loongson/Project/'+ filename
    with open(path, 'rb') as f:
        file_content = f.read()
        # 将文件内容返回给客户端进行下载
        return send_file(
            io.BytesIO(file_content),
            attachment_filename=filename,as_attachment=True
        )


if __name__ == '__main__':
    app.run(host='192.168.43.3', port=5000)


