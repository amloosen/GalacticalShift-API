"""User model"""
from sqlalchemy import Column, Integer, BigInteger, DateTime, Float, VARCHAR # ForeignKey
from models.db import Model
from models.base_object import BaseObject
import numpy

class TrainingA(BaseObject, Model):

    id = Column(Integer, primary_key=True)

    user_id            = Column(VARCHAR(length=100))
    study_part       = Column(Integer, nullable=False)
    startTime         = Column(VARCHAR(length=100))
    sectionStartTime = Column(VARCHAR(length=100))

    corr_pos = Column(VARCHAR(length=100))
    all_corr_values = Column(VARCHAR(length=100))
    valueOnElement = Column(VARCHAR(length=100))
    trainAcc = Column(VARCHAR(length=100))

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

    def get_corr_pos(self):
        return (self.corr_pos)

    def get_all_corr_values(self):
        return (self.all_corr_values)

    def get_valueOnElement(self):
        return (self.valueOnElement)

    def get_trainAcc(self):
        return (self.trainAcc)

    def errors(self):
        errors = super(TrainingA, self).errors()
        return errors
