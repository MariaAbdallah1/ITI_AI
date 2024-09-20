import pyAgrum as gum

# Create a Bayesian Network
bn = gum.BayesNet('TrainScheduling')

# Add nodes
rain = bn.add(gum.LabelizedVariable('rain', 'Rain', 3))
maintenance = bn.add(gum.LabelizedVariable('maintenance', 'Maintenance', 2))
train = bn.add(gum.LabelizedVariable('train', 'Train', 2))
appointment = bn.add(gum.LabelizedVariable('appointment', 'Appointment', 2))

# Add arcs
bn.addArc(rain, maintenance)
bn.addArc(rain, train)
bn.addArc(maintenance, train)
bn.addArc(train, appointment)

# Define the CPTs (Conditional Probability Tables)
bn.cpt(rain).fillWith([0.7, 0.2, 0.1])

bn.cpt(maintenance)[{'rain': 0}] = [0.4, 0.6] #[Yes, No]
bn.cpt(maintenance)[{'rain': 1}] = [0.2, 0.8]
bn.cpt(maintenance)[{'rain': 2}] = [0.1, 0.9]

bn.cpt(train)[{'rain': 0, 'maintenance': 0}] = [0.8, 0.2] #Ontime, Delayed
bn.cpt(train)[{'rain': 0, 'maintenance': 1}] = [0.9, 0.1]
bn.cpt(train)[{'rain': 1, 'maintenance': 0}] = [0.6, 0.4]
bn.cpt(train)[{'rain': 1, 'maintenance': 1}] = [0.7, 0.3]
bn.cpt(train)[{'rain': 2, 'maintenance': 0}] = [0.4, 0.6]
bn.cpt(train)[{'rain': 2, 'maintenance': 1}] = [0.5, 0.5]

bn.cpt(appointment)[{'train': 0}] = [0.9, 0.1] #attend, miss
bn.cpt(appointment)[{'train': 1}] = [0.6, 0.4]

# Perform inference
model = gum.LazyPropagation(bn)
model.makeInference()

#liklihood
# # Calculate probability for a given observation
observation = {"rain": 0, "maintenance": 1, "train": 0, "appointment": 0}
model.setEvidence(observation)
probability = model.evidenceProbability()
print(f"Probability of the observation {observation}: {probability}")

#Inference
model.setEvidence({'train': 1,
                   'maintenance':0})  # 'delayed' is index 1 in the train variable

# Calculate predictions for each node
nodes = bn.names()
#prediction= probability distribution For all nodes{Rain, Maint, Train, Appoiment} model.posterior('appoinment') P(Appoiment|Train=delayed)
predictions = {node: model.posterior(node) for node in nodes if node != 'train'}

# Print predictions for each node
for node, prediction in predictions.items():
    print(f"{node}:")
    for i, value in enumerate(bn.variable(node).labels()):
        probability = prediction[i]
        print(f"    {value}: {probability:.4f}")