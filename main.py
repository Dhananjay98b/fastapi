from fastapi import FastAPI,HTTPException

app = FastAPI()

@app.get('/')
def root_url():
    return {'message':'welcome to the fastapi'}

@app.get('/sub')
def root_url():
    return {'message':'welcome to the fastapi internal page'}

users = {
    1:{
        "name":"mani",
        "orders":{
            1:{"item1":"laptop","amount":4566},
            2:{"item2":"top","amount":566},
    }
    },
    2:{
        "name":"kiran",
        "orders":{
            1:{"item1":"lap","amount":456},
            2:{"item2":"tops","amount":66},
    }},
    3:{"name":"praveen"}}

@app.get('/user/{user_id}/order/{order_id}')
def get_users(user_id:int,order_id:int):
    if user_id not in users:
        raise HTTPException(status_code =404, details ="product id not found")
    return users[user_id]['orders'][order_id]
