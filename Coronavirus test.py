class Virus_corona :
    def __init__(self,oxjen,dama,fesharkhon,zarabanghalb) :

        self.oxjen=oxjen
        self.dama=dama
        self.fesharkhon=fesharkhon
        self.zarabanghalb=zarabanghalb

t_corona_oxjen = float(input("please select oxjen :"))
t_corona_dama = float(input("please select dama :"))
t_corona_fesharhkon = float(input("please select fesharkhon :"))
t_corona_zarabanghalb = float(input("please select zarabanghalb :"))



if t_corona_oxjen < 40 and t_corona_dama < 30 :
    print("check test corona")
elif t_corona_oxjen < 30 and t_corona_dama < 20 and t_corona_fesharhkon < 10 and t_corona_zarabanghalb :
    print("virus corona  ")
else :
    print("test shoma - ast")