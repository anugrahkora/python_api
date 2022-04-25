from fastapi import FastAPI

app = FastAPI()
tle = {
    1: "1 25544U 98067A   22113.52489120  .00011770  00000+0  21220-3 0  9995",
    2: "2 25544  51.6421 247.3034 0005299  49.4166  72.3404 15.50220861336708"
}


@app.get("/home")
def home():
    return {"Data": "Home"}


@app.get("/")
def root():
    return {"Data": "root"}


@app.get("/location/{tle_line}")
def location(tle_line: int):
    return tle[tle_line]
