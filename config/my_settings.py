DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "Scheme Name",
        "USER": "User Name",
        "PASSWORD": "Your Password",
        "HOST": "localhost",
        "PORT": "Database Server Port",
        "OPTIONS": {
            "init_command": "SET sql_mode='STRICT_TRANS_TABLES'",
            "charset": "utf8mb4",
            "use_unicode": True,
        },
    }
}

SECRET_KEY = {
    "secret": "m!#@+v40p*05jd2fds2fe)me1f&4mvfi!igbv7b^2dyrn5=o2dw!i-0u7*&^",
    "algorithm": "HS256",
}

EMAIL = {
    "EMAIL_BACKEND": "django.core.mail.backends.smtp.EmailBackend",
    "EMAIL_USE_TLS": True,
    "EMAIL_PORT": 587,
    "EMAIL_HOST": "smtp.naver.com",
    "EMAIL_HOST_USER": "lee88067@naver.com",
    "EMAIL_HOST_PASSWORD": "1648audu!",
    "SERVER_EMAIL": "Gmail ID",
    "REDIRECT_PAGE": "https://www.naver.com",
}
