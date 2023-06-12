from flask import render_template

from src.main.moveit import create_app
from src.config import config_instance

app = create_app(config=config_instance())


@app.get('/')
def get_root():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
