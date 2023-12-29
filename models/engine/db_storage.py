#!/usr/bin/python3
"""DBStorage class for interacting with the db"""

from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import BaseModel, Base
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class DBStorage():
    """Database Engine"""

    __engine = None
    __session = None

    def __init__(self):
        """The constructor for this class"""

        username = getenv('HBNB_MYSQL_USER')
        password = getenv('HBNB_MYSQL_PWD')
        host = getenv('HBNB_MYSQL_HOST')
        db = getenv('HBNB_MYSQL_DB')
        env = getenv('HBNB_ENV')

        con_string = f"mysql+mysqldb://{username}:{password}@{host}/{db}"
        self.__engine = create_engine(con_string, pool_pre_ping=True)
        Session = sessionmaker(bind=self.__engine,
                               expire_on_commit=False)
        self.__session = Session()

        if env == 'test':
            Base.metadata.drop_all(bind=self.__engine)

    def classes(self):
        """returns a dict of classes"""

        return {
            "BaseModel": BaseModel,
            "Amenity": Amenity,
            "City": City,
            "Place": Place,
            "Review": Review,
            "State": State,
            "User": User
        }

    def all(self, cls=None):
        """query on the current db session and returns all objects
        depending on if the class name is given or none
        """

        if not cls:
            classes = [User, State, City, Amenity, Place, Review]
        else:
            classes = [self.classes()[cls]]

        result = []
        result = self.__session.query(*classes).all()

        map = {}
        for obj in result:
            key = '{}.{}'.format(type(obj).__name__, obj.id)
            obj.pop("_sa_instance_state")
            map[key] = obj
        return map

    def new(self, obj):
        """Add the object to the current database session (self.__session)"""

        self.__session.add(obj)

    def save(self):
        """commit all changes of the current db session (self.__session)"""

        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current db session obj if not None"""

        if obj:
            self.__session.delete(obj)

    def reload(self):
        """create all tables in the db using a sessionmaker"""

        Base.metadata.create_all(self.__engine)
        self.__session = sessionmaker(bind=self.__engine,
                                      expire_on_commit=False)
        Session = scoped_session(self.__session)
        self.__session = Session()

    def close(self):
        """Removes the session object"""

        self.__session.close()
