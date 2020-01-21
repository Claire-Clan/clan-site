from clan_blog import create_app


app = create_app()

if __name__ == "__main__":
    """ Run flask app """
    app.run(host="127.0.0.1:5000")
