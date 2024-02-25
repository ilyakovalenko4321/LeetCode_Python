class StrongPasswordChecker:
	@staticmethod
	def decomposition(s):
		elementary_parts_of_password = []
		for i in s:
			elementary_parts_of_password.append(i)
		sorted_elementary = {'repetition': False, 'title': 0, 'lower': 0, 'integer': 0, 'len': len(elementary_parts_of_password)}
		repetitions = 1
		previous = None
		for i in elementary_parts_of_password:
			"""Показывает сколько всего букв превысило лимит серии
			Надо сделать чтобы показывало повторения по отдельности"""
			if i == previous:
				repetitions += 1
			else:
				repetitions = 1
			if repetitions >= 3:
				sorted_elementary['repetition'] += 1

			"""Проверяет количество нужных символов"""
			if i.istitle():
				sorted_elementary['title'] += 1
			else:
				try:
					int(i)
					sorted_elementary['integer'] += 1
				except ValueError:
					sorted_elementary['lower'] += 1
			previous = i
		return sorted_elementary

	@classmethod
	def steps(cls, s):
		"""Когда будут показывать по отдельности повторения, просто вычесть из общего количества повторения.
		Если не будет хватать, то заменить на недостающие избыточные символы"""

		decomposition_dictionary = cls.decomposition(s)

		return decomposition_dictionary


x = StrongPasswordChecker
y = x.steps('A11sstt')
print(y)

print('FU')