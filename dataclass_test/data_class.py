from dataclasses import asdict, astuple, dataclass

@dataclass
class ComTest:
    id:int
    text:str

def func():
    com_test = ComTest(1,"It is test1")
    print(com_test)
    
    print(asdict(com_test))
    return astuple(com_test)

if __name__ =="__main__":
    func()
    


