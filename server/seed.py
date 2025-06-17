from app import app
from models import db, Message

with app.app_context():
    print("Clearing existing messages...")
    Message.query.delete()

    print("Seeding database...")
    msg1 = Message(username='Ian', body='Hello, World!')
    msg2 = Message(username='Robert', body='Chatterbox is alive!')
    
    db.session.add_all([msg1, msg2])
    db.session.commit()

    print("Seeding complete!")
