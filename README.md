# FastAPI Municipality API

This FastAPI application provides endpoints to query Brazil's State Ceará municipalities data based on various criteria, including name, population and IDHM od different years, and starting character.

## Endpoints

### 1. Root Endpoint
- **URL**: `/`
- **Method**: `GET`
- **Description**: Returns all the data.

### 2. Get Municipality by Name
- **URL**: `/municipio/{item_name}`
- **Method**: `GET`
- **Description**: Retrieves a municipality by its name.
- **Parameters**:
  - `item_name` (str): The name of the municipality.
- **Response**:
  - The municipality data if found.
  - `"Município não encontrado."` if the municipality is not found.

### 3. Get Municipalities by Population
- **URL**: `/municipio/population/{population}`
- **Method**: `GET`
- **Description**: Retrieves municipalities with a population greater than the specified value in 2017.
- **Parameters**:
  - `population` (int): The population threshold.
- **Response**:
  - A list of municipalities matching the criteria.
  - `"Nenhum município encontrado com população maior que a informada."` if no municipalities match.

### 4. Get Municipalities Starting with a Specific Character
- **URL**: `/municipio/startswith/{char}`
- **Method**: `GET`
- **Description**: Retrieves municipalities that start with a specific character.
- **Parameters**:
  - `char` (str): The starting character.
- **Response**:
  - A list of municipalities matching the criteria.
  - `"Nenhum município encontrado."` if no municipalities match.

### 5. Get Municipalities by Population for a Given Year
- **URL**: `/municipio/population/{populacao}/year/{ano}`
- **Method**: `GET`
- **Description**: Retrieves municipalities with a population greater than the specified value for a given year.
- **Parameters**:
  - `populacao` (int): The population threshold.
  - `ano` (int): The year.
- **Response**:
  - A list of municipalities matching the criteria.
  - `"Nenhum município encontrado com população maior que a informada ou no ano reqisitado."` if no municipalities match.

### 6. Get Municipalities with IDHM Higher Than a Specified Value
- **URL**: `/municipio/idhm_higher_than/{idhm}`
- **Method**: `GET`
- **Description**: Retrieves municipalities with an IDHM greater than the specified value.
- **Parameters**:
  - `idhm` (float): The IDHM threshold.
- **Response**:
  - A list of municipalities matching the criteria.
  - `"Nenhum município encontrado com IDHM maior que o informado."` if no municipalities match.

### 7. Get Municipalities with IDHM Lower Than a Specified Value
- **URL**: `/municipio/idhm_lower_than/{idhm}`
- **Method**: `GET`
- **Description**: Retrieves municipalities with an IDHM lower than the specified value.
- **Parameters**:
  - `idhm` (float): The IDHM threshold.
- **Response**:
  - A list of municipalities matching the criteria.
  - `"Nenhum município encontrado com IDHM menor que o informado."` if no municipalities match.

### 8. Get Municipalities by Population and IDHM in 2017
- **URL**: `/municipio/population/{populacao}/idhm/{idhm}`
- **Method**: `GET`
- **Description**: Retrieves municipalities with a population greater than the specified value and an IDHM greater than the specified value in 2017.
- **Parameters**:
  - `populacao` (int): The population threshold.
  - `idhm` (float): The IDHM threshold.
- **Response**:
  - A list of municipalities matching the criteria.
  - `"Nenhum município encontrado com população maior que a informada ou IDHM maior que o informado."` if no municipalities match.

### 9. Get Municipalities by Population, IDHM, and Year
- **URL**: `/municipio/population/{populacao}/idhm/{idhm}/year/{ano}`
- **Method**: `GET`
- **Description**: Retrieves municipalities with a population greater than the specified value, an IDHM greater than the specified value, for a given year.
- **Parameters**:
  - `populacao` (int): The population threshold.
  - `idhm` (float): The IDHM threshold.
  - `ano` (int): The year.
- **Response**:
  - A list of municipalities matching the criteria.
  - `"Nenhum município encontrado com população maior que a informada, IDHM maior que o informado ou no ano reqisitado."` if no municipalities match.

### How to Run the Application

## Using Python Locally

## 1. Clone the Repository
- git clone https://your-repo-url 
- cd your-repo-directory

## 2. Install Dependencies:
- Ensure you have `fastapi` and `uvicorn` 
- installed. You can install them using 
- pip: pip install fastapi uvicorn

## 3. Run the application
- uvicorn main:app --reload

## 4. Access the Endpoints
- Once the application is running, access the endpoints by visiting http://127.0.0.1:8000/ in your web browser or using a tool like cURL or Postman.

## Using Docker
## 1. Clone the Repository:
- git clone https://your-repo-url
- cd your-repo-directory

## 2. Ensure Docker is Installed:
- Make sure you have Docker installed on your machine. You can download and install it from the Docker website.

## 3. Build the Docker Image:
- docker build -t my-fastapi-app .

## 4. Run the Docker Container:
- docker run -d -p 8000:8000 my-fastapi-app

## 5. Access the Endpoints:
- Once the application is running, access the endpoints by visiting http://localhost:8000/ in your web browser or using a tool like cURL or Postman.