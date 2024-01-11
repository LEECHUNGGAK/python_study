from pydantic import BaseModel, ConfigDict
from beanie import Document
from typing import Optional, List


class Event(Document):
    title: str
    image: str
    description: str
    tags: List[str]
    location: str

    model_config = ConfigDict(
        json_schema_extra={
            "examples": [
                {
                    "title": "FastAPI Book Launch",
                    "image": "https://linktomyimage.com/image.png",
                    "description": (
                        "We will be discussing the contes of the FastAPI book in this event. "
                        "Ensure to come with your own copy to win gifts!"
                    ),
                    "tags": [
                        "python",
                        "fastapi",
                        "book",
                        "launch",
                    ],
                    "location": "Google Meet",
                }
            ]
        }
    )

    class Settings:
        name = "events"


class EventUpdate(BaseModel):
    title: Optional[str] = None
    image: Optional[str] = None
    description: Optional[str] = None
    tags: Optional[List[str]] = None
    location: Optional[str] = None

    model_config = ConfigDict(
        json_schema_extra={
            "Examples": [
                {
                    "title": "FastAPI Book Launch",
                    "image": "https://linktomyimage.com/image.png",
                    "description": (
                        "We will be discussing the contes of the FastAPI book in this event. "
                        "Ensure to come with your own copy to win gifts!"
                    ),
                    "tags": [
                        "python",
                        "fastapi",
                        "book",
                        "launch",
                    ],
                    "location": "Google Meet",
                }
            ]
        }
    )
