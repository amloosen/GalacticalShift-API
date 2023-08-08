"""User model"""
from sqlalchemy import Column, Integer, BigInteger, DateTime, Float, VARCHAR # ForeignKey
from models.db import Model
from models.base_object import BaseObject
import numpy

class SliderTraining(BaseObject, Model):

    id = Column(Integer, primary_key=True)

    user_id            = Column(VARCHAR(length=100))
    study_part       = Column(Integer, nullable=False)
    startTime         = Column(VARCHAR(length=200))


    sectionStartTime = Column(VARCHAR(length=100))
    practSgmMu = Column(VARCHAR(length=10000), nullable=False)


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

    def get_practSgmMu(self):
        return (self.practSgmMu)


    def errors(self):
        errors = super(SliderTraining, self).errors()
        return errors
