class Phone:
    IMEI = None     # 序列号
    producer = "HM" # 厂商

    def call_by_4g(self):
        print("4g通话")



class Phone2022(Phone):
    face_id = "10001"   # 面部识别ID


    def call_by_5g(self):
        print("2022年新功能，5g通话")


class Phone2024(Phone):
    producer = "Itcast" # 复写父类属性

    def call_by_4g(self):
        print("5g通话") # 复写父类方法
        # 方式1
        Phone.call_by_4g(self) # 复写后调用父类的成员方法
        print(Phone.producer)  # 复写后调用父类的成员属性
        # 方式2 
        print(super().producer)  # 复写后调用父类的成员属性
        super().call_by_4g()     # 复写后调用父类的成员方法

# phone = Phone2022()
# phone.call_by_4g()


class NFCReader:
    nfc_type = "第五代"
    producer = "HM"


    def read_card(self):
        print("NFC读卡")

    def write_card(self):
        print("NFC写卡")


class RemoteControl:
    rc_type = "红外遥控"

    def control(self):
        print("红外遥控开启了")


class MyPhone(Phone, NFCReader, RemoteControl):
    pass # 没有任何含义，为了保持定义的完整性

# 输出同名的属性成员，以从左到右的顺序为依据
# myphone = MyPhone()
# myphone.call_by_4g()
# myphone.read_card()
# myphone.control()