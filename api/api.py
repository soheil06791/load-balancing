from sanic import Sanic, response

app = Sanic("Api")

aggregate= {}
async def request_food(request):
    if 'client-key' not in dict(request.headers):
        return response.json({"state": aggregate})
    if dict(request.headers)['client-key'] not in aggregate:
        aggregate[dict(request.headers)['client-key']] = 0
    aggregate[dict(request.headers)['client-key']] += 1
    return response.json({"state": aggregate})


if __name__ == "__main__":
    app.add_route(request_food, "/", methods=["GET"])
    app.run(host="0.0.0.0", port=8080)
