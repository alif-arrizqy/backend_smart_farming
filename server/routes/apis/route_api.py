from fastapi import APIRouter, HTTPException, status, Body
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from server.controllers import *
from server.response_helper import *
from server.models import *


router = APIRouter()

# Cabai
# Humidity
@router.get("/api/humidity/cabai/all", response_description="Get all humidity data")
async def api_all_humidity():
    try:
        humidity = await get_all_humidity_cabai()
        return JSONResponse(status_code=status.HTTP_200_OK, content=success_response(humidity, message="Successfully retrieved all humidity"))
    except:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=fail_response(message="All data humidity not found"))


@router.get("/api/humidity/cabai", response_description="Get single humidity data")
async def api_get_humidity():
    try:
        humidity = await get_humidity_cabai()
        return JSONResponse(status_code=status.HTTP_200_OK, content=success_response(humidity, message="Successfully retrieved single humidity"))
    except:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=fail_response(message="Single data humidity not found"))

# Moisture
@router.get("/api/moisture/cabai/all", response_description="Get all moisture data")
async def api_all_moisture():
    try:
        moisture = await get_all_moisture_cabai()
        return JSONResponse(status_code=status.HTTP_200_OK, content=success_response(moisture, message="Successfully retrieved all moisture"))
    except:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=fail_response(message="All data moisture not found"))


@router.get("/api/moisture/cabai", response_description="Get single moisture data")
async def api_get_moisture():
    try:
        moisture = await get_moisture_cabai()
        return JSONResponse(status_code=status.HTTP_200_OK, content=success_response(moisture, message="Successfully retrieved single moisture"))
    except:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=fail_response(message="Single data moisture not found"))


# Temperature
@router.get("/api/temperature/cabai/all", response_description="Get all temperature data")
async def api_all_temperature():
    try:
        temperature = await get_all_temperature_cabai()
        return JSONResponse(status_code=status.HTTP_200_OK, content=success_response(temperature, message="Successfully retrieved all temperature"))
    except:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=fail_response(message="All data temperature not found"))


@router.get("/api/temperature/cabai", response_description="Get single temperature data")
async def api_get_temperature():
    try:
        temperature = await get_temperature_cabai()
        return JSONResponse(status_code=status.HTTP_200_OK, content=success_response(temperature, message="Successfully retrieved single temperature"))
    except:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=fail_response(message="Single data temperature not found"))

# Tomat
# Humidity
@router.get("/api/humidity/tomat/all", response_description="Get all humidity data")
async def api_all_humidity():
    try:
        humidity = await get_all_humidity_tomat()
        return JSONResponse(status_code=status.HTTP_200_OK, content=success_response(humidity, message="Successfully retrieved all humidity"))
    except:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=fail_response(message="All data humidity not found"))


@router.get("/api/humidity/tomat", response_description="Get single humidity data")
async def api_get_humidity():
    try:
        humidity = await get_humidity_tomat()
        return JSONResponse(status_code=status.HTTP_200_OK, content=success_response(humidity, message="Successfully retrieved single humidity"))
    except:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=fail_response(message="Single data humidity not found"))

# Moisture
@router.get("/api/moisture/tomat/all", response_description="Get all moisture data")
async def api_all_moisture():
    try:
        moisture = await get_all_moisture_tomat()
        return JSONResponse(status_code=status.HTTP_200_OK, content=success_response(moisture, message="Successfully retrieved all moisture"))
    except:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=fail_response(message="All data moisture not found"))


@router.get("/api/moisture/tomat", response_description="Get single moisture data")
async def api_get_moisture():
    try:
        moisture = await get_moisture_tomat()
        return JSONResponse(status_code=status.HTTP_200_OK, content=success_response(moisture, message="Successfully retrieved single moisture"))
    except:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=fail_response(message="Single data moisture not found"))


# Temperature
@router.get("/api/temperature/tomat/all", response_description="Get all temperature data")
async def api_all_temperature():
    try:
        temperature = await get_all_temperature_tomat()
        return JSONResponse(status_code=status.HTTP_200_OK, content=success_response(temperature, message="Successfully retrieved all temperature"))
    except:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=fail_response(message="All data temperature not found"))


@router.get("/api/temperature/tomat", response_description="Get single temperature data")
async def api_get_temperature():
    try:
        temperature = await get_temperature_tomat()
        return JSONResponse(status_code=status.HTTP_200_OK, content=success_response(temperature, message="Successfully retrieved single temperature"))
    except:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=fail_response(message="Single data temperature not found"))

# Terung
# Humidity
@router.get("/api/humidity/terung/all", response_description="Get all humidity data")
async def api_all_humidity():
    try:
        humidity = await get_all_humidity_terung()
        return JSONResponse(status_code=status.HTTP_200_OK, content=success_response(humidity, message="Successfully retrieved all humidity"))
    except:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=fail_response(message="All data humidity not found"))


@router.get("/api/humidity/terung", response_description="Get single humidity data")
async def api_get_humidity():
    try:
        humidity = await get_humidity_terung()
        return JSONResponse(status_code=status.HTTP_200_OK, content=success_response(humidity, message="Successfully retrieved single humidity"))
    except:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=fail_response(message="Single data humidity not found"))

# Moisture
@router.get("/api/moisture/terung/all", response_description="Get all moisture data")
async def api_all_moisture():
    try:
        moisture = await get_all_moisture_terung()
        return JSONResponse(status_code=status.HTTP_200_OK, content=success_response(moisture, message="Successfully retrieved all moisture"))
    except:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=fail_response(message="All data moisture not found"))


@router.get("/api/moisture/terung", response_description="Get single moisture data")
async def api_get_moisture():
    try:
        moisture = await get_moisture_terung()
        return JSONResponse(status_code=status.HTTP_200_OK, content=success_response(moisture, message="Successfully retrieved single moisture"))
    except:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=fail_response(message="Single data moisture not found"))


# Temperature
@router.get("/api/temperature/terung/all", response_description="Get all temperature data")
async def api_all_temperature():
    try:
        temperature = await get_all_temperature_terung()
        return JSONResponse(status_code=status.HTTP_200_OK, content=success_response(temperature, message="Successfully retrieved all temperature"))
    except:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=fail_response(message="All data temperature not found"))


@router.get("/api/temperature/terung", response_description="Get single temperature data")
async def api_get_temperature():
    try:
        temperature = await get_temperature_terung()
        return JSONResponse(status_code=status.HTTP_200_OK, content=success_response(temperature, message="Successfully retrieved single temperature"))
    except:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=fail_response(message="Single data temperature not found"))
