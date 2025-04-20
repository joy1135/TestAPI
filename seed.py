from sqlalchemy.orm import Session
from database import engine
import models as m

# Для создания бд
m.Base.metadata.drop_all(bind = engine)
m.Base.metadata.create_all(bind = engine)

with Session(bind = engine) as session:
    c1 = m.Category(name = "Еда", description='Вкусная, для людей')
    p1 = m.Product(name = "Молоко",categories=[c1])
    c2 = m.Category(name = "Электротехника")
    p2 = m.Product(name = "Телевизор", categories=[c2])
    session.add_all([p1, c1, c2, p2])

    g1 = m.Game(
        name = "Майнкрафт",
        description = "Веселая песочница",
        rating = 10
    )
    session.add(g1)
    g2 = m.Game(
        name = "Террария",
        description = "Веселая песочница с видом с боку",
        rating = 10
    )
    session.add(g2)

    session.commit()