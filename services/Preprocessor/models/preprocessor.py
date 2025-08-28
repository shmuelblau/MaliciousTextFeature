import nltk
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('wordnet')
nltk.download('omw-1.4')


from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import string
import re



class Preprocessor:

    @staticmethod
    def remove_punctuation(tweet:str) -> str:
        return ''.join([char for char in tweet if char not in string.punctuation])


    @staticmethod
    def to_lower(tweet:str) -> str:
        return tweet.lower()


    @staticmethod
    def remove_special_marks(tweet:str) -> str:
        return re.sub(r'[^\w\s]', '', tweet)


    @staticmethod
    def remove_unnecessary_whitespace(tweet:str) -> str:
        return re.sub(r'\s+', ' ', tweet).strip()


    @staticmethod
    def remove_stop_words(tweet:str) -> str:
        stop_words = set(stopwords.words('english'))
        tokens = word_tokenize(tweet)
        filtered_tokens = [word for word in tokens if word not in stop_words]
        return ' '.join(filtered_tokens)


    @staticmethod
    def lemmatization(tweet) -> str:
        lemmatizer = WordNetLemmatizer()
        tokens = word_tokenize(tweet)
        lemmatized_words = [lemmatizer.lemmatize(word) for word in tokens]
        return ' '.join(lemmatized_words)

    @staticmethod
    def do_all(tweet):
        text = Preprocessor.remove_special_marks(tweet)
        text = Preprocessor.remove_unnecessary_whitespace(text)
        text = Preprocessor.to_lower(text)
        text = Preprocessor.remove_stop_words(text)
        text = Preprocessor.lemmatization(text)
        return text



