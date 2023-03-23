

# __<method_name> er for at indikere, at det ikke er meningen at denne metode skal overrides. når man bruger __foran metodenavnet, vil metoden blive "name-mangled" og få sat _<Classname> foran. name-mangling er for at gøre det usandsynligt, at metoden ved et uheld bliver overridet. Metoden i class A vil se sådan her ud: _A__method
class A:
    def __method(self):
        print('I am a method in A')
    
    def method(self):
        self.__method()

a = A()
a.method()

# overrider __method i A klassen, ved at override det navn metoden får pga "name-mangling". Det er ikke meningen at man skal gøre dette.
class B(A):
    def _A__method(self):
        print('Im a method in B')

    def __len__(self):
        return 10

b = B()
b.method()
print(len(b))
