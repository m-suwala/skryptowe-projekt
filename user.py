from mongoengine import *
import bcrypt

try:
    connect(host="mongodb+srv://Monika:drzewo123@cluster0.szlzs.mongodb.net/skryptowe?retryWrites=true&w=majority")
except Exception as e:
    print(e)


class User(Document):
    login = StringField(max_length=100, unique=True, required=True)
    password = StringField(max_length=100, required=True)
    favs = ListField()
    diet = StringField()


def create_acc(login, password):
    passw = bytes(password, 'utf-8')
    if len(password) < 8:
        raise ValidationError
    hashed = bcrypt.hashpw(passw, bcrypt.gensalt())
    user = User(login=login, password=hashed, diet="None")
    user.save()


def login(login, password):
    try:
        passw = bytes(password, 'utf-8')
        user = User.objects(login=login).first()
        if user:
            passw2 = bytes(user.password, 'utf-8')
            if bcrypt.checkpw(passw, passw2):
                return user.to_json()
        else:
            return None
    except Exception:
        pass

def add_to_fav(login, meal_id):
    try:
        user = User.objects(login=login).first()
        if meal_id in user.favs:
            pass
        else:
            user.favs.append(meal_id)
        user.save()
    except Exception:
        pass

def remove_from_fav(login, meal_id):
    try:
        user = User.objects(login=login).first()
        user.favs.remove(meal_id)
        user.save()
    except Exception:
        pass

def is_fav(login, meal_id):
    try:
        user = User.objects(login=login).first()
        return meal_id in user.favs
    except Exception:
        pass

def get_favs(login):
    try:
        user = User.objects(login=login).first()
        return user.favs
    except Exception:
        pass


def get_diet(login):
    try:
        user = User.objects(login=login).first()
        return user.diet
    except Exception:
        pass


def change_password(login, current_password, new_password):
    try:
        user = User.objects(login=login).first()
        curr_pass = bytes(current_password, 'utf-8')
        if user:
            passw = bytes(user.password, 'utf-8')
            if bcrypt.checkpw(curr_pass, passw) and len(new_password) >= 8:
                new_pass = bytes(new_password, 'utf-8')
                hashed = bcrypt.hashpw(new_pass, bcrypt.gensalt())
                user.update(password=hashed.decode())
                user.save()
                return True
        return False
    except Exception:
        return False


def clear_fav(login):
    try:
        user = User.objects(login=login).first()
        user.update(favs=[])
        user.save()
    except Exception as e:
        print(e)


def change_diet(login, new_diet):
    try:
        user = User.objects(login=login).first()
        user.update(diet=new_diet)
        user.save()
    except Exception as e:
        print(e)
