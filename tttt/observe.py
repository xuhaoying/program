import abc


class Subject(object):
    def __init__(self):
        self._observers = []

    def attach(self, observer):
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer):
        try:
            self._observers.remove(observer)
        except ValueError:
            pass

    def notify(self):
        for observer in self._observers:
            observer.update(self)


class Course(Subject):
    def __init__(self):
        super(Course, self).__init__()
        self._message = None

    @property
    def message(self):
        return self._message
    
    @message.setter
    def message(self, msg):
        self._message = msg
        self.notify()


class Observer(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def update(self, subject):
        pass


class UserObserver(Observer):
    def update(self, subject):
        print("User observer: ", subject.message)

class OrgObserver(Observer):
    def update(self, subject):
        print("Organization observer: ", subject.message)     

if __name__ == '__main__':
    # 初始化一个用户观察者
    user = UserObserver()
    # 初始化一个机构观察者
    org = OrgObserver()

    # 初始化一个课程
    course = Course()
    # 注册观察者
    course.attach(user)
    course.attach(org)

    # 设置course.message，这时观察者会收到通知
    course.message = "two observers"

    # 注销一个观察者
    course.detach(user)
    course.message = "single observer"