import shutil
from fastapi import FastAPI, HTTPException, Depends, UploadFile
from database import get_db
from sqlalchemy.orm import Session
import models as m
from typing import List
import pyd

app = FastAPI()

@app.get("/product", response_model=List[pyd.ProductSchema])
def get_all_product(db:Session=Depends(get_db)):
    products = db.query(m.Product).all()
    return products

@app.get("/product/{product_id}", response_model=pyd.BaseProduct)
def get_product(product_id:int, db:Session=Depends(get_db)):
    product = db.query(m.Product).filter(
        m.Product.id == product_id
    ).first()
    if not product:
        raise HTTPException(404, 'Игра не найдена')
    return product

@app.get("/game", response_model=List[pyd.BaseGame])
def get_all_game(db:Session=Depends(get_db)):
    games = db.query(m.Game).all()
    return games

@app.get("/game/{game_id}", response_model=pyd.BaseGame)
def get_game(game_id:int, db:Session=Depends(get_db)):
    game = db.query(m.Game).filter(
        m.Game.id == game_id
    ).first()
    if not game:
        raise HTTPException(404, 'Игра не найдена')
    return game

# @app.post("/game", response_model=pyd.BaseGame)
# def create_game(product:pyd.CreateGame, db:Session=Depends(get_db)):
#     product_db = db.query(m.Product).filter(m.Product.name == product.name).first()
#     if product_db:
#         raise HTTPException(400, "Такой товар уже есть")
#     product_db = m.Product()
#     product_db.name = product.name
#     db.add(product_db)
#     db.commit()
#     return product_db

@app.post("/product", response_model=pyd.BaseProduct)
def create_product(product:pyd.CreateProduct, img: UploadFile, db:Session=Depends(get_db)):
    product_db = db.query(m.Product).filter(m.Product.name == product.name).first()
    if product_db:
        raise HTTPException(400, "Такой товар уже есть")
    if img.content_type not in ("image/png", "image/jpeg"):
        raise HTTPException(400, "Такой товар уже есть")
    with open(f"files/{img.filename}", "wb") as f:
        shutil.copyfileobj(img.file, f)
    product_db = m.Product()
    product_db.img = f"files/{img.filename}"
    product_db.name = product.name
    db.add(product_db)
    db.commit()
    return product_db

@app.post("/product/img/{product_id}", response_model=pyd.BaseProduct)
def create_product(product:pyd.CreateProduct, img: UploadFile, db:Session=Depends(get_db)):
    product_db = db.query(m.Product).filter(m.Product.name == product.name).first()
    if product_db:
        raise HTTPException(400, "Такой товар уже есть")    
    if img.content_type not in ("image/png", "image/jpeg"):
        raise HTTPException(400, "Такой товар уже есть")
    with open(f"files/{img.filename}", "wb") as f:
        shutil.copyfileobj(img.file, f)
    product_db = m.Product()
    product_db.img = f"files/{img.filename}"
    product_db.name = product.name
    db.add(product_db)
    db.commit()
    return product_db


@app.delete("/product/{product_id}")
def del_product(product_id:int, db:Session=Depends(get_db)):
    product = db.query(m.Product).filter(
        m.Product.id == product_id
    ).first()
    if not product:
        raise HTTPException(404, 'Товар не найден')
    db.delete(product)