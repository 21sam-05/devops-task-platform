from fastapi import FastAPI

app = FastAPI(
    title="DevOps Task Platform",
    description="A learning project for revising DevOps concepts",
    version="1.0.0"
)


@app.get("/")
def root():
    return {
        "message": "DevOps Task Platform is running!"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }



@app.get("/tasks")
def get_tasks():
    return {
        "tasks": [
            {
                "id": 1,
                "title": "Learn Docker",
                "completed": False
            },
            {
                "id": 2,
                "title": "Learn Kubernetes",
                "completed": False
            }
        ]
    }
