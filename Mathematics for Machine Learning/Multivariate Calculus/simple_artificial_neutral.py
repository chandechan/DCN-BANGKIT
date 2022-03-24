# First we set the state of the network
σ = np.tanh
w1 = 1.3
b1 = -0.1

# Then we define the neuron activation.
def a1(a0) :
  return σ(w1 * a0 + b1)
  
# Finally let's try the network out!
# Replace x with 0 or 1 below,
a1(0)

'''
# First set up the network.
sigma = np.tanh
sigma = np.tanh
W = np.array([[-2, 4, -1], [6, 0, -3]])
b = np.array([0.1, -2.5])
x = np.array([0.3, 0.4, 0.1])

c = np.matmul(W, x)
f = c + b
a1 = sigma(f)

'''