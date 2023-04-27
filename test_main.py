#imports
import main 

def test_index():
    assert main.index() == 'Hello, world!'
    
def test_winc():
    assert main.winc() == 'Whoohooo, laatste opdracht van winc!'

# Aangepast nadat Github Actions/run-tests.yml groen is voor: run-tests, Deploy, Build

def test_hoera():
    assert main.hoera() == 'Hoera, als je dit ziet dan werkt het!'