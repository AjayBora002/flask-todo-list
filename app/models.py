from app import db
class Task(db.Model): # ye ek Task model hai jo database me tasks ko represent karega, mtlb ye table banayega
    # db.model ye flask ko bolega jo class hai use real database table me convert kar de

    id = db.Column(db.Integer, primary_key=True) # unique id for each task
    title = db.Column(db.String(100), nullable=False) # title of the task
    status = db.Column(db.String(20), default="Pending") # status of the task, whether it's pending, in progress, or completed
    