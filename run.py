from app import create_app, db
from app.models import Task

app = create_app()
with app.app_context(): # ye flask ko btata hai ki ab hum app context ke andar hain
    db.create_all()  # Create database tables for our data models

if __name__ == '__main__':
    app.run(debug=True)