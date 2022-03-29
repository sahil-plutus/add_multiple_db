
class CheckerRouter:
    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'teacher':
            return 'teacher'
        elif model._meta.app_label == 'student':
            return 'student'
        return 'default'

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'teacher':
            return 'teacher'
        elif model._meta.app_label == 'student':
            return 'student'
        return 'default'

    def allow_relation(self, obj1, obj2, **hints):
        if obj1._meta.app_label == 'student' or obj2._meta.app_label == 'student':
            return True
        elif 'student' not in [obj1._meta.app_label, obj2._meta.app_label]:
            return True
        elif obj1._meta.app_label == 'teacher' or obj2._meta.app_label == 'teacher':
            return True
        elif 'teacher' not in [obj1._meta.app_label, obj2._meta.app_label]:
            return True
        return False


    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label == 'student':
            return db == 'student'
        elif app_label == 'teacher':
            return db == 'teacher'
        return None
