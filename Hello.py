from flask import request, Flask , jsonify

app = Flask("__name__")

courses = [
    {
        "id":1,
        "name":"English",
        "description":"English courses"
    },
    {
        "id":2,
        "name":"Kinyarwanda",
        "description":"English courses"
    },
    {
        "id":3,
        "name":"History",
        "description":"English courses"
    },
    {
        "id":4,
        "name":"Chemistry",
        "description":"English courses"
    },
    {
        "id":5,
        "name":"Math",
        "description":"English courses"
    },
]

@app.get("/courses")
def getCourses():
    return jsonify(courses), 200

    

@app.get("/course/<int:course_id>")
def getAcourse(course_id):
    for course in courses:
        if course["id"] == course_id:
            return jsonify(course), 200
    return "Course Not Found", 404


@app.post("/courses")
def createCourse():
    newCourse = request.get_json()
    courses.append(newCourse)
    return jsonify(newCourse), 201  # 201 for resource creation


@app.delete("/course/<int:course_id>")
def deleteCourse(course_id):
    for course in courses:
        if course["id"] == course_id:
            courses.remove(course)
            return "Removed Successfully!", 200
    return "Course Not Found", 404

        
@app.put("/courses/<int:course_id>")
def updateCourse(course_id):
    for course in courses:
        if course["id"] == course_id:
            updated_data = request.get_json()
            course.update(updated_data)  # Update the original course
            return jsonify({"message": "Course Updated", "course": course}), 200
    return "Course Not Found", 404

        



