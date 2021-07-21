class AucCompute():
    def __init__(self):
        self.samples = []
        samples = [(0.5, 1), (0.6, 1), (0.2, 0), (0.55, 0)]

    def compute(self, label, score):
        samples = sorted()


    def roc_area(self, ):

        def true_pos_rate():
            return float(tp)/(float(tp) + float(fn))
        def false_peg_rate():
            return float(fp)/(float(tn) + float(fp))

        sample_total = float(len(samples))
        pos_total = 0.0
        for label, _ in samples:
            pos_total += label
        neg_total = sample_total - pos_total
        last_score =
        tp = 0
        fn = pos_total /
        for label, score in samples:
            if label = 1:
                tp +=1
            else:
                fp += 1



