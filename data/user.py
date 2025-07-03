import dataclasses
@dataclasses.dataclass
class User:
    first_name: str
    last_name: str
    email: str
    user_number: int
    year: int
    month: str
    day: str
    gender: str
    subjects: str
    upload_picture: str
    hobbies: str
    current_address: str
    state: str
    city: str

    @property
    def date_birthday(self):
        return f"{int(self.day)} {self.month},{self.year}"