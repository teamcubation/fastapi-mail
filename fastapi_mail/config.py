from typing import Optional

from jinja2 import Environment, FileSystemLoader
from pydantic import Field
from pydantic import DirectoryPath, EmailStr
from typing_extensions import Annotated
from pydantic_settings import BaseSettings


class ConnectionConfig(Settings):
    MAIL_USERNAME: str
    MAIL_PASSWORD: str
    MAIL_PORT: int = 465
    MAIL_SERVER: str
    MAIL_TLS: bool = False
    MAIL_SSL: bool = True
    MAIL_DEBUG: Annotated[int, Field(gt=-1, lt=2)] = 0  # type: ignore
    MAIL_FROM: EmailStr
    MAIL_FROM_NAME: Optional[str] = None
    TEMPLATE_FOLDER: Optional[DirectoryPath] = None
    SUPPRESS_SEND: Annotated[int, Field(gt=-1, lt=2)] = 0  # type: ignore
    USE_CREDENTIALS: bool = True
    VALIDATE_CERTS: bool = True

    def template_engine(self) -> Environment:
        """Return template environment."""
        folder = self.TEMPLATE_FOLDER
        if not folder:
            raise ValueError(
                'Class initialization did not include a ``TEMPLATE_FOLDER`` ``PathLike`` object.'
            )
        template_env = Environment(loader=FileSystemLoader(folder))
        return template_env
