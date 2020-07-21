from chateaubriand.app.extensions import db


class MultiFileModel(db.Model):
    __tablename__ = "multi_file"

    id = db.Column(db.Integer, primary_key=True)
    homework_id = db.Column(db.Integer, db.ForeignKey("homework.id"))
    team_id = db.Column(db.Integer, db.ForeignKey("team.id"))
    file_name = db.Column(db.String, nullable=False)
    path = db.Column(db.String, nullable=False, unique=True)
    created_at = db.Column(db.DateTime, nullable=False)
    is_late = db.Column(db.Boolean, nullable=False)