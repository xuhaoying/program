# 王小二的家里有三种电器分别是灯，风扇和电视，在王小二离开家的时候需要将这三种电器都关闭。下面代码中我们实现了该功能。但是我们发现王小二和电器之间关联太紧密了，你有什么办法降低王小二和电器之间的耦合度吗？ 请编写相应代码，并给出测试代码。

class Lamp(object):
    """
    灯对象
    """
    def power_off(self):
        print("Lamp power off")


class Fan(object):
    """
    电风扇
    """
    def switch_off(self):
        print("Fan switch off")


class Tv(object):
    """
    电视机
    """
    def off(self):
        print("Tv off")

class PowerOff(object):
    
    def __init__(self):
        self.lamp = Lamp()
        self.fan = Fan()
        self.tv = Tv()
    
    def off(self):
        self.lamp.power_off()
        self.fan.switch_off()
        self.tv.off()


class Person(object):
    """
    人
    """
    def __init__(self):
        self.power = PowerOff()

    def leave_home(self):
        """
        出门散步啦，需要关闭所有电器
        """
        self.power.off()


if __name__ == '__main__':
    wang = Person()
    wang.leave_home()