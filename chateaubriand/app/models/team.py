from chateaubriand.app.extensions import db


class TeamModel(db.Model):
    __tablename__ = "team"

    id = db.Column(db.Integer, primary_key=True)
    leader_id = db.Column(db.Integer, db.ForeignKey("student.id"))
    assignment_id = db.Column(db.Integer, db.ForeignKey("homework.id"))
    name = db.Column(db.String)

    members = db.relationship("MemberModel")
