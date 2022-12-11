from fastapi import APIRouter, HTTPException, status, Body
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from server.controllers import *
from server.response_helper import *
from server.models import *


router = APIRouter()

# Humidity
@router.get("/api/humidity/all", response_description="Get all humidity data")
async def api_all_humidity():
    try:
        humidity = await get_all_humidity()
        return JSONResponse(status_code=status.HTTP_200_OK, content=success_response(humidity, message="Successfully retrieved all humidity"))
    except:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=fail_response(message="All data humidity not found"))


@router.get("/api/humidity", response_description="Get single humidity data")
async def api_get_humidity():
    try:
        humidity = await get_humidity()
        return JSONResponse(status_code=status.HTTP_200_OK, content=success_response(humidity, message="Successfully retrieved single humidity"))
    except:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=fail_response(message="Single data humidity not found"))


@router.post("/api/humidity", response_description="Add new humidity data")
async def api_add_humidity(store: HumidtySchema = Body(...)):
    value = jsonable_encoder(store)
    try:
        humidity = await store_humidity(value)
        return JSONResponse(status_code=status.HTTP_201_CREATED, content=success_response(humidity, message="Successfully added new humidity"))
    except:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=fail_response(message="Failed to add new humidity"))

# Moisture
@router.get("/api/moisture/all", response_description="Get all moisture data")
async def api_all_moisture():
    try:
        moisture = await get_all_moisture()
        return JSONResponse(status_code=status.HTTP_200_OK, content=success_response(moisture, message="Successfully retrieved all moisture"))
    except:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=fail_response(message="All data moisture not found"))


@router.get("/api/moisture", response_description="Get single moisture data")
async def api_get_moisture():
    try:
        moisture = await get_moisture()
        return JSONResponse(status_code=status.HTTP_200_OK, content=success_response(moisture, message="Successfully retrieved single moisture"))
    except:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=fail_response(message="Single data moisture not found"))


@router.post("/api/moisture", response_description="Add new moisture data")
async def api_add_moisture(value: float):
    if value is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=fail_response(message="Invalid input"))
    
    try:
        moisture = await store_moisture(value)
        return JSONResponse(status_code=status.HTTP_201_CREATED, content=success_response(moisture, message="Successfully added new moisture"))
    except:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=fail_response(message="Failed to add new moisture"))

# Temperature
@router.get("/api/temperature/all", response_description="Get all temperature data")
async def api_all_temperature():
    try:
        temperature = await get_all_temperature()
        return JSONResponse(status_code=status.HTTP_200_OK, content=success_response(temperature, message="Successfully retrieved all temperature"))
    except:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=fail_response(message="All data temperature not found"))


@router.get("/api/temperature", response_description="Get single temperature data")
async def api_get_temperature():
    try:
        temperature = await get_temperature()
        return JSONResponse(status_code=status.HTTP_200_OK, content=success_response(temperature, message="Successfully retrieved single temperature"))
    except:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=fail_response(message="Single data temperature not found"))


@router.post("/api/temperature", response_description="Add new temperature data")
async def api_add_temperature(value: float):
    if value is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=fail_response(message="Invalid input"))
    
    try:
        temperature = await store_temperature(value)
        return JSONResponse(status_code=status.HTTP_201_CREATED, content=success_response(temperature, message="Successfully added new temperature"))
    except:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=fail_response(message="Failed to add new moisture"))