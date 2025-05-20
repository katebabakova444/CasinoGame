from collections import Counter
class Statistics:
    def analyze(self, outcomes):
        counts = Counter(outcomes)
        return dict(counts)