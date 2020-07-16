from chateaubriand.app.extensions import db


class StudentModel(db.Model):
    __tablename__ = "student"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    student_number = db.Column(db.String(4), nullable=False, unique=True)
    name = db.Column(db.String, nullable=False)

    single_files = db.relationship("SingleFileModel")
