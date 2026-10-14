from fastapi import FastAPI
import psycopg2

connection=psycopg2.connect(
    host="db.fqdkhdjankbnfjbzrahw.supabase.co",
    port=5432,
    database="postgres",
    user="postgres",
    password="OjotoUnion123"
)

app=FastAPI()

@app.post("/tasks")
def create_task(task_name:str,assigned_to:str,status:str): 
    cursor=connection.cursor()
    cursor.execute(
        """
        INSERT INTO tasks (task_name, assigned_to, status) VALUES (%s, %s, %s)
        """,
        (task_name, assigned_to, status)
    )
    connection.commit()
    cursor.close()
    connection.close()
    return {"message": "Task created successfully"}
    