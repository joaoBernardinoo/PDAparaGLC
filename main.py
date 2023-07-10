Q = ['Q_n','q_0','q_1','q_2','Q_f']
def convert_ap_to_glc(transitions):
	glc_rules = []
	for transition in transitions:
		q, a, B, p, CD = transition
		productions = ''
		if a == 'ε':
			a = ''
		
		if CD == 'ε':
			# Regra para transição com desempilhamento
			if a == '':
				glc_rule = f"$$[{q}{B}{p}] -> ε$$"
				glc_rules.append(glc_rule)
			# Regra para transição sem mexer na pilha
			else:
				glc_rule = f"$$[{q}{B}{p}] -> {a}$$"
				glc_rules.append(glc_rule)

			
			
		# Regra para transição com empilhamento e desempilhamento
		elif len(CD) == 2:
			for j in Q:
				for i in Q:
					productions += f"[{p}{CD[0]}{i}][{i}{CD[1]}{p}]"
					variable = f"{q}{B}{j}"
					glc_rule = f"$$[{variable}] -> {a}{productions}$$"
					glc_rules.append(glc_rule)
					productions = ''

	return glc_rules

# Exemplo de uso
transitions = [
	('q_1', '1', '1', 'q_1', 'ε'),
]

glc_rules = convert_ap_to_glc(transitions)

# Exibir as regras de produção da GLC
for rule in glc_rules:
	print(rule)
