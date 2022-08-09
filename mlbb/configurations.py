from configparser import ConfigParser, NoOptionError, NoSectionError
import os


def load_config(config: ConfigParser, section: str, name: str, default=None) -> str:
    try:
        output = config.get(section, name)
    except (NoOptionError, NoSectionError) as e:
        output = default
    return output


def config() -> None:
    config_parse = ConfigParser()
    config_parse.read("settings.ini")
    SYSTEM = "SYSTEM"
    CLOUDINARY = 'CLOUDINARY'
    USER = 'USER'

    # SYSTEM
    os.environ.setdefault("DJANGO_DEBUG", load_config(config_parse, SYSTEM, "DJANGO_DEBUG", "False"))
    os.environ.setdefault("SECRET_KEY", load_config(config_parse, SYSTEM, "SECRET_KEY", "super_secret_key"))
    os.environ.setdefault("HOST", load_config(config_parse, SYSTEM, "HOST", "localhost:8000"))

    # CLOUDINARY
    os.environ.setdefault("CLOUD_NAME", load_config(config_parse, CLOUDINARY, "CLOUD_NAME", "clodinary-super-name" ))
    os.environ.setdefault("API_KEY", load_config(config_parse, CLOUDINARY, 'API_KEY', 'cloudinary_api'))
    os.environ.setdefault("API_SECRET", load_config(config_parse, CLOUDINARY, 'API_SECRET', 'cloudinary_secret'))

    # USER
    os.environ.setdefault("LOGIN_FOR_EMAIL", load_config(config_parse, USER, "LOGIN_FOR_EMAIL", 'emailhost'))
    os.environ.setdefault("PASSWORD_FOR_EMAIL", load_config(config_parse, USER, "PASSWORD_FOR_EMAIL", 'emailpassword'))