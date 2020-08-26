from chateaubriand.app.extensions import db


class SelfEvaluationModel(db.Model):
    __tablename__ = "personal_evaluation"

    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey("student.id"))
    assignment_id = db.Column(db.Integer, db.ForeignKey("homework.id"))
    scientific_accuracy = db.Column(db.Integer, nullable=False)
    communication = db.Column(db.Integer, nullable=False)
    attitude = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)
