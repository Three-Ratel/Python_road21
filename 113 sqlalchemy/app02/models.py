from app02 import db


class Test(db.Model):
    __tablename__ = 'test'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), nullable=False)


if __name__ == '__main__':
    from app02 import create_app
    app = create_app()
    db.drop_all(app=app)
    db.create_all(app=app)
