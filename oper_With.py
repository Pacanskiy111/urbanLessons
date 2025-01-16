class WordsFinder:
    def __init__(self, *args):
        self.file_names = args

    def get_all_words(self):
        all_words = {}
        list_ = []
        symbols = [',', '.', '=', '!', '?', ';', ':', ' - ']
        for name in self.file_names:
            with open(name, encoding='utf-8') as file:
                for line in file:
                    line = line.lower()
                    for i in symbols:
                        line = line.replace(f'{i}', '')
                    line = line.split()
                    list_ += line
            all_words[name] = list_
        return all_words

    def find(self, word):
        dict_find = {}
        for name, words in self.get_all_words().items():
            for i in words:
                if i == word.lower():
                    dict_find[name] = words.index(i) + 1
            return dict_find

    def count(self, word):
        equal = 0
        dict_count = {}
        for name, words in self.get_all_words().items():
            for i in words:
                if i == word.lower():
                    equal += 1
                    dict_count[name] = equal
            return dict_count


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего
