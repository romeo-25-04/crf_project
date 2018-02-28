from process_data.get_data import Dataset
import pprint
pp = pprint.PrettyPrinter(indent=2)


data = Dataset('../var/train_data/NER-de-train.tsv')

names = set()
for sentence in data.sents:
    for (Id, word, label, label2) in sentence.sent:
        if label == 'B-PER':
            names.add(word)

names = sorted(names)
suffixes = [name[-4:] for name in names]
suffixes = sorted(suffixes)

freq = dict()
for suff in suffixes:
    suff = suff.lower()
    freq[suff] = freq.get(suff, 0) + 1
desc_freq = sorted(freq, key=freq.get, reverse=True)

best = [key for key in desc_freq[:150]
        if freq[key] > 5]

# suff form payment-recip-set
exist = {"+", "gmbh", "dr.", "kg", "tadt", "med.", "pvs", "mann",
         "ag", "haus", "co", "asse", "heke", "otto", "co.", "vice", "land", "burg",
         "axis", "dr", "mvz", "arna", "shop", "hibo", "ngen", "trum", "abor", "berg",
         "tung", "cher", "sche", "line", "haft", "eter", "bank", "ller", "prix",
         "bert", "rieb", "reis", "rlag", "heim", "hnik", "west", "plus", "dorf",
         "rung", "e.v.", "bad", "gbr", "nger", "auer", "bach", "chen", "prit",
         "ener", "iver", "hule", "samt", "auto", "rope", "ster", "ernd", "ikum",
         "omas", "eine", "data", "fuer", "ko-o", "nder", "sand", "reas", "ypal", "med",
         "eger", "eier", "anne", "tion", "stik", "over", "rich", "inik", "tein", "ches",
         "buhl", "egen", "toys", "cker", "eder", "mmer", "tian", "esso", "beck", "rlin",
         "erke", "fone", "iner", "rgen", "eiss", "eben", "ider", "arzt", "efan", "isch",
         "arkt", "rank", "serv", "usen", "rger", "hler", "tter", "nter", "erei", "hard",
         "ling", "eria", "hael", "rner", "ngut", "furt", "werk", "ance", "ital",
         "azon", "inde", "sser", "fhof", "rtin", "ndel", "gner", "db"}

union = sorted(set(best) | exist)

# pp.pprint(union)

print('exist:\t', len(exist))
print('best:\t', len(best))
print('union:\t', len(union))

output = ", ".join(['"{0}"'.format(x) for x in union])

with open('../var/suffix_list.txt', 'w') as file_handler:
    file_handler.write(output)
