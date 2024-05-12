import psycopg2


class PostgreSQLConnection:
    
    def __init__(self, dbname, user, password, host='localhost', port='5432'):
        self.dbanme = dbname
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.conn = None
    
    def conectar(self):
        try:
            self.conn = psycopg2.connect(dbname = self.dbanme, user=self.user, password= self.password, host=self.host, port=self.port)
            print("Conexão com sucesso!")
        except psycopg2.Error as e:
            print("Erro ao conectar ao Postgres: ", e)
        pass
    
    def select_user(self, query):
        if not self.conn:
            print("Você não está conectado!")
            return None
        try:
            cursor = self.conn.cursor()
            cursor.execute(query)
            rows = cursor.fetchall()
            cursor.close()
            return rows
        except psycopg2 as e:
            print("Erro ao executar a consulta", e)
            return None
        
            
    def insert_user(self, id, name, area, job_description, role, salary, is_active, last_evaluation):
        if not self.conn:
            print("Você não esta conectado")
            return None
        try:
            cursor = self.conn.cursor()
            cursor.execute(
                "INSERT INTO users (id, name, area, job_description, role, salary, is_active, last_evaluation) VALUES(%s, %s, %s, %s, %s, %s, %s, %s)",
                (id, name, area, job_description, role, salary, is_active, last_evaluation)
            )
            self.conn.commit()
            cursor.close()
            print("Usuario regsitrado")
        except psycopg2.Error as e:
            print('Não foi possivel registrar! - ', e)
    
    
    def delete_user(self, user_id: int):
        if not self.conn:
            print("Você não esta conectado")
            return None
        try:
            cursor = self.conn.cursor()
            cursor.execute(
                "DELETE FROM users WHERE id = %s",
                (user_id,)
            )
            self.conn.commit()
            cursor.close()
            print("Registro deletado!")
            
        except psycopg2.Error as e:
            print("Não foi possivel deletar! - ", e)
    
    def update_user(self, id=None, name=None, area=None, job_description=None, role=None, salary=None, is_activate=None, last_evaluation=None):
        if not self.conn:
           print("Você não esta conectado")
           return None
       
        try:
            cursor = self.conn.cursor()
            
            update_query = "UPDATE user SET"
            update_values = []
            
            if name is not None:
                update_query += " name = %s,"
                update_values.append(name)

            if area is not None:
                update_query += " area = %s,"
                update_values.append(area)

            if job_description is not None:
                update_query += " job_description = %s,"
                update_values.append(job_description)

            if role is not None:
                update_query += " role = %s,"
                update_values.append(role)

            if salary is not None:
                update_query += " salary = %s,"
                update_values.append(salary)

            if is_activate is not None:
                update_query += " is_activate = %s,"
                update_values.append(is_activate)
            
            if last_evaluation is not None:
                update_query += " last_evaluation = %s,"
                update_values.append(last_evaluation)
                        
            
            update_query = update_query.strip(',') + " WHERE id = %s"
            update_values.append(id)
            
            cursor.execute(update_query, tuple(update_values))
            self.conn.commit()
            cursor.close()
            print("Usuario atualizado!")
            
        except psycopg2.Error as e:
            print('Deu ruim', e)
    
        
    def close(self):
        if self.conn:
            self.conn.close()
            print("Conexão fechada!")
