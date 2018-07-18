import feedsreader

from flask import Flask
app = Flask(__name__, static_url_path='/static')

@app.route('/')
def feeds():
    feedsreader.execute_feed_read_write()
    return app.send_static_file('index.html')

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')