import os

from bcrypt import checkpw, hashpw, gensalt

from app.modules import db


class Vault(db.Model):
    """Vault model class for SQLAlchemy ORM"""
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    vault_name = db.Column(db.String(100), nullable=False, unique=True)
    vault_key = db.Column(db.String(300), nullable=False)
    vault_id = db.Column(db.String(100), nullable=False)
    salt = db.Column(db.String(200), default=gensalt)

    # NOTE: In a real application make sure to properly hash and salt passwords
    def check_password(self, password: str):
        """Validate if the string password passed as argument is the same password as stored in the db"""
        return self.vault_key == password

    def save(self):
        """Save current entity"""
        if not self.id:
            db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_by_name(vault_name:str):
        return Vault.query.filter_by(vault_name=vault_name).one_or_none()
