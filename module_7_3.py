class WordsFinder:
    all_words = {}

    def __init__(self, *filename):
        self.filename = filename

    def get_all_words(self):
        for filename in self.filename:
            words = []
            with open(filename, 'r', encoding='utf-8') as file:
                for line in file:
                    no_need_symbols = (',', '.', '=', '!', '?', ';', ':', ' - ')
                    line = ''.join(symbol for symbol in line if symbol not in no_need_symbols)
                    words.extend(line.lower().strip().split())
            self.all_words[filename] = words
        return self.all_words

    def find(self, word):
        result = {}
        for name, words in self.get_all_words().items():
            need = word.lower()
            word_number = 0
            for word in words:
                word_number += 1
                if need in word:
                    result[name] = word_number
                    break
        return result

    def count(self, word):
        result = {}
        for name, words in self.get_all_words().items():
            need = word.lower()
            if need in words:
                result[name] = words.count(need)
        return result


#  Пример выполнения программы:
# finder2 = WordsFinder('test_file.txt')
# print(finder2.get_all_words())  # Все слова
# print(finder2.find('TEXT'))  # 3 слово по счёту
# print(finder2.count('teXT'))  # 4 слова teXT в тексте всего

# finder3 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt')
# print(finder3.get_all_words())
# print(finder3.find('captain'))
# print(finder3.count('captain'))

# finder4 = WordsFinder('Rudyard Kipling - If.txt',)
# print(finder4.get_all_words())
# print(finder4.find('if'))
# print(finder4.count('if'))
