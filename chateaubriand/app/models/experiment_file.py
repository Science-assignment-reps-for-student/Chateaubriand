from chateaubriand.app.extensions import db


class ExperimentFileModel(db.Model):
    __tablename__ = "experiment_file"

    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey("student.id"))
    assignment_id = db.Column(db.Integer, db.ForeignKey("homework.id"))
    team_id = db.Column(db.Integer, db.ForeignKey("team.id"))
    file_name = db.Column(db.String, nullable=False)
    path = db.Column(db.String, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)
    is_late = db.Column(db.Boolean, nullable=False)

    student = db.relationship("StudentModel")
