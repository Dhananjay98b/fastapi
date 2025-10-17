from fastapi import FastAPI,HTTPException
app =FastAPI()

students = [
    {"id": 1, "name": "Aarav", "section": "A", "attendance": 92.5},
    {"id": 2, "name": "Meera", "section": "B", "attendance": 85.0},
    {"id": 3, "name": "Karan", "section": "C", "attendance": 76.3},
    {"id": 4, "name": "Riya", "section": "A", "attendance": 89.9},
    {"id": 5, "name": "Vikram", "section": "B", "attendance": 94.2},
    {"id": 6, "name": "Sneha", "section": "C", "attendance": 68.7},
    {"id": 7, "name": "Aditya", "section": "A", "attendance": 73.5},
    {"id": 8, "name": "Pooja", "section": "B", "attendance": 97.1},
    {"id": 9, "name": "Rahul", "section": "C", "attendance": 88.4},
    {"id": 10, "name": "Divya", "section": "A", "attendance": 90.8}
]
# @app.get('/students/{id}')
# def get_student_data(id:int):
#     if id not in students:
#         raise HTTPException(status_code =404, details ="product id not found")

# @app.get('/students/{students_name}')
# def get_student_data(students_name:str):
#     if students_id not in students:
#         raise HTTPException(status_code =404, details ="product id not found")

@app.get("/students/id")
def get_student_by_id(student_id: int):
    return [s for s in students if s["id"] == student_id]

@app.get("/students/name")
def get_student_by_name(student_name: str):
    return [s for s in students if s["name"].lower() == student_name.lower()]

    
