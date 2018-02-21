from itertools import chain
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.preprocessing import LabelBinarizer
import sklearn

from process_data.get_data import GetData

def bio_classification_report(y_true, y_pred):
    lb = LabelBinarizer()
    y_true_combined = lb.fit_transform(list(chain.from_iterable(y_true)))
    y_pred_combined = lb.transform(list(chain.from_iterable(y_pred)))

    tagset = set(lb.classes_) #- {'O'}
    print(tagset)
    tagset = sorted(tagset, key=lambda tag: tag.split('-', 1)[::-1])
    class_indices = {cls: idx for idx, cls in enumerate(lb.classes_)}

    return classification_report(
        y_true_combined,
        y_pred_combined,
        labels=[class_indices[cls] for cls in tagset],
        target_names=lb.classes_,
    )


result = GetData('../var/results/result_arow.tsv')

print(result.sents[0].outer_labels_pred)

gtru = [sentence.outer_labels for sentence in result.sents]
pred = [sentence.outer_labels_pred for sentence in result.sents]
print(len(gtru), len(pred))

print(bio_classification_report(gtru, pred))
