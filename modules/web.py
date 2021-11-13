from flask import Flask
from modules.logs import logger
import logging


def main():
    app = Flask("app")
    app.logger.disabled = True

    log = logging.getLogger("werkzeug")
    log.setLevel(logging.ERROR)

    @app.route("/")
    def hello_world():
        logger.info("Got request")
        try:
            import main

            main.main()
            logger.info("Webserver ran main")
        except Exception as e:
            logger.exception(e)
            print(e)
            pass
        return "trying to run"

    app.run(host="0.0.0.0", port=8080)


if __name__ == "__main__":
    main()
