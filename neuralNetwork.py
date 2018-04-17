import numpy
import scipy.special

class NeuralNetwork:
    def __init__(self, inputnodes, hiddennotes, outputnodes, learningrate):
        self.inodes = inputnodes
        self.hnodes = hiddennotes
        self.onodes = outputnodes

        self.lr = learningrate

        self.wih = (numpy.random.rand(self.hnodes, self.inodes)-0.5)
        self.who = (numpy.random.rand(self.onodes, self.hnodes)-0.5)

        self.activation_function = lambda x: scipy.special.expit(x)

        #print(self.wih)

        #print (self.wih)
        pass

    def train(self, inputs_list, targets_list):

        inputs = numpy.array(inputs_list, ndmin=2).T
        targets = numpy.array(targets_list, ndmin=2).T

        hidden_inputs = numpy.dot(self.wih, inputs)
        hidden_outputs = self.activation_function(hidden_inputs);

        final_inputs = numpy.dot(self.who, hidden_outputs)
        final_outputs = self.activation_function(final_inputs);

        output_errors = targets - final_outputs

        hidden_errors = numpy.dot(self.who.T, output_errors)

        self.who += self.lr * numpy.dot((output_errors * final_outputs * (1.0 - final_outputs)), numpy.transpose(hidden_outputs))
        self.wih += self.lr * numpy.dot((hidden_errors * hidden_outputs * (1.0 - hidden_outputs)), numpy.transpose(inputs))
        pass

    def query(self, inputs_list):

        inputs = numpy.array(inputs_list, ndmin=2).T

        #print(self.wih)
        #print(inputs)

        hidden_inputs = numpy.dot(self.wih, inputs)
        hidden_outputs = self.activation_function(hidden_inputs);

        #print("---")
        #print(hidden_inputs)
        #print(self.who)
        #print(hidden_outputs)
        final_inputs = numpy.dot(self.who, hidden_outputs)
        final_outputs = self.activation_function(final_inputs);
        return final_outputs

    def showW(self):
        print("wih:")
        print(self.wih)
        print("who")
        print(self.who)
        pass
