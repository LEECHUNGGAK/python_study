from beanie import PydanticObjectId
from fastapi import APIRouter, HTTPException, Path, status
from typing import List

from database.connection import Database
from models.events import Event, EventUpdate


event_router = APIRouter(tags=["Event"])

event_database = Database(Event)


@event_router.get("/", response_model=List[Event])
async def retrieve_all_events() -> List[Event]:
    events = await event_database.get_all()
    return events


@event_router.get("/{id}", response_model=Event)
async def retrieve_event(id: PydanticObjectId = Path(..., title="The ID of the event to retrieve")) -> Event:
    event = await event_database.get(id)
    if not event:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Event with supplied ID does not exist",
        )
    return event


@event_router.post("/new")
async def create_event(body: Event) -> dict:
    await event_database.save(body)
    return {
        "message": "Event created successfully."
    }


@event_router.put("/{id}", response_model=Event)
async def update_event(
    body: EventUpdate,
    id: PydanticObjectId=Path(..., title="The ID of the event to update"),
) -> Event:
    updated_event = await event_database.update(
        id=id,
        body=body,
    )
    if not updated_event:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Event with supplied ID does not exist",
        )
    return update_event

@event_router.delete("/{id}")
async def delete_event(id: PydanticObjectId=Path(..., title="The ID of the event to update")) -> dict:
    result = event_database.delete(id=id)
    if not result:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Event with supplied ID does not exist",
        )
    return {
        "message": "Event deleted successfully."
    }
