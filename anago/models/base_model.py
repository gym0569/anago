from keras.models import load_model, save_model


class BaseModel(object):

    def __init__(self, config, embeddings, ntags):
        self.config = config
        self.embeddings = embeddings
        self.ntags = ntags
        self.model = None

    def train(self, X, y):
        self._build_model()
        self.model.fit(X, y, batch_size=self.config.batch_size, epochs=self.config.epoch_size)

    def predict(self, X):
        y_pred = self.model.predict(X, batch_size=1)
        return y_pred

    def evaluate(self, X, y):
        score = self.model.evaluate(X, y, batch_size=1)
        return score

    def save(self, filepath):
        save_model(self.model, filepath)

    def load(self, filepath):
        self.model = load_model(filepath=filepath)

    def _build_model(self):
        pass
