from chateaubriand.app.extensions import db


class HomeworkModel(db.Model):
    __tablename__ = "homework"

    id = db.Column(db.Integer, primary_key=True)
    deadline_1 = db.Column(db.DateTime, nullable=False)
    deadline_2 = db.Column(db.DateTime, nullable=False)
    deadline_3 = db.Column(db.DateTime, nullable=False)
    deadline_4 = db.Column(db.DateTime, nullable=False)
    title = db.Column(db.String, nullable=False)
    description = db.Column(db.String)
    type = db.Column(db.Enum("SINGLE", "MULTI", "EXPERIMENT"), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)

    single_files = db.relationship("SingleFileModel")