from app.models import User

def register_user(email, password):
    user = User(email, password)
    user.save()
