"""A Base Model for the AirBnB project"""

import uuid
from datetime import datetime
import models


class BaseModel():
    """This is the superclass for the entire project.

    Attributes:
        id : a randomly generated UUID for each object.
        created_at : the timestamp when an instance is initialized.
        updated_at : the timestamp when an instance is last updated.
        DateF : the standard timestamp format used across all instances.

    Methods:
        __str__ : returns the dictionary representation of an instance.
    """

    DateF = "%Y-%m-%dT%H:%M:%S.%f"

    def __init__(self, *args, **kwargs):
        """Initialize an instance with either provided dictionary values or randomly generated ones.

        Args:
            *args: Currently not in use.
            **kwargs: Dictionary representation of an object to initialize the instance from.
        """

        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)
        else:
            for key, value in kwargs.items():
                if key in ["created_at", "updated_at"]:
                    setattr(self, key, datetime.strptime(value, self.DateF))
                elif key != "__class__":
                    setattr(self, key, value)

    def save(self):
        """Update modified time of the instance"""

        self.updated_at = datetime.now()
        models.storage.save()

    def __str__(self):
        """Returns custom dictionary representation of the instance """

        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)


    def to_dict(self):
        """Return dict representation of the instance with additional
        attributes and iso formatted date-time
        """

        dict_repr = vars(self)
        dict_repr["__class__"] = self.__class__.__name__
        for key, value in dict_repr.items():
            if key == "updated_at" or key == "created_at":
                dict_repr[key] = value.isoformat(timespec="microseconds")
        return dict_repr
