from abc import abstractmethod, ABCMeta

class RunAppMagatire(metaclass=ABCMeta):

    @abstractmethod
    def put(self, a):
        return a

class output(RunAppMagatire):

    def r(self,a):
        print(666666,a)



print(isinstance(RunAppMagatire,list))