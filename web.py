from flask import Flask
app = Flask('app')


@app.route('/')
def hello_world():
    try:
        import main
        main.main()
    except Exception as e:
        print(e)
        pass
    return 'trying to run'


app.run(host='0.0.0.0', port=8080)
