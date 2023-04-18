#imports
import main 

def test_index():
    assert main.index() == 'Hello, world!'
    
def test_winc():
    assert main.winc() == 'Whoohooo, laatste opdracht van winc!'
