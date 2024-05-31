import json
from fastapi import FastAPI
from fastapi.responses import JSONResponse

# Load the JSON data once at the start
with open('localization.json') as file:
    data = json.load(file)['Worksheet']
    
# Initialize FastAPI application
app = FastAPI()

# Root endpoint: returns all the data
@app.get("/")
def read_root():
    return data

# Endpoint to get a municipality by name
@app.get("/municipio/{item_name}")
def get_item(item_name: str):
    for item in data:
        if item['Nome'].lower() == item_name.lower():
            return item
    return "Município não encontrado."

# Endpoint to get municipalities with population greater than the specified value in 2017
@app.get("/municipio/population/{population}")
def get_population(populacao: int):
    filtered_data = [
        item for item in data if int(item["populacao total 2017"]) > populacao
    ]
    if filtered_data:
        return JSONResponse(content=filtered_data)
    return "Nenhum município encontrado com população maior que a informada."

# Endpoint to get municipalities that start with a specific character
@app.get("/municipio/startswith/{char}")
def get_municipio_by_char(char):
    filtered_data = [
        item for item in data if item["Nome"].lower().startswith(char.lower())
    ]
    if filtered_data:
        return JSONResponse(content=filtered_data)
    return "Nenhum município encontrado."

# Endpoint to get municipalities with population greater than the specified value for a given year
@app.get("/municipio/population/{populacao}/year/{ano}")
def get_population_year(populacao: int, ano: int):
    filtered_data = [
        item for item in data if int(item["populacao total " + str(ano)]) > populacao
    ]
    if filtered_data:
        return JSONResponse(content=filtered_data)
    return "Nenhum município encontrado com população maior que a informada ou no ano reqisitado."

# Endpoint to get municipalities with IDHM greater than the specified value
@app.get("/municipio/idhm_higher_than/{idhm}")
def get_idhm(idhm: float):
    filtered_data = [
        item for item in data if float(item["IDHM 2010"]) > idhm
    ]
    if filtered_data:
        return JSONResponse(content=filtered_data)
    return "Nenhum município encontrado com IDHM maior que o informado."

# Endpoint to get municipalities with IDHM lower than the specified value
@app.get("/municipio/idhm_lower_than/{idhm}")
def get_idhm(idhm: float):
    filtered_data = [
        item for item in data if float(item["IDHM 2010"]) < idhm
    ]
    if filtered_data:
        return JSONResponse(content=filtered_data)
    return "Nenhum município encontrado com IDHM menor que o informado."

# Endpoint to get municipalities with population greater than the specified value and IDHM greater than the specified value in 2017
@app.get("/municipio/population/{populacao}/idhm/{idhm}")
def get_population_idhm(populacao: int, idhm: float):
    filtered_data = [
        item for item in data if int(item["populacao total 2017"]) > populacao and float(item["IDHM 2010"]) > idhm
    ]
    if filtered_data:
        return JSONResponse(content=filtered_data)
    return "Nenhum município encontrado com população maior que a informada ou IDHM maior que o informado."

# Endpoint to get municipalities with population greater than the specified value, IDHM greater than the specified value, for a given year
@app.get("/municipio/population/{populacao}/idhm/{idhm}/year/{ano}")
def get_population_idhm_year(populacao: int, idhm: float, ano: int):
    filtered_data = [
        item for item in data if int(item["populacao total " + str(ano)]) > populacao and float(item["IDHM 2010"]) > idhm
    ]
    if filtered_data:
        return JSONResponse(content=filtered_data)
    return "Nenhum município encontrado com população maior que a informada, IDHM maior que o informado ou no ano reqisitado."
