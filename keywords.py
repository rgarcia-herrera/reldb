# coding: utf-8
import csv
from pattern.es import parse, split

with open('reporte.csv') as f, open('reporte_kw.csv', 'w') as o:
    w = csv.writer(o)
    reporte = csv.reader(f, delimiter="|", quotechar='"')
    header = reporte.next() + ['verbs', 'adj', 'nouns']
    w.writerow(header)
    for r in reporte:

        s = parse(r[7], lemmata=True, relations=True)
        nouns = []
        adj = []
        verbs = []
        for sentence in split(s):
            nouns += [n.lemma for n in sentence.nouns]
            adj += [a.string for a in sentence.adjectives]
            for v in sentence.verbs:
                for l in v.lemmata:
                    verbs.append(l)

        w.writerow(r + [" ".join(verbs).encode('utf-8'),
                        " ".join(adj).encode('utf-8'),
                        " ".join(nouns).encode('utf-8')])
