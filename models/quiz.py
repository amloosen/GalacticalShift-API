"""User model"""
from sqlalchemy import Column, Integer, BigInteger, DateTime, Float, VARCHAR, ARRAY, Text # ForeignKey
from models.db import Model
from models.base_object import BaseObject
import numpy


class Quiz(BaseObject, Model):

    id = Column(Integer, primary_key=True)

    user_id = Column(VARCHAR(length=100))
    study_part = Column(Integer, nullable=False)
    startTime = Column(VARCHAR(length=100))
    sectionStartTime = Column(VARCHAR(length=100))
    sectionEndTime = Column(VARCHAR(length=100))
    timesRepeated = Column(VARCHAR(length=1000))
    timesRestarted = Column(VARCHAR(length=1000))

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

    def get_sectionEndTime(self):
        return (self.sectionStartTime)

    def get_timesRepeated(self):
        return (self.timesRepeated)

    def get_timesRestarted(self):
        return (self.timesRestarted)

    def errors(self):
        errors = super(Quiz, self).errors()
        return errors
