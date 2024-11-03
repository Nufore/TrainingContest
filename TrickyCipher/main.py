import string
from sys import intern


def num_of_letter(word: str) -> int | str:
	alfabet = string.ascii_lowercase
	if word.lower() in alfabet:
		numb = alfabet.index(word.lower())
		return numb + 1


def get_last_three_from_hex(numb: int) -> str:
	return hex(numb)[-3:]


def unique_words(data):
	counter = []
	for word in data:
		for symbol in word:
			if symbol not in counter:
				counter.append(symbol)
	return len(counter)


def date_month_sum(data):
	summ = 0
	for numb in data:
		for symbol in numb:
			summ += int(symbol)
	return summ


def main():
	n = int(input())
	interns = []
	for _ in range(n):
		data = input().split(',')

		unique_words_in_fio = unique_words(data[0:3])
		sum_of_date_and_month = date_month_sum(data[3:5])
		first_letter = num_of_letter(data[0][0])

		final_value = unique_words_in_fio + sum_of_date_and_month * 64 + first_letter * 256

		interns.append(get_last_three_from_hex(final_value).upper())

	string_data = ' '.join(interns)
	print(string_data)


if __name__ == "__main__":
	main()

