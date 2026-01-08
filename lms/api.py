from ninja import Router
from .models import Course
from .schemas import CourseSchema, CourseCreateSchema
from .jwt_auth import JWTAuth

router = Router()

@router.get("/courses", response=list[CourseSchema])
def list_courses(request):
    return Course.objects.all()

@router.post("/courses", auth=JWTAuth())
def create_course(request, data: CourseCreateSchema):
    return Course.objects.create(**data.dict())
