import dataclasses
@dataclasses.dataclass
class User:
    first_name: str
    last_name: str
    email: str
    userNumber: int
    DateBithday: str
    gender: str
    subjects: str
    uploadPicture: str
    Hobbies: str
    CurrentAddress: str
    state: str
    city: str