
class Role:
    n = 123 #类变量
    n_list = []
    name = "我是类name"
    def __init__(self, name, role, weapon, life_value=100, money=15000):
        #构造函数
        #在实例化时做一些类的初始化的工作
        self.name = name #r1.name=name实例变量(静态属性),作用域就是实例本身
        self.role = role
        self.weapon = weapon
        self.__life_value = life_value	#添加两个下划线，定义为私有属性，
										#外部访问不了，不能在外都调取
        self.money = money
    def __del__(self):
	#析构函数： 在实例释放、销毁的时候自动执行的，通常用于做一些收尾工作， 如关闭一些数据库连接，关闭打开的临时文件
	#在程序结束时执行,外部删除实例是也执行
        pass #print("%s 彻底死了。。。。" %self.name)

    def show_status(self):
        print("name:%s weapon:%s life_val:%s" %(self.name,
                                                 self.weapon,
                                                self.__life_value))	#私有属性内部可以访问。调取
    def shot(self): # 类的方法，功能 （动态属性）
        print("shooting...")

    def __got_shot(self): #私有方法，外部不可访问
        self.__life_value -=50
        print("%s:ah...,I got shot..."% self.name)

    def buy_gun(self, gun_name):
        print("%s just bought %s" % (self.name,gun_name) )



r1 = Role('Chenronghua', 'police',  'AK47') # Role(r1,'Alex', 'police',  'AK47')把一个类变成一个具体对象的过程叫 实例化(初始化一个类，造了一个对象)
r1.buy_gun("AK47")
r1.got_shot()
r1.__got_shot()#出错，不可访问
print(r1.show_status())



r2 = Role('jack', 'terrorist', 'B22')  #生成一个角色
r2.got_shot()
r1.name = "陈荣华"
r1.n_list.append("from r1")		#添加到了类变量，而不是实例变量
r1.n_list = [1,2,3,4]		#添加到实例变量
r1.bullet_prove = True  #可以给 ri 类中添加属性，添加了一个实例变量
# r1.n = "改类变量" 	#实质是给 ri 创建了一个实例变量，不是修改类 role 中的类变量
# print("r1:",r1.weapon,r1.n )
# #del r1.weapon
#
#
#
#
# #print(r1.n,r1.name,r1.bullet_prove,r1.weapon)
#
# #
# r2 = Role('jack', 'terrorist', 'B22')  #生成一个角色
# r2.name = "徐良伟"
# r2.n_list.append("from r2")
# print("r2:",r2.name,r2.n,r2.n_list)
# # r2.got_shot() #Role.got_shot(r2)
#
Role.n = "ABC" 	#修改类的类变量
# print(Role.n_list)
#
# print(r1.n ,r2.n )
