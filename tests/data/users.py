
import os


VALID_USER = {
    "name": os.getenv("SB_NAME", "Akbota"),
    "email": os.getenv("SB_EMAIL", "autotest_user@example.com"),
    "password": os.getenv("SB_PASSWORD", "Qwerty123"),
}


INVALID = {
    "short_password": "12345",
}
