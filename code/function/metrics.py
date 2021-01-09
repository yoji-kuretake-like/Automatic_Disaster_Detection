#This is the function of metrics

def true_positive(y_true, y_pred):
    return Kbackend.sum(Kbackend.cast(Kbackend.equal(y_true * y_pred, 1), Kbackend.floatx()))

def false_positive(y_true, y_pred):
    return Kbackend.sum(Kbackend.cast(Kbackend.less(y_true, y_pred), Kbackend.floatx()))

def false_negative(y_true, y_pred):
    return Kbackend.sum(Kbackend.cast(Kbackend.greater(y_true, y_pred), Kbackend.floatx()))

def iou(y_true, y_pred):
    y_pred = Kbackend.round(y_pred)
    return true_positive(y_true, y_pred) / (false_negative(y_true, y_pred)+true_positive(y_true, y_pred)+false_positive(y_true, y_pred) + Kbackend.epsilon())
