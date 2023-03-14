class Multi_ListNode :
    def __init__(self, item):
        self.item = item
        self.nextName = None
        self.nextId = None
    def listByName(self):
        s = "\n"
        while self is not None:
            #print(self.item)
            s = s + str(self.item) + "\n"
            self = self.nextName
#        s = s + "--"
        return s
    def listById(self):
        s = "\n"
        while self is not None:
            #print(self.item)
            s = s + str(self.item) + "\n"
            self = self.nextId
#        s = s + "--"
        return s


A = Multi_ListNode({"1001","Rose"})
B = Multi_ListNode({"1005","Jisoo"})
C = Multi_ListNode({"1007","Lisa"})
D = Multi_ListNode({"1002","Jennie"})
C.nextName = D
D.nextName = B
B.nextName = A
A.nextId = D
D.nextId = B
B.nextId = C
print(C.listByName())
print("---------------")
print(A.listById())
print(type({"1002","Jennie"}))