import numpy as np
from hmmlearn import hmm

states = ['Sunny', 'Rainy']
observations = ['Umbrella', 'No Umbrella']

start_prob = np.array([0.5, 0.5])
transition_prob = np.array([[0.8, 0.2],
                            [0.3, 0.7]])

emission_prob = np.array([[0.2, 0.8],
                          [0.9, 0.1]])
observation_sequence = np.array([0, 1, 0, 1, 0, 1, 0, 1, 0]).reshape(-1, 1)

model = hmm.CategoricalHMM(n_components=2)
model.startprob_ = start_prob
model.transmat_ = transition_prob
model.emissionprob_ = emission_prob

# Predict the most likely sequence of states
logprob, hidden_states = model.decode(observation_sequence, algorithm="viterbi")

# Decode states to labels
hidden_state_labels = [states[state] for state in hidden_states]

print("Most likely sequence of hidden states:", hidden_state_labels)