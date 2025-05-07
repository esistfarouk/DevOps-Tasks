from fastapi import FastAPI, HTTPException
import redis
import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

# Redis configuration
redis_client = redis.Redis(
    host=os.getenv('REDIS_HOST', 'redis'),
    port=int(os.getenv('REDIS_PORT', 6379)),
    db=0,
    decode_responses=True
)

# PostgreSQL configuration
def get_db_connection():
    try:
        return psycopg2.connect(
            host=os.getenv('POSTGRES_HOST', 'postgres'),
            user=os.getenv('POSTGRES_USER', 'postgres'),
            password=os.getenv('POSTGRES_PASSWORD', 'postgres'),
            database=os.getenv('POSTGRES_DB', 'postgres')
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database connection failed: {str(e)}")


@app.get("/")
async def index():
    return {"message": "Welcome to the FastAPI application!"}

@app.get("/redis")
async def redis_test():
    try:
        redis_client.set('test_key', 'Hello from Redis!')
        value = redis_client.get('test_key')
        return {"redis_value": value}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/postgres")
async def postgres_test():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT version()")
        result = cursor.fetchone()
        cursor.close()
        conn.close()
        return {"postgres_status": "Connected successfully", "version": result[0]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "main:app",
        host=os.getenv('HOST', '0.0.0.0'),
        port=int(os.getenv('PORT', 8000)),
        reload=True
    )