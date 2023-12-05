#!/usr/bin/python3

"""This module contain parent class
 contains all common attributes
 for later inheritance.
"""

from uuid import uuid4
import datetime
import models


class BaseModel:
    """ BaseModel is a general model
    for all other models.
    it has the common methods, attributes required.
    to take care of the initialization, serialization and
    deserialization of your future instances
    """

    def __init__(self,  *args, **kwargs):
        """
        Initialize a new BaseModel instance.
        Assigns a unique id and the current datetime
        to created_at and updated_at.
        """
        if len(kwargs) > 0:
            for key, value in kwargs.items():
                if key == "created_at" or key == 'updated_at':
                    value = datetime.datetime.strptime(
                        kwargs[key], "%Y-%m-%dT%H:%M:%S.%f")
                if (key != "__class__"):
                    setattr(self, key, value)

        else:
            self.id = str(uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)

    def __str__(self):
        """
        Return a string representation of the BaseModel instance.
        """
        return "[{}] ({}) {}". \
            format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """
        Update the updated_at attribute with the current datetime.
        """
        self.updated_at = datetime.datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Return a dictionary representation of the BaseModel instance.
        This dictionary includes all instance attributes, the class name,
        and created_at and updated_at in ISO format.
        """
        dc = self.__dict__.copy()
        dc['created_at'] = self.created_at.isoformat()
        dc['updated_at'] = self.updated_at.isoformat()
        dc['__class__'] = self.__class__.__name__

        return dc
