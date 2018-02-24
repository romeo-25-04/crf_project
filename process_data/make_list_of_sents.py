import argparse

parser = argparse.ArgumentParser(
    description='Make list of strings sentences from a dataset.'
)
parser.add_argument("--path",
                    default="../var/test_data/NER-de-test.tsv",
                    help='path to data file')
arguments =parser.parse_args()

with open(arguments.path, encoding="utf8") as file_handle:
    lines = [line.strip().split('\t') for line in file_handle]
    sents = []
    sent = ''
    for line in lines:
        if len(line) == 4:
            sent += line[1] + ' '
        elif len(line) == 1:
            sents.append(sent.strip())
            sent = ''
    sents.append(sent.strip())

    out = '\n'.join(sents)
    with open('out.txt', 'w', encoding="utf8") as out_file:
        out_file.write(out)
