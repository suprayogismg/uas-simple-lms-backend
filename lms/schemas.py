from ninja import Schema

class CourseSchema(Schema):
    id: int
    title: str
    description: str

class CourseCreateSchema(Schema):
    title: str
    description: str
