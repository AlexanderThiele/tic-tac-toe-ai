import neuralNetwork as nn
import numpy

input_nodes = 9
hidden_nodes = 9
output_nodes = 9
learning_rate = 0.3

class NeuralNetworkTrainer:
    def __init__(self):
        self.n = nn.NeuralNetwork(input_nodes, hidden_nodes, output_nodes, learning_rate)

    def trainRound(self):
        n.train([0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 0]);
        n.train([0, 0, 0, 0, 0, -1, 0, 1, 0], [0, 0, 0, 0, 1, 0, 0, 0, 0]);
        n.train([0, -1, 0, 0, 1, -1, 0, 1, 0], [0, 0, 0, 0, 0, 0, 1, 0, 0]);
        n.train([0, -1, -1, 0, 1, -1, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 1]);
        n.train([0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 0]);
        n.train([0, 0, 0, 0, 0, -1, 0, 1, 0], [0, 0, 0, 0, 1, 0, 0, 0, 0]);
        n.train([0, -1, 0, 0, 1, -1, 0, 1, 0], [0, 0, 0, 0, 0, 0, 1, 0, 0]);
        n.train([0, -1, -1, 0, 1, -1, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 1]);
        n.train([0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0, 0, 0, 0]);
        n.train([0, 0, 1, 0, -1, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0, 0, 0]);
        n.train([-1, 1, 1, 0, -1, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 1]);
        n.train([-1, 1, 1, 0, -1, -1, 0, 0, 1], [0, 0, 0, 1, 0, 0, 0, 0, 0]);
        n.train([-1, 1, 1, 1, -1, -1, 0, -1, 1], [0, 0, 0, 0, 0, 0, 1, 0, 0]);
        n.train([0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 1]);
        n.train([0, 0, 0, 0, -1, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0, 1, 0]);
        n.train([0, 0, 0, 0, -1, 0, -1, 1, 1], [0, 0, 1, 0, 0, 0, 0, 0, 0]);
        n.train([0, 0, 1, 0, -1, -1, -1, 1, 1], [0, 0, 0, 1, 0, 0, 0, 0, 0]);
        n.train([0, -1, 1, 1, -1, -1, -1, 1, 1], [1, 0, 0, 0, 0, 0, 0, 0, 0]);
        n.train([0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 1, 0, 0]);
        n.train([0, 0, 0, 0, 0, 0, 1, -1, 0], [0, 0, 0, 0, 1, 0, 0, 0, 0]);
        n.train([0, 0, -1, 0, 1, 0, 1, -1, 0], [0, 0, 0, 0, 0, 1, 0, 0, 0]);
        n.train([0, 0, -1, -1, 1, 1, 1, -1, 0], [0, 1, 0, 0, 0, 0, 0, 0, 0]);
        n.train([-1, 1, -1, -1, 1, 1, 1, -1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 1]);
        n.train([0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0, 0]);
        n.train([0, 0, 0, 0, 1, -1, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0, 0, 0]);
        n.train([0, 1, 0, 0, 1, -1, 0, -1, 0], [0, 0, 1, 0, 0, 0, 0, 0, 0]);
        n.train([0, 1, 1, 0, 1, -1, -1, -1, 0], [0, 0, 0, 1, 0, 0, 0, 0, 0]);
        n.train([-1, 1, 1, 1, 1, -1, -1, -1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 1]);
        n.train([0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0, 0, 0, 0]);
        n.train([0, 0, 1, 0, 0, -1, 0, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0, 0]);
        n.train([0, 0, 1, 0, 1, -1, 0, -1, 0], [0, 0, 0, 0, 0, 0, 1, 0, 0]);
        n.train([0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0, 0, 0, 0]);
        n.train([0, 0, 1, 0, -1, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0, 0]);
        n.train([0, 0, 1, 0, -1, 1, 0, 0, -1], [0, 0, 0, 0, 0, 0, 0, 1, 0]);
        n.train([0, 0, 1, 0, -1, 1, -1, 1, -1], [0, 0, 0, 1, 0, 0, 0, 0, 0]);
        n.train([0, -1, 1, 1, -1, 1, -1, 1, -1], [1, 0, 0, 0, 0, 0, 0, 0, 0]);
        n.train([0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0, 0]);
        n.train([1, 0, 0, 0, 0, -1, 0, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0, 0]);
        n.train([1, 0, 0, 0, 1, -1, 0, 0, -1], [0, 1, 0, 0, 0, 0, 0, 0, 0]);
        n.train([1, 1, 0, 0, 1, -1, 0, -1, -1], [0, 0, 1, 0, 0, 0, 0, 0, 0]);
        n.train([0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0, 0]);
        n.train([1, -1, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0, 0]);
        n.train([1, -1, 0, 0, 1, 0, 0, 0, -1], [0, 0, 0, 0, 0, 1, 0, 0, 0]);
        n.train([1, -1, -1, 0, 1, 1, 0, 0, -1], [0, 0, 0, 1, 0, 0, 0, 0, 0]);
        n.train([0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0, 0, 0]);
        n.train([0, 1, -1, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0, 0]);
        n.train([0, 1, -1, 0, 1, 0, 0, -1, 0], [0, 0, 0, 0, 0, 0, 1, 0, 0]);
        n.train([0, 1, -1, 0, 1, -1, 1, -1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 1]);
        n.train([0, 1, -1, -1, 1, -1, 1, -1, 1], [1, 0, 0, 0, 0, 0, 0, 0, 0]);
        n.train([0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0, 0, 0, 0]);
        n.train([0, 0, 1, 0, 0, -1, 0, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0, 0]);
        n.train([0, 0, 1, 0, 1, -1, 0, -1, 0], [0, 0, 0, 0, 0, 0, 1, 0, 0]);
        n.train([0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0, 0, 0]);
        n.train([0, 0, 0, 1, -1, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 0]);
        n.train([0, 0, 0, 1, -1, 0, -1, 1, 0], [0, 0, 1, 0, 0, 0, 0, 0, 0]);
        n.train([-1, 0, 1, 1, -1, 0, -1, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 1]);
        n.train([-1, 0, 1, 1, -1, -1, -1, 1, 1], [0, 1, 0, 0, 0, 0, 0, 0, 0]);
        n.train([0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0, 0, 0]);
        n.train([0, -1, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 0]);
        n.train([0, -1, 0, 1, -1, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0, 1, 0, 0]);
        n.train([-1, -1, 0, 1, -1, 0, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 1]);
        n.train([0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0, 0, 0, 0]);
        n.train([0, -1, 1, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0, 0]);
        n.train([0, -1, 1, 0, 1, 0, -1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 1]);
        n.train([-1, -1, 1, 0, 1, 0, -1, 0, 1], [0, 0, 0, 0, 0, 1, 0, 0, 0]);
        n.train([0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0, 0, 0, 0]);
        n.train([0, 0, 1, 0, -1, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0, 0, 0]);
        n.train([-1, 1, 1, 0, -1, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0, 0]);
        n.train([-1, 1, 1, 0, -1, 1, 0, -1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 1]);
        n.train([0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0, 0, 0, 0]);
        n.train([0, 0, 1, 0, -1, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0, 0, 0]);
        n.train([-1, 1, 1, 0, -1, 0, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0, 0, 0]);
        n.train([-1, 1, 1, 1, -1, -1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 1, 0, 0]);
        n.train([0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0, 0, 0, 0]);
        n.train([-1, 0, 1, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 1, 0, 0]);
        n.train([-1, 0, 1, 0, -1, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 1]);
        n.train([-1, 0, 1, 0, -1, 0, 1, -1, 1], [0, 0, 0, 0, 0, 1, 0, 0, 0]);
        n.train([0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0, 0, 0, 0]);
        n.train([-1, 0, 1, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0, 0]);
        n.train([-1, 0, 1, 0, 1, 0, -1, 0, 0], [0, 0, 0, 1, 0, 0, 0, 0, 0]);
        n.train([-1, 0, 1, 1, 1, -1, -1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 0]);
        n.train([-1, -1, 1, 1, 1, -1, -1, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 1]);
        n.train([0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0, 0, 0, 0]);
        n.train([0, -1, 1, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0, 0]);
        n.train([0, -1, 1, 0, 1, 0, -1, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0, 0]);
        n.train([0, -1, 1, 0, 1, 1, -1, 0, -1], [0, 0, 0, 1, 0, 0, 0, 0, 0]);
        n.train([0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 1, 0, 0]);
        n.train([0, 0, 0, 0, -1, 0, 1, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0, 0]);
        n.train([1, 0, 0, -1, -1, 0, 1, 0, 0], [0, 1, 0, 0, 0, 0, 0, 0, 0]);
        n.train([1, 1, -1, -1, -1, 0, 1, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0, 0]);
        n.train([1, 1, -1, -1, -1, 1, 1, -1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 1]);
        pass

    def trainRound2(self):
        self.n.train([0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0, 0, 0]);
        self.n.train([0, 1, 0, 0, 0, -1, 0, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0, 0]);
        self.n.train([0, 1, 0, 0, 1, -1, 0, -1, 0], [0, 0, 1, 0, 0, 0, 0, 0, 0]);
        self.n.train([-1, 1, 1, 0, 1, -1, 0, -1, 0], [0, 0, 0, 0, 0, 0, 1, 0, 0]);
        self.n.train([0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0, 0, 0]);
        self.n.train([0, 1, 0, 0, 0, -1, 0, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0, 0]);
        self.n.train([0, 1, 0, 0, 1, -1, 0, -1, 0], [0, 0, 1, 0, 0, 0, 0, 0, 0]);
        self.n.train([0, 1, 1, 0, 1, -1, -1, -1, 0], [1, 0, 0, 0, 0, 0, 0, 0, 0]);
        self.n.train([0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0, 0, 0]);
        self.n.train([0, 1, 0, 0, -1, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 1, 0, 0]);
        self.n.train([0, 1, 0, 0, -1, -1, 1, 0, 0], [0, 0, 0, 1, 0, 0, 0, 0, 0]);
        self.n.train([-1, 1, 0, 1, -1, -1, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 1]);
        self.n.train([-1, 1, 0, 1, -1, -1, 1, -1, 1], [0, 0, 1, 0, 0, 0, 0, 0, 0]);
        self.n.train([0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0, 0, 0]);
        self.n.train([0, 1, 0, -1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0, 0]);
        self.n.train([0, 1, 0, -1, 1, 0, 0, -1, 0], [0, 0, 1, 0, 0, 0, 0, 0, 0]);
        self.n.train([0, 1, 1, -1, 1, 0, -1, -1, 0], [1, 0, 0, 0, 0, 0, 0, 0, 0]);
        self.n.train([0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0, 0, 0]);
        self.n.train([0, 1, 0, 0, -1, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0, 0]);
        self.n.train([0, 1, 0, 0, -1, 1, -1, 0, 0], [0, 0, 1, 0, 0, 0, 0, 0, 0]);
        self.n.train([0, 1, 1, 0, -1, 1, -1, 0, -1], [1, 0, 0, 0, 0, 0, 0, 0, 0]);
        self.n.train([0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0, 0, 0]);
        self.n.train([0, 1, 0, 0, 0, 0, -1, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0, 0]);
        self.n.train([0, 1, 0, 0, 1, 0, -1, -1, 0], [1, 0, 0, 0, 0, 0, 0, 0, 0]);
        self.n.train([0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0, 0, 0]);
        self.n.train([0, 1, 0, 0, 0, 0, 0, -1, 0], [0, 0, 0, 1, 0, 0, 0, 0, 0]);
        self.n.train([0, 1, 0, 1, -1, 0, 0, -1, 0], [1, 0, 0, 0, 0, 0, 0, 0, 0]);
        self.n.train([1, 1, 0, 1, -1, 0, -1, -1, 0], [0, 0, 1, 0, 0, 0, 0, 0, 0]);
        self.n.train([0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0, 0, 0]);
        self.n.train([0, 1, -1, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 1, 0, 0]);
        self.n.train([0, 1, -1, 0, 0, -1, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 1]);
        self.n.train([0, 1, -1, 0, -1, -1, 1, 0, 1], [0, 0, 0, 1, 0, 0, 0, 0, 0]);
        self.n.train([-1, 1, -1, 1, -1, -1, 1, 0, 1], [0, 0, 0, 0, 0, 0, 0, 1, 0]);
        self.n.train([0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0, 0, 0]);
        self.n.train([0, 1, 0, 0, 0, 0, 0, 0, -1], [0, 0, 0, 0, 1, 0, 0, 0, 0]);
        self.n.train([0, 1, 0, 0, 1, 0, 0, -1, -1], [0, 0, 0, 0, 0, 0, 1, 0, 0]);
        self.n.train([0, 1, -1, 0, 1, 0, 1, -1, -1], [0, 0, 0, 1, 0, 0, 0, 0, 0]);
        self.n.train([-1, 1, -1, 1, 1, 0, 1, -1, -1], [0, 0, 0, 0, 0, 1, 0, 0, 0]);
        self.n.train([0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0, 0, 0]);
        self.n.train([0, 1, 0, 0, -1, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0, 0]);
        self.n.train([0, 1, 0, 0, -1, 1, -1, 0, 0], [0, 0, 1, 0, 0, 0, 0, 0, 0]);
        self.n.train([0, 1, 1, 0, -1, 1, -1, 0, -1], [1, 0, 0, 0, 0, 0, 0, 0, 0]);
        pass

    def doTraining(self):
        for i in range(1000):
            self.trainRound2();
            if(i%100 == 0):
                print(i);
        pass

    def query(self, data):
        return numpy.transpose(self.n.query(data))

#print(n.query(numpy.random.rand(hidden_nodes, input_nodes)));
#print(n.query([0,0,0,0,0,0,0,0,0]))
#print(n.query([0, 1, 0, 0, -1, 0, 0, 0, 0]))
#print(n.query([0, 1, 0, 0, -1, 1, -1, 0, 0]))
#print(n.query([0, 1, 1, 0, -1, 1, -1, 0, -1]))
#print(n.query())
#n.showW();
