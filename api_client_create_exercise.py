from clients.courses.courses_client import CreateCourseRequestDict, get_course_client
from clients.exercises.exercises_client import get_exercises_client, CreateExerciseRequestDict
from clients.files.files_client import CreateFileRequestDict, get_files_client
from clients.private_http_builder import AuthenticationUserDict
from clients.users.public_users_client import get_public_users_client, CreateUserRequestDict
from tools.fakers import get_random_email

public_users_client = get_public_users_client()

# Инициализируем запрос на создание пользователя
create_user_request = CreateUserRequestDict(
    email=get_random_email(),
    password="string",
    lastName="string",
    firstName="string",
    middleName="string"
)

# Отправляем POST запрос на создание пользователя
create_user_response = public_users_client.create_user(create_user_request)

# Инициализируем пользовательские данные для аутентификации
authentification_user = AuthenticationUserDict(
    email = create_user_request["email"],
    password = create_user_request["password"]
)

files_client = get_files_client(authentification_user)
course_client = get_course_client(authentification_user)
exercises_client = get_exercises_client(authentification_user)

create_file_request = CreateFileRequestDict(
    filename='image.png',
    directory='courses',
    upload_file='./testdata/files/image.png'
)
create_file_response = files_client.create_file(create_file_request)
print("Create file data:", create_file_response)

create_course_request = CreateCourseRequestDict(
    title="title",
    maxScore=100,
    minScore=10,
    description="Python API course",
    estimatedTime="2 weeks",
    previewFileId=create_file_response['file']['id'],
    createdByUserId=create_user_response['user']['id']
)

create_course_response = course_client.create_course(create_course_request)
print('Create course data:', create_course_response)

create_exercise_request = CreateExerciseRequestDict(
    title='Exercise 1',
    courseId = create_course_response['course']['id'],
    maxScore=5,
    minScore=1,
    orderIndex=0,
    description="Exercise 1",
    estimatedTime="5 minutes"
)

create_exercise_response = exercises_client.create_exercise(create_exercise_request)
print('Create exercise data:', create_exercise_response)
