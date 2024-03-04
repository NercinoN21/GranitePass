"""
Routine responsible for running the app
"""
from granitepass import create_app

app = create_app()


if __name__ == '__main__':
    app.run(debug=True)
