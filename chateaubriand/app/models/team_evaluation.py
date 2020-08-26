from chateaubriand.app.extensions import db


class MutualEvaluationModel(db.Model):
    __tablename__ = "team_evaluation"

    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey("student.id"))
    assignment_id = db.Column(db.Integer, db.ForeignKey("homework.id"))
    target_id = db.Column(db.Integer, db.ForeignKey("student.id"))
    communication = db.Column(db.Integer, nullable=False)
    cooperation = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)
