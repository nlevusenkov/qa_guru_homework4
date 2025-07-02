import dataclasses
@dataclasses.dataclass
class User:
    first_name: str
    last_name: str
    email: str
    userNumber: int
    year: int
    month: str
    day: str
    gender: str
    subjects: str
    uploadPicture: str
    Hobbies: str
    CurrentAddress: str
    state: str
    city: str

    @property
    def DateBithday(self):
        return f"{int(self.day)} {self.month},{self.year}"