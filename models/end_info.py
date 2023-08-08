"""User model"""
from sqlalchemy import Column, Integer, String, ARRAY, Text,VARCHAR, Float

from models.db import Model
from models.base_object import BaseObject


class EndInfo(BaseObject, Model):

    id = Column(Integer, primary_key=True)

    user_id            = Column(VARCHAR(length=100))
    study_part       = Column(Integer, nullable=False)
    startTime         = Column(VARCHAR(length=100))
    sectionStartTime = Column(VARCHAR(length=100))

    feedback             = Column(Text(length=10000))
    bonus                = Column(Text(length=10000))

    def get_id(self):
        return (self.id)

    def get_user_id(self):
        return str(self.user_id)

    def get_study_part(self):
        return (self.study_part)

    def get_startTime(self):
        return (self.startTime)

    def get_sectionStartTime(self):
        return (self.sectionStartTime)

    def get_feedback(self):
        return str(self.feedback)

    def get_bonus(self):
        return str(self.bonus)


    def errors(self):
        errors = super(EndInfo, self).errors()
        return errors
