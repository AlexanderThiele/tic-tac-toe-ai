from twisted.internet.defer import succeed
from klein import run, route
from twisted.web.static import File
import json
import neuralNetworkTrainer as nnt
import sys

@route('/', methods=['GET'], branch=True)
def home(request):
    return File("./tic-tac-toe")

@route('/api/tic-tac-toe', methods=['POST'])
def do_post(request):
    content = json.loads(request.content.read())
    move_data = map(float,content["move"]);
    print(move_data)

    nnMove = neuralNetwork.query(move_data)

    print(nnMove.ravel())
    response = json.dumps({"data":nnMove.ravel().tolist()})
    print(response)
    return response

def initNeuralNetwork():
    print("load & train model")
    global neuralNetwork
    neuralNetwork = nnt.NeuralNetworkTrainer()
    neuralNetwork.doTraining()
    print("neurals trained")
    return

initNeuralNetwork()
port = int(sys.argv[1]);
if(port == None):
    port = 8080;

run("0.0.0.0", port)
#run()
