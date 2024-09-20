import pyAgrum as gum

bn = gum.BayesNet('StudentAdmission')

exam = bn.add(gum.LabelizedVariable('exam', 'Exam Level', 2))  # e: {0: easy, 1: difficult}
iq = bn.add(gum.LabelizedVariable('iq', 'IQ Level', 2))        # i: {0: low, 1: high}
aptitude = bn.add(gum.LabelizedVariable('aptitude', 'Aptitude Score', 2))  # s: {0: low, 1: high}
marks = bn.add(gum.LabelizedVariable('marks', 'Marks', 2))     # m: {0: fail, 1: pass}
admission = bn.add(gum.LabelizedVariable('admission', 'Admission', 2))     # a: {0: not admitted, 1: admitted}

bn.addArc(exam, marks)
bn.addArc(iq, aptitude)
bn.addArc(iq, marks)
bn.addArc(marks, admission)

bn.cpt(exam).fillWith([0.7, 0.3])  # P(exam=0), P(exam=1)
bn.cpt(iq).fillWith([0.8, 0.2])    # P(iq=0), P(iq=1)
bn.cpt(aptitude)[{'iq': 0}] = [0.75, 0.25]
bn.cpt(aptitude)[{'iq': 1}] = [0.4, 0.6]
bn.cpt(marks)[{'exam': 0, 'iq': 0}] = [0.6, 0.4]
bn.cpt(marks)[{'exam': 0, 'iq': 1}] = [0.5, 0.5]
bn.cpt(marks)[{'exam': 1, 'iq': 0}] = [0.9, 0.1]
bn.cpt(marks)[{'exam': 1, 'iq': 1}] = [0.8, 0.2]
bn.cpt(admission)[{'marks': 0}] = [0.6, 0.4]
bn.cpt(admission)[{'marks': 1}] = [0.9, 0.1]

# Perform inference
model = gum.LazyPropagation(bn)

#case1: The student has low IQ, low Aptitude, the exam is difficult, and the student passed Calculate the probability of securing admission
model.setEvidence({'exam': 1, 'iq': 0, 'aptitude': 0, 'marks': 1})  # Evidence: Exam=1, IQ=0, Aptitude=0, Marks=1
model.makeInference()
prob_case1 = model.posterior('admission')[1]  # P(admission=1 | evidence)
print(f"Case 1: Probability of Admission (inference): {prob_case1:.2f}")

#case2: The student has high IQ, high Aptitude, the exam is easy but fails and does not secure admission
observation = {'exam': 0, 'iq': 1, 'aptitude': 1, 'marks': 0, 'admission': 0}  # Evidence: Exam=0, IQ=1, Aptitude=1, Marks=0, Admission=0
model.setEvidence(observation)
likelihood_case2 = model.evidenceProbability()
print(f"Case 2: Likelihood of Observation: {likelihood_case2:.2f}")