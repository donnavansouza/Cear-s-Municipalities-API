import json
from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware


# Initialize FastAPI application
app = FastAPI()

origins = ["http://localhost:3000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load the JSON data once at the start
with open("localization.json") as file:
    data = json.load(file)["Worksheet"]


# Root endpoint: returns all the data
@app.get("/")
def read_root():
    return {"message": "API is up and running."}


@app.get("/municipalities")
def get_municipalities():
    return data


# Endpoint to get a municipality by name
@app.get("/municipality/{item_name}")
def get_item(item_name: str):
    for item in data:
        if item["Municipality_name"].lower() == item_name.lower():
            return item
    raise HTTPException(status_code=404, detail="No municipality found.")


# Endpoint to get municipalities with population greater than the specified value in 2017
@app.get("/municipality/population/{population}")
def get_population(population: int):
    filtered_data = [
        item for item in data if int(item["Total population 2017"]) > population
    ]
    if filtered_data:
        return JSONResponse(content=filtered_data)
    raise HTTPException(status_code=404, detail="No municipality found.")


# Endpoint to get municipalities that start with a specific character
@app.get("/municipality/startswith/{char}")
def get_municipality_by_char(char):
    filtered_data = [
        item
        for item in data
        if item["Municipality_name"].lower().startswith(char.lower())
    ]
    if filtered_data:
        return JSONResponse(content=filtered_data)
    raise HTTPException(status_code=404, detail="No municipality found.")


# Endpoint to get municipalities with population greater than the specified value for a given year
@app.get("/municipality/population/{population}/year/{year}")
def get_population_year(population: int, year: int):
    try:
        filtered_data = [
            item
            for item in data
            if int(item["Total population " + str(year)]) > population
        ]
        if filtered_data:
            return JSONResponse(content=filtered_data)
        raise HTTPException(
            status_code=404, detail="No municipality found with the specified criteria."
        )
    except KeyError:
        raise HTTPException(
            status_code=400, detail="There's no data for the requested year."
        )


# Endpoint to get municipalities with IDHM greater than the specified value
@app.get("/municipality/idhm_higher_than/{idhm}")
def get_idhm(idhm: float):
    filtered_data = [item for item in data if float(item["IDHM 2010"]) > idhm]
    if filtered_data:
        return JSONResponse(content=filtered_data)
    raise HTTPException(status_code=404, detail="No municipality found.")


# Endpoint to get municipalities with IDHM lower than the specified value
@app.get("/municipality/idhm_lower_than/{idhm}")
def get_idhm(idhm: float):
    filtered_data = [item for item in data if float(item["IDHM 2010"]) < idhm]
    if filtered_data:
        return JSONResponse(content=filtered_data)
    raise HTTPException(status_code=404, detail="No municipality found.")


# Endpoint to get municipalities with population greater than the specified value and IDHM greater than the specified value in 2017
@app.get("/municipality/population/{population}/idhm/{idhm}")
def get_population_idhm(population: int, idhm: float):
    filtered_data = [
        item
        for item in data
        if int(item["Total population 2017"]) > population
        and float(item["IDHM 2010"]) > idhm
    ]
    if filtered_data:
        return JSONResponse(content=filtered_data)
    raise HTTPException(status_code=404, detail="No municipality found.")


# Endpoint to get municipalities with population greater than the specified value, IDHM greater than the specified value, for a given year
@app.get("/municipality/population/{population}/idhm/{idhm}/year/{year}")
def get_population_idhm_year(population: int, idhm: float, year: int):
    try:
        filtered_data = [
            item
            for item in data
            if int(item["Total population " + str(year)]) > population
            and float(item["IDHM 2010"]) > idhm
        ]
        if filtered_data:
            return JSONResponse(content=filtered_data)
        raise HTTPException(
            status_code=404, detail="No municipality found with the specified criteria."
        )
    except KeyError:
        raise HTTPException(
            status_code=400, detail="There's no data for the requested year."
        )
