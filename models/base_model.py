#!/usr/bin/python3
"""
This module contains a super class called
`BaseModel` that defines all common attributes/methods
for other classes
"""
from datetime import datetime
import models
import uuid


class BaseModel:
    """This class contains init - constractor method which initialize three
    public instance attributes, str - magic method that returns a string
    representation of an object, save method - that updates attribute and
    a dictionary method that returns dictionary"""

    def __init__(self, *args, **kwargs):
        """Initialize public instance attributes
        Args:
            args (): no-keyword argument (argument order is important)
            kwargs (attr): key-worded argument
            (argument order is not important)
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        if kwargs is not None and len(kwargs) != 0:
            self.id = kwargs['id']
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    date_and_time = value.split("T")
                    date = date_and_time[0].split("-")
                    time = date_and_time[1].split(":")
                    sec_micro_sec = time[2].split(".")
                    msec = int(sec_micro_sec[1])
                    d = [int(i) for i in date]
                    t = [int(float(j)) for j in time]
                    f = datetime(d[0], d[1], d[2], t[0], t[1], t[2], msec)
                    if key == 'created_at':
                        self.created_at = f
                    if key == 'updated_at':
                        self.updated_at = f

    def __str__(self):
        """Returns formated string representation of an object """
        return f'[{self.__class__.__name__}] ({self.id}) {self.__dict__}'

    def save(self):
        """Update the public instance attribute `updated_at` with the current
        datetime
        """
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """Returns a dictionary containing all keys/values of
        __dict__ of the instance
        """
        dcn = self.__dict__.copy()
        dcn['created_at'] = self.created_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        dcn['updated_at'] = self.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        dcn['__class__'] = self.__class__.__name__

        return dcn
