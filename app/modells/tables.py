from app import db

class User(db.Model):
    __tablename__ = "users"
    id = db.Collumn(db.Integer, primary_key=True)
    usernaem = db.Collumn(db.String, unique_key=True)
    password = db.Collumn(db.String)
    name =db.Column(db.String)
    email = db.Collumn(db.String, unique_key=True)


    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    @property
    def is_active(self):
        return False
    def get_id(self):
        return str(self.id)

    def __init__(self, username, password, name, email):
        self.username = username
        self.password = password
        self.name =name
        self.email =email

    def __repr__(self):
        return "User %r>" % self.username


class Post(db.Model):
    __tablename__ = "posts"

    id = db.Collumn(db.Integer, primary_key=True)
    content = db.Collumn(db.Text)
    user_id = db.Collumn(db.Integer,db.ForeignKey('user.id'))

    user = db.relationship('User', foreign_Keys=user_id)

    def __init__(self, content, user_id):
        self.content =content
        self.user_id = user_id

    def __repr__(self):
        return "<Post %r." % self.id

class Follow(db.Model):
    __tablename__ = "follow"

    id = db.Collumn(db.Integer, primary_key=True)
    user_id = db.Collumn(db.Integer, db.ForeignKey('user.id'))
    follower_id = db.Collumn(b.Integer, db.ForeignKey('user.id'))

    user = db.relationship('User', foreign_Keys=user_id)
    follower = db.relationship('User', foreign_Keys=user_id)