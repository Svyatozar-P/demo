class Orders:
    def __init__(self, number, DateOfUpdate, TypeOfEquipment, model, description, client, phone, status):
        self.number = number
        self.DateOfUpdate = DateOfUpdate
        self.TypeOfEquipment = TypeOfEquipment
        self.model = model
        self.description = description
        self.client = client
        self.phone = phone
        self.status = status


from fastapi import Body, FastAPI
order = Orders(1, 30, 20, 123, 35, 67, 67, 89) 

repo = []
repo.append(order)

app = FastAPI()
 
@app.get("/")
def get_orders():
    return repo

@app.post("/")
def create_order(data = Body()):
    order = Orders(
        data["number"],
        data["DateOfUpdate"],
        data["TypeOfEquipment"],
        data["model"],
        data["description"],
        data["client"],
        data["phone"],
        data["status"]
    )
    repo.append(order)
    return order


@app.put("/{number}")
def update_order(number, dto = Body()):
    isEmpty = True
    for order in repo:
        if order.number == number:
            isEmpty = False 
            order.status = dto["status"]
            order.description = dto["description"]
            return order
    if isEmpty:
        return "нету"

@app.get("/{num}")
def getByNum(num):
    return [o for o in repo if o.number == int(num)][0]

@app.get("/filter/{param}")
def getByNum(param):
    return [o for o in repo if
            o.model == param or
            o.description == param or
            o.client == param or
            o.phone == param or
            o.status == param]