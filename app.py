from flask import Flask, jsonify, request
from flasgger import Swagger
from model import SimpleModel

app= Flask(__name__)
swagger = Swagger(app, template={
    "info": {
        "title": "Mesa Simulation API",
        "version": "1.0.0",
        "description": "Api for interacting with the Simple Model headless mesa model"
    }
})

model = SimpleModel(num_agents=10, width=10, height=10)


@app.route('/state', methods=['GET'])
def get_state():
    """
    return the current state without advancing time

    responses:
     200:
        description : A JSON object containg the current step and agent data
    """
    return (jsonify(model.get_stats()))

@app.route('/step', methods=['GET'])
def get_step():
    """
    advance the simulation by one step

    responses:
     200:
        description : A JSON object containing the updated step and agent data
    """
    model.step()
    return (jsonify(model.get_stats()))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
