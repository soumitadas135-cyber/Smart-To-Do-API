from fastapi import APIRouter, Depends
from app.database import db
from bson import ObjectId

router = APIRouter(prefix="/tasks")

@router.post("/")
async def create_task(task: dict):
    result = await db.tasks.insert_one(task)
    return {"id": str(result.inserted_id)}

@router.get("/")
async def get_tasks():
    tasks = []
    async for task in db.tasks.find():
        task["_id"] = str(task["_id"])
        tasks.append(task)
    return tasks

@router.put("/{task_id}")
async def update_task(task_id: str, task: dict):
    await db.tasks.update_one(
        {"_id": ObjectId(task_id)}, {"$set": task}
    )
    return {"message": "Task updated"}

@router.delete("/{task_id}")
async def delete_task(task_id: str):
    await db.tasks.delete_one({"_id": ObjectId(task_id)})
    return {"message": "Task deleted"}