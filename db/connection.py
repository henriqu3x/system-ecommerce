import psycopg2
import logging

logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")

class Connection():
    def __init__(self, user, password, host, port, database):
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.database = database

        self.conn = None
        self.cur = None

    def conectar(self):
        try:
            self.conn = psycopg2.connect(database=self.database, 
                                         password=self.password, 
                                         user=self.user, 
                                         host=self.host, 
                                         port=self.port)
            
            self.cur = self.conn.cursor()
        except Exception as e:
            logging.error(f'Ocorreu um erro ao tentar se conectar ao banco de dados: {e}')
            self.desconectar()

    def desconectar(self):
        try:
            if self.cur:
                self.cur.close()
            if self.conn:
                self.conn.close()
        except Exception as e:
            logging.error(f'Ocorreu um erro ao tentar se desconectar do banco de dados: {e}')

    def manipular(self, sql, variaveis=None):
        try:
            self.conectar()

            if variaveis:
                self.cur.execute(sql, variaveis)
            else:
                self.cur.execute(sql)

            self.conn.commit()

            logging.debug('SQL EXECUTADO COM SUCESSO!')
            return True
        except Exception as e:
            logging.error(f'Ocorreu um erro ao tentar manipular o banco de dados: {e}')
            return False
        finally:
            self.desconectar()

    def consultar(self, sql, variaveis=None):
        try:
            self.conectar()

            if variaveis:
                self.cur.execute(sql, variaveis)
            else:
                self.cur.execute(sql)

            consulta = self.cur.fetchall()

            return consulta
        except Exception as e:
            logging.error(f'Ocorreu um erro ao tentar fazer uma consulta no banco de dados: {e}')
            return []
        finally:
            self.desconectar()
