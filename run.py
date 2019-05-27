from gecole import app
from gecole import db


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)