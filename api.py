from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import sqlite3
import database

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

conn = sqlite3.connect("gastos.db", check_same_thread=False)
cursor = conn.cursor()

@app.get("/", response_class=HTMLResponse)
def home(request: Request):

    cursor.execute("SELECT * FROM gastos")
    gastos = cursor.fetchall()

    categorias = {}
    total = 0

    for gasto in gastos:
        monto = gasto[1]
        categoria = gasto[2]

        total += monto

        if categoria in categorias:
            categorias[categoria] += monto
        else:
            categorias[categoria] = monto

    cantidad_gastos = len(gastos)

    categoria_top = "N/A"

    if categorias:
        categoria_top = max(categorias, key=categorias.get)

    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "gastos": gastos,
            "categorias": categorias,
            "total": total,
            "cantidad_gastos": cantidad_gastos,
            "categoria_top": categoria_top
        }
    )

from fastapi.responses import RedirectResponse

@app.post("/agregar")
def agregar_gasto(monto: float = Form(...), categoria: str = Form(...)):
    cursor.execute(
        "INSERT INTO gastos (monto, categoria) VALUES (?, ?)",
        (monto, categoria)
    )

    conn.commit()

    return RedirectResponse("/", status_code=303)

@app.post("/eliminar/{id}")
def eliminar_gasto(id: int):
    cursor.execute("DELETE FROM gastos WHERE id = ?", (id,))
    conn.commit()

    return RedirectResponse("/", status_code=303)