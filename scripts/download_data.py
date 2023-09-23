from decouple import config
import psycopg2 as pg
import pandas as pd

params = {
    "host" : config("RDS_HOST"),
    "port" : config("PORT"),
    "user" : config("USER"),
    "password" : config("PASSWORD"),
    "database" : config("DATABASE"),
}

class DatabaseHandler():
    def __init__(self, params):
        self.params = params
        self.conn = pg.connect(**params)
        self.curr = self.conn.cursor()
        
    def get_all_rows(self, table):
        sql_query = f"""
            SELECT * FROM  {table}"""
        self.curr.execute(sql_query)        
        rows = self.curr.fetchall()     
        column_names = [desc[0] for desc in self.curr.description]
        print(column_names)
        return rows, column_names

    def rows_to_csv(self, rows, file_name="data.csv", columns=None):
        df = pd.DataFrame(rows, columns=columns)
        df.to_csv(file_name, index=False)
        print(f"Saved {file_name} to disk")

    def __del__(self):
        self.conn.close()
        self.curr.close()

if __name__ == '__main__':
    db = DatabaseHandler(params)
    tables = list(map(str, config('TABLES')[1:-1].split(', ')))
    for table in tables:
        rows, column_names = db.get_all_rows(table=table)
        db.rows_to_csv(
            rows=rows,
            file_name=f"./data/{table}.csv",
            columns=column_names
        )
