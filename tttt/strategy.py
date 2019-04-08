
class AdminShow(object):
    def show(self):
        return "show with admin"
    

class UserShow(object):
    def show(self):
        return "show with user"
    

class Question(object):
    def __init__(self, show_obj):
        self.show_obj = show_obj

    def show(self):
        return self.show_obj.show()


if __name__ == '__main__':
    q = Question(AdminShow())
    print(q.show())
    q.show_obj = UserShow()
    print(q.show())
   