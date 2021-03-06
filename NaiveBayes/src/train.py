import NaiveBayes.src.dataset as dataset
import NaiveBayes.src.naivebayes as nb

data = dataset.SentimentDataset()
data.load_data()
data.clean_data()
naivebayes = nb.NaiveBayes()
naivebayes.create_freqs(data.trainX,data.trainY.tolist())
naivebayes.train(data.trainX, data.trainY)
print(naivebayes.logprior)
print(len(naivebayes.loglikelihood))

naivebayes.predict("Nice")
naivebayes.predict("sad")
naivebayes.predict("very bad")
naivebayes.predict("very good")
naivebayes.predict("I did not like this movie")
naivebayes.predict("I would like to see more movies like this")

