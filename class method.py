class num_tuple:
    def __init__(self, lst):
        self.lst = lst
        self.num()
      
    def num(self):
        lst_b = []
        num_1 = 0
        for i in self.lst:
            lst_b.append(str(type(i)))
        for i in lst_b:
            if i == "<class 'tuple'>":
                num_1 += 1
        print(num_1)
