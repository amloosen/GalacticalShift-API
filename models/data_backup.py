"""User model"""
from sqlalchemy import Column, Integer, BigInteger, DateTime, Float, VARCHAR, Text# ForeignKey

from models.db import Model
from models.base_object import BaseObject


class DataBackup(BaseObject, Model):

    id = Column(Integer, primary_key=True)

    user_id            = Column(VARCHAR(length=100))
    study_part       = Column(Integer, nullable=False)
    times_element1_backup = Column(Text(length=100000), nullable=False)
    times_element2_backup = Column(Text(length=100000), nullable=False)
    times_element3_backup = Column(Text(length=100000), nullable=False)
    indicKey_backup = Column(Text(length=100000), nullable=False)
    trialSgmMu_backup = Column(Text(length=100000), nullable=False)
    indicKey_backup = Column(Text(length=100000), nullable=False)
    bonus                = Column(Text(length=100000))

    def get_bonus(self):
       return str(self.bonus)


    def get_id(self):
        return (self.id)

    def get_user_id(self):
        return str(self.user_id)

    def get_study_part(self):
        return (self.study_part)

    def get_trialSgmMu(self):
        return (self.trialSgmMu)


    def get_times_element1_backup(self):
        return (self.times_element1_backup)

    def get_times_element2_backup(self):
        return (self.times_element2_backup)

    def get_times_element3_backup(self):
        return (self.times_element3_backup)

    def get_trialRT_backup(self):
        return (self.trialRT_backup)

    def get_indicKey_backup(self):
        return (self.indicKey_backup)

    def get_trialSgmMu_backup(self):
        return (self.trialSgmMu_backup)


    def errors(self):
        errors = super(DataBackup, self).errors()
        return errors
