import config


class Parser(object):
    def __init__(self, frequency_threshold):
        self.datafile = config.dataVectors
        self.frequency = frequency_threshold
        self.min_support = 0
        self.total = 0
        self.word_frequencies = {}
        self.items = []
        self.frequent_words = None
        self.total_items = 0
        self.words = 0
        self.lines = 0
        self.frequent_words_count = None

    def parse(self, datafile = None):
        if datafile is None:
            file = self.datafile
        else:
            self.datafile = datafile
            file = datafile

        current_item = (1, [])
        with open(file, 'r') as infile:
            self.total_items = int(infile.readline())
            self.words = int(infile.readline())
            self.lines = int(infile.readline())
            for line in infile:
                split = line.split(" ")
                item = int(split[0])
                word = int(split[1])

                if word in self.word_frequencies:
                    self.word_frequencies[word] += 1
                else:
                    self.word_frequencies[word] = 1

                if item != current_item[0]:
                    self.items.append(current_item)
                    current_item = (item, [word])
                else:
                    current_item[1].append(word)
                # self.total += 1

        self.min_support = round(self.frequency * self.total_items)
        self._remove_infrequent()
        self._sort_and_filter_items()

    def _remove_infrequent(self):
        self.frequent_words_count = {k: v for k, v in self.word_frequencies.items() if v > self.min_support}
        self.frequent_words = [x[0] for x in sorted(self.frequent_words_count, key=lambda x: x[1])]

    def _sort_and_filter_items(self):
        new_list = []
        for item in self.items:
            words = item[1]
            frequent = []
            for word in words:
                if word in self.word_frequencies and self.word_frequencies[word] > self.min_support:
                    frequent.append((word, self.word_frequencies[word]))
            if len(frequent) > 0:
                new_list.append([x[0] for x in sorted(frequent, key=lambda x: x[1])])
        self.items = new_list

if __name__ == "__main__":
    test = Parser(0.4)
    test.parse()
    print(test.frequent_words)


