from collections import Counter

def analyze_outcome(self):
    counts = Counter(self.outcomes)
    return dict(counts)