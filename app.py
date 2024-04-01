from src import crear_app



if __name__ == '__main__':
    app = crear_app()
    app.run('0.0.0.0', port=5100, debug=True)