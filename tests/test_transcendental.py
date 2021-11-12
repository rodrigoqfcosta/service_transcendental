import requests as req

def getFatorial_calc(n1):
    param = {'arg1': int(n1)}
    res = req.get("http://localhost:5002/fatorial", param)
    data = res.json()

    return data["result"]

def test_function_fatorial():
    assert getFatorial_calc(5) == 120
