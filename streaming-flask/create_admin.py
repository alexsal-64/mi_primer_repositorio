from app import app
from models import db, Admin

with app.app_context():
    admin = Admin(username="alexsal")
    admin.set_password("ve10x172859n")
    db.session.add(admin)
    db.session.commit()
    print("¡Usuario administrador creado exitosamente!")