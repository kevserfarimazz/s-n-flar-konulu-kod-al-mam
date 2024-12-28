class ogrenci:
    def __init__(self,ogrno,kadi,sifre,mail):
        self.ogrno=ogrno
        self.kadi=kadi
        self.sifre=sifre
        self.mail=mail
    def bilgigoruntuleme(self):
        print("öğrenci numarası" , self.ogrno ,"adı" ,self.kadi,"şifresi", self.sifre,"Mail adresi", self.mail)

class transkript(ogrenci):
    def __init__(self,ders1,ders2,ders3,ders4,ders5):
        self.ders1=ders1
        self.ders2=ders2
        self.ders3=ders3
        self.ders4=ders4
        self.ders5=ders5                                                     
    def dersler(self):
        print("dersler", self.ders1,self.ders2,self.ders3,self.ders4,self.ders5)

class akademik(ogrenci):
    def __init__(self,ders1not,ders1finalnot,ders2not,ders2finalnot,ders3not,ders3finalnot,ders4not,ders4finalnot,ders5not,ders5finalnot):
        self.ders1not=ders1not
        self.ders1finalnot=ders1finalnot
        self.ders2not=ders2not
        self.ders2finalnot=ders2finalnot
        self.ders3not=ders3not
        self.ders3finalnot=ders3finalnot
        self.ders4not=ders4not
        self.ders4finalnot=ders4finalnot
        self.ders5not=ders5not
        self.ders5finalnot=ders5finalnot
    ortalama=0

    def notlar(self):
        self.ortalama=(self.ders1not+self.ders1finalnot)/2
        print("1. dersin ortalaması=",self.ortalama)
        self.ortalama=(self.ders2not+self.ders2finalnot)/2
        print("2. dersin ortalaması=",self.ortalama)
        self.ortalama=(self.ders3not+self.ders3finalnot)/2
        print("3. dersin ortalaması=",self.ortalama)
        self.ortalama=(self.ders4not+self.ders4finalnot)/2
        print("4. dersin ortalaması=",self.ortalama)
        self.ortalama=(self.ders5not+self.ders5finalnot)/2
        print("5. dersin ortalaması=",self.ortalama)
        self.ortalama=(self.ders1not+self.ders1finalnot+self.ders2not+self.ders2finalnot+self.ders3not+self.ders3finalnot+self.ders4not+self.ders4finalnot+self.ders5not+self.ders5finalnot)/10
        print("hepsinin ortalaması=",self.ortalama)

class devam(ogrenci):
    def __init__(self,ders1devam,ders2devam,ders3devam,ders4devam,ders5devam):
        self.ders1devam=ders1devam
        self.ders2devam=ders2devam
        self.ders3devam=ders3devam
        self.ders4devam=ders4devam
        self.ders5devam=ders5devam
    def kalma(self):
        if self.ders1devam>4:
            print("devamsızlıktan kaldınız")
        else:
            print("devamsızlığınızda sorun yok")
        if self.ders2devam>4:
            print("devamsızlıktan kaldınız")
        else:
            print("devamsızlığınızda sorun yok")
        if self.ders3devam>4:
            print("devamsızlıktan kaldınız")
        else:
            print("devamsızlığınızda sorun yok")
        if self.ders4devam>4:
            print("devamsızlıktan kaldınız")
        else:
            print("devamsızlığınızda sorun yok")
        if self.ders5devam>4:
            print("devamsızlıktan kaldınız")
        else:
            print("devamsızlığınızda sorun yok")

class saglik(ogrenci):
    def __init__(self,raporsayisi):
        self.raporsayisi=raporsayisi
    def rapor(self):
        print("rapor şu kadar kullanıldı:", self.raporsayisi)

Kevser=ogrenci(435841,"Kevser",1283,"kevser@gmail.com")
Kevser.bilgigoruntuleme()

Kevser=transkript("ders1","ders2","ders3","ders4","ders5")
Kevser.dersler()

Kevser=akademik(89,90,90,90,89,67,87,99,67,46)
Kevser.notlar()

Kevser=devam(1,2,3,1,5)
Kevser.kalma()

Kevser=saglik(15)
Kevser.rapor()