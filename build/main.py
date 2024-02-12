from TelasGerais.login import InterfaceLogin
from Backend.DataBase import Connection

if __name__ == '__main__':
    
    conn = Connection()
    conn.criaBanco()
    
    login = InterfaceLogin()
    login.inicializa()