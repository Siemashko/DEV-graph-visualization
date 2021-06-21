import json

with open('philosophers.json', 'r') as f:
    raw = json.load(f)

with open('philo.json', 'r') as f:
    transformed = json.load(f)

node_list = raw['people']


closeness_centrality = {'Thales': 0.27314814814814814,
 'Anaximander': 0.21572212065813529,
 'Anaximenes': 0.17771084337349397,
 'Parmenides': 0.36990595611285265,
 'Heraclitus': 0.38562091503267976,
 'Empedocles': 0.2706422018348624,
 'Leucippus & Democritus': 0.35542168674698793,
 'Xenophanes': 0.3722397476340694,
 'Socrates': 0.38562091503267976,
 'Plato': 0.5108225108225108,
 'Pythagoras': 0.3390804597701149,
 'Aristotle': 0.5042735042735043,
 'Diogenes': 0.3232876712328767,
 'Pyrrho': 0.39730639730639733,
 'Epicurus': 0.4259927797833935,
 'Stoics (Zeno of Citium et al)': 0.4,
 'Timon of Phlius': 0.36085626911314983,
 'Plotinus': 0.367601246105919,
 'Saint Augustine': 0.4796747967479675,
 'John Scotus Erigena': 0.3769968051118211,
 'Thomas Aquinas': 0.4645669291338583,
 'Saint Anselm': 0.39864864864864863,
 'William of Ockham': 0.44528301886792454,
 'Francis Bacon': 0.4125874125874126,
 'Thomas Hobbes': 0.4957983193277311,
 'Zeno of Elea': 0.35435435435435436,
 'René Descartes': 0.502127659574468,
 'Benedict Spinoza': 0.5291479820627802,
 'John Locke': 0.5108225108225108,
 'Anne Conway': 0.44029850746268656,
 'Gottfried Wilhelm Leibniz': 0.48360655737704916,
 'George Berkeley': 0.41114982578397213,
 'Francis Hutcheson': 0.4306569343065693,
 'David Hume': 0.5244444444444445,
 'Jean-Jacques Rousseau': 0.45038167938931295,
 'Edmund Burke': 0.41114982578397213,
 'Immanuel Kant': 0.5488372093023256,
 'Jeremy Bentham': 0.4229390681003584,
 'Mary Wollstonecraft': 0.4013605442176871,
 'Johann Gottlieb Fichte': 0.44360902255639095,
 'Friedrich Schelling': 0.43223443223443225,
 'Georg Wilhelm Friedrich Hegel': 0.4738955823293173,
 'Arthur Schopenhauer': 0.4816326530612245,
 'Ludwig Feuerbach': 0.4306569343065693,
 'John Stuart Mill': 0.4738955823293173,
 'Charles Darwin': 0.47580645161290325,
 'Søren Kierkegaard': 0.41114982578397213,
 'Karl Marx': 0.4290909090909091,
 'Charles Sanders Peirce': 0.4419475655430712,
 'William James': 0.36875,
 'Friedrich Nietzsche': 0.43223443223443225,
 'Gottlob Frege': 0.3933333333333333,
 'Sigmund Freud': 0.5130434782608696,
 'Ferdinand de Saussure': 0.4645669291338583,
 'Edmund Husserl': 0.4068965517241379,
 'Henri Bergson': 0.4573643410852713,
 'John Dewey': 0.43866171003717475,
 'Pierre Duhem': 0.3959731543624161,
 'Bertrand Russell': 0.4609375,
 'George Edward Moore': 0.4154929577464789,
 'Ludwig Wittgenstein': 0.49166666666666664,
 'Martin Heidegger': 0.42142857142857143,
 'Georges Bataille': 0.40273037542662116,
 'Rudolf Carnap': 0.4083044982698962,
 'Carl Hempel': 0.36990595611285265,
 'Karl Popper': 0.466403162055336,
 'Gilbert Ryle': 0.4419475655430712,
 'Frank Ramsey': 0.2706422018348624,
 'Jacques Lacan': 0.4338235294117647,
 'Theodor Adorno': 0.466403162055336,
 'Hannah Arendt': 0.46825396825396826,
 'Jean-Paul Sartre': 0.37942122186495175,
 'Simone de Beauvoir': 0.4169611307420495,
 'Albert Camus': 0.3575757575757576,
 'Maurice Merleau-Ponty': 0.39072847682119205,
 'Alfred Jules Ayer': 0.4419475655430712,
 'John Langshaw Austin': 0.4354243542435424,
 'Willard Van Orman Quine': 0.4591439688715953,
 'William Frankena': 0.39864864864864863,
 'Wilfred Sellars': 0.41843971631205673,
 'Sir Peter Strawson': 0.44360902255639095,
 'Paul Grice': 0.3480825958702065,
 'Elizabeth Anscombe': 0.39730639730639733,
 'Peter Winch': 0.3818770226537217,
 'Donald Davidson': 0.45384615384615384,
 'Abraham Irving Melden': 0.3630769230769231,
 'John Mackie': 0.3818770226537217,
 'Richard Hare': 0.44696969696969696,
 'Philippa Foot': 0.30971128608923887,
 'John Rawls': 0.4259927797833935,
 'Thomas Kuhn': 0.42142857142857143,
 'Paul Feyerabend': 0.36990595611285265,
 'Michel Foucault': 0.4083044982698962,
 'Jean-François Lyotard': 0.4573643410852713,
 'Michael Dummett': 0.39072847682119205,
 'Hilary Putnam': 0.44866920152091255,
 'Bernard Williams': 0.44029850746268656,
 'Jean Baudrillard': 0.4199288256227758,
 'Harry Frankfurt': 0.35542168674698793,
 'Jacques Derrida': 0.3881578947368421,
 'Richard Rorty': 0.4154929577464789,
 'Luce Irigaray': 0.41114982578397213,
 'John Searle': 0.41843971631205673,
 'Jerry Fodor': 0.4,
 'Thomas Nagel': 0.4097222222222222,
 'Sandra Harding': 0.3522388059701492,
 'Carol Gilligan': 0.3630769230769231,
 'Robert Nozick': 0.39730639730639733,
 'Saul Kripke': 0.3920265780730897,
 'Frank Jackson': 0.36645962732919257,
 'David Lewis': 0.427536231884058,
 'John McDowell': 0.4125874125874126,
 'Richard Boyd': 0.38436482084690554,
 'Tim Scanlon': 0.3532934131736527,
 'Richard Dawkins': 0.38943894389438943,
 'Daniel Dennett': 0.5130434782608696,
 'Simon Blackburn': 0.3564954682779456,
 'Judith Butler': 0.40273037542662116,
 'David Chalmers': 0.44360902255639095}

degree_centrality = {'Thales': 0.01694915254237288,
 'Anaximander': 0.01694915254237288,
 'Anaximenes': 0.00847457627118644,
 'Parmenides': 0.05084745762711865,
 'Heraclitus': 0.0423728813559322,
 'Empedocles': 0.00847457627118644,
 'Leucippus & Democritus': 0.03389830508474576,
 'Xenophanes': 0.0423728813559322,
 'Socrates': 0.1016949152542373,
 'Plato': 0.4491525423728814,
 'Pythagoras': 0.01694915254237288,
 'Aristotle': 0.2542372881355932,
 'Diogenes': 0.01694915254237288,
 'Pyrrho': 0.05084745762711865,
 'Epicurus': 0.1440677966101695,
 'Stoics (Zeno of Citium et al)': 0.0847457627118644,
 'Timon of Phlius': 0.025423728813559324,
 'Plotinus': 0.0423728813559322,
 'Saint Augustine': 0.211864406779661,
 'John Scotus Erigena': 0.03389830508474576,
 'Thomas Aquinas': 0.1440677966101695,
 'Saint Anselm': 0.03389830508474576,
 'William of Ockham': 0.13559322033898305,
 'Francis Bacon': 0.06779661016949153,
 'Thomas Hobbes': 0.2796610169491525,
 'Zeno of Elea': 0.01694915254237288,
 'René Descartes': 0.3050847457627119,
 'Benedict Spinoza': 0.3474576271186441,
 'John Locke': 0.3728813559322034,
 'Anne Conway': 0.1694915254237288,
 'Gottfried Wilhelm Leibniz': 0.22033898305084745,
 'George Berkeley': 0.11016949152542373,
 'Francis Hutcheson': 0.11016949152542373,
 'David Hume': 0.3220338983050847,
 'Jean-Jacques Rousseau': 0.17796610169491525,
 'Edmund Burke': 0.09322033898305085,
 'Immanuel Kant': 0.4491525423728814,
 'Jeremy Bentham': 0.07627118644067797,
 'Mary Wollstonecraft': 0.09322033898305085,
 'Johann Gottlieb Fichte': 0.11016949152542373,
 'Friedrich Schelling': 0.1271186440677966,
 'Georg Wilhelm Friedrich Hegel': 0.3220338983050847,
 'Arthur Schopenhauer': 0.2627118644067797,
 'Ludwig Feuerbach': 0.1440677966101695,
 'John Stuart Mill': 0.17796610169491525,
 'Charles Darwin': 0.2033898305084746,
 'Søren Kierkegaard': 0.13559322033898305,
 'Karl Marx': 0.2627118644067797,
 'Charles Sanders Peirce': 0.1694915254237288,
 'William James': 0.025423728813559324,
 'Friedrich Nietzsche': 0.2288135593220339,
 'Gottlob Frege': 0.06779661016949153,
 'Sigmund Freud': 0.3728813559322034,
 'Ferdinand de Saussure': 0.2288135593220339,
 'Edmund Husserl': 0.07627118644067797,
 'Henri Bergson': 0.13559322033898305,
 'John Dewey': 0.16101694915254236,
 'Pierre Duhem': 0.059322033898305086,
 'Bertrand Russell': 0.1694915254237288,
 'George Edward Moore': 0.0847457627118644,
 'Ludwig Wittgenstein': 0.3898305084745763,
 'Martin Heidegger': 0.15254237288135594,
 'Georges Bataille': 0.1271186440677966,
 'Rudolf Carnap': 0.11016949152542373,
 'Carl Hempel': 0.07627118644067797,
 'Karl Popper': 0.2033898305084746,
 'Gilbert Ryle': 0.1694915254237288,
 'Frank Ramsey': 0.00847457627118644,
 'Jacques Lacan': 0.22033898305084745,
 'Theodor Adorno': 0.3389830508474576,
 'Hannah Arendt': 0.1864406779661017,
 'Jean-Paul Sartre': 0.17796610169491525,
 'Simone de Beauvoir': 0.1864406779661017,
 'Albert Camus': 0.059322033898305086,
 'Maurice Merleau-Ponty': 0.0423728813559322,
 'Alfred Jules Ayer': 0.11016949152542373,
 'John Langshaw Austin': 0.22033898305084745,
 'Willard Van Orman Quine': 0.211864406779661,
 'William Frankena': 0.0423728813559322,
 'Wilfred Sellars': 0.11864406779661017,
 'Sir Peter Strawson': 0.13559322033898305,
 'Paul Grice': 0.0423728813559322,
 'Elizabeth Anscombe': 0.1016949152542373,
 'Peter Winch': 0.059322033898305086,
 'Donald Davidson': 0.17796610169491525,
 'Abraham Irving Melden': 0.025423728813559324,
 'John Mackie': 0.059322033898305086,
 'Richard Hare': 0.1271186440677966,
 'Philippa Foot': 0.01694915254237288,
 'John Rawls': 0.1271186440677966,
 'Thomas Kuhn': 0.1694915254237288,
 'Paul Feyerabend': 0.05084745762711865,
 'Michel Foucault': 0.2033898305084746,
 'Jean-François Lyotard': 0.1864406779661017,
 'Michael Dummett': 0.09322033898305085,
 'Hilary Putnam': 0.17796610169491525,
 'Bernard Williams': 0.1271186440677966,
 'Jean Baudrillard': 0.17796610169491525,
 'Harry Frankfurt': 0.00847457627118644,
 'Jacques Derrida': 0.1016949152542373,
 'Richard Rorty': 0.11864406779661017,
 'Luce Irigaray': 0.1864406779661017,
 'John Searle': 0.1440677966101695,
 'Jerry Fodor': 0.0847457627118644,
 'Thomas Nagel': 0.06779661016949153,
 'Sandra Harding': 0.025423728813559324,
 'Carol Gilligan': 0.025423728813559324,
 'Robert Nozick': 0.07627118644067797,
 'Saul Kripke': 0.07627118644067797,
 'Frank Jackson': 0.05084745762711865,
 'David Lewis': 0.11016949152542373,
 'John McDowell': 0.0847457627118644,
 'Richard Boyd': 0.0423728813559322,
 'Tim Scanlon': 0.0847457627118644,
 'Richard Dawkins': 0.07627118644067797,
 'Daniel Dennett': 0.4152542372881356,
 'Simon Blackburn': 0.025423728813559324,
 'Judith Butler': 0.16101694915254236,
 'David Chalmers': 0.22033898305084745}

for item in node_list:
    item['id'] = item['name']
    time = item["time"]
    if time[-2:] == "BC":
        if time == "5th century BC":
            born = 500
            died = 401
        else:
            born, died = time[:-3].split("–")
        born, died = -int(born), -int(died)
    else:
        dates = time.split("–")
        if len(dates) > 1:
            born, died = dates[0], dates[1]
        else:
            born, died = dates[0], None
    item['born'] = born
    item['died'] = died
    item.pop('time')
    item['degree_centrality'] = degree_centrality[item['id']]
    item['closeness_centrality'] = closeness_centrality[item['id']]


transformed['nodes'] = node_list

links = {}

for link in transformed['links']:
    source, target = link['source'], link['target']
    if source not in links:
        links[source] = {}
    if target not in links:
        links[target] = {}
    if target not in links[source]:
        links[source][target] = 0
    if source not in links[target]:
        links[target][source] = 0
    update = 1 if link['label'] == 'p' else -1
    links[target][source] = links[target][source] + update
    links[source][target] = links[source][target] + update

print(links)

links_vis = []

for source, targets in links.items():
    for target, weight in targets.items():
        links_vis.append({
            "source": source,
            "target": target,
            "weight": weight
        })

print(links_vis)

transformed['links'] = links_vis

with open('data/philo-final.json', 'w') as f:
    json.dump(transformed, f)

