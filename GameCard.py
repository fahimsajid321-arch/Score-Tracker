# class Players:
#     def __init__(self):
#         self.Faheem = list()
#         self.Waseem = list()
#         self.Usama = list()
#         self.Waqar = list()
#     def add_score(self, Faheem, Waseem,Usama,Waqar):
#         self.Faheem.append(Faheem)
#         self.Waseem.append(Waseem)
#         self.Usama.append(Usama)
#         self.Waqar.append(Waqar)
#         if sum(self.Faheem) < 100:
#             print(f"Faheem: {self.Faheem} : Total = {sum(self.Faheem)}")
#         else:
#             print("Faheem Thrown Out")
#             Faheem = "Thrown out"
#         if sum(self.Waseem) < 100:
#             print(f"Waseem: {self.Waseem} : Total = {sum(self.Waseem)}")
#         else:
#             print("Waseem Thrown Out")
#             Waseem = "Thrown out"
#         if sum(self.Usama) < 100:
#             print(f"Usama: {self.Usama} : Total = {sum(self.Usama)}")
#         else:
#             print("Usama Thrown Out")
#             Usama = "Thrown out"
#         if sum(self.Waqar) < 100:
#             print(f"Waqar: {self.Waqar} : Total = {sum(self.Waqar)}")
#         else:
#             print("Waqar Thrown Out")
#             Waqar = "Thrown out"
#         Round =[Faheem,Waseem,Usama,Waqar]
#         print(f"Round Score: {Round}")

# a = Players()
# a.add_score(10,10,20,15)
# print(a.add_score(10,20,30,40))
# print(a.add_score(12,13,14,15))
# print(a.add_score(12,13,14,30))
# print(a.add_score(12,13,14))
# print(a.add_score(12,13,14))


class Players:
    def __init__(self):
        self.Faheem = list()
        self.Waseem = list()
        self.Usama = list()
        self.Waqar = list()

    # Setting =None allows you to stop passing an argument once someone is out
    def add_score(self, Faheem=None, Waseem=None, Usama=None, Waqar=None):
        # Faheem
        if Faheem is not None and sum(self.Faheem) < 100:
            self.Faheem.append(Faheem)
            if sum(self.Faheem) >= 100:
                print("Faheem Thrown Out")
                Faheem = "Thrown out"
            else:
                print(f"Faheem: {self.Faheem} : Total = {sum(self.Faheem)}")
        else:
            Faheem = "Thrown out"

        # Waseem
        if Waseem is not None and sum(self.Waseem) < 100:
            self.Waseem.append(Waseem)
            if sum(self.Waseem) >= 100:
                print("Waseem Thrown Out")
                Waseem = "Thrown out"
            else:
                print(f"Waseem: {self.Waseem} : Total = {sum(self.Waseem)}")
        else:
            Waseem = "Thrown out"

        # Usama
        if Usama is not None and sum(self.Usama) < 100:
            self.Usama.append(Usama)
            if sum(self.Usama) >= 100:
                print("Usama Thrown Out")
                Usama = "Thrown out"
            else:
                print(f"Usama: {self.Usama} : Total = {sum(self.Usama)}")
        else:
            Usama = "Thrown out"

        # Waqar
        if Waqar is not None and sum(self.Waqar) < 100:
            self.Waqar.append(Waqar)
            if sum(self.Waqar) >= 100:
                print("Waqar Thrown Out")
                Waqar = "Thrown out"
            else:
                print(f"Waqar: {self.Waqar} : Total = {sum(self.Waqar)}")
        else:
            Waqar = "Thrown out"

        Round = [Faheem, Waseem, Usama, Waqar]
        print(f"Round Score: {Round}\n")


a = Players()

# Round 1: All 4 play
a.add_score(10, 10, 20, 15)

# Round 2: All 4 play
a.add_score(10, 20, 30, 40)

# Round 3: All 4 play (Waqar crosses 100: 15 + 40 + 50 = 105 -> Thrown Out)
a.add_score(12, 13, 14, 50)

# Round 4: Waqar's argument is removed completely; only pass 3 arguments
a.add_score(12, 13, 14)
a.add_score(12,14,13,13)