from chateaubriand.app.extensions import db


class TeamModel(db.Model):
    __tablename__ = "team"

    id = db.Column(db.Integer, primary_key=True)
    leader_id = db.Column(db.Integer, db.ForeignKey("student.id"))
    homework_id = db.Column(db.Integer, db.ForeignKey("homework.id"))
    name = db.Column(db.String)