from chateaubriand.app.extensions import db


class MemberModel(db.Model):
    __tablename__ = "member"

    id = db.Column(db.Integer, primary_key=True)
    team_id = db.Column(db.Integer, db.ForeignKey("team.id"))
    student_id = db.Column(db.Integer, db.ForeignKey("student.id"))