from models import Dog, session

def create_table(base, engine):
    """Creates the table"""
    base.metadata.create_all(engine)

def save(session, dog):
    """Saves a dog instance to the database"""
    session.add(dog)
    session.commit()

def get_all(session):
    """Returns all dogs in the database"""
    return session.query(Dog).all()

def find_by_name(session, name):
    """Finds a dog by name"""
    return session.query(Dog).filter_by(name=name).first()

def find_by_id(session, id):
    """Finds a dog by ID"""
    return session.query(Dog).filter_by(id=id).first()

def find_by_name_and_breed(session, name, breed):
    """Finds a dog by name and breed"""
    return session.query(Dog).filter_by(name=name, breed=breed).first()

def update_breed(session, dog, breed):
    """Updates a dog's breed"""
    dog.breed = breed
    session.commit()
