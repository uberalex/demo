from bottle import route, run, template, static_file

@route('/hello/<name>')
def hello(name):
    return template('<b>Hello {{name}}</b>!', name=name)


@route('/')
def home():
    return template('index.html')


@route("/static/js/<filepath:re:.*\.js>")
def js(filepath):
    return static_file(filepath, root="static/js")


@route("/static/css/<filepath:re:.*\.css>")
def csss(filepath):
    return static_file(filepath, root="static/css")

run(host='localhost', port=8080, debug=True)
