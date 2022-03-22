

# First we set the state of the network
σ = np.tanh
w1 = 1.3
b1 = -0.1

# Then we define the neuron activation.
def a1(a0) :
  z = w1 * a0 + b1
  return σ(z)

# Experiment with different values of x below.
x = 0
a1(x)

answer = 1.2

'''

'''
