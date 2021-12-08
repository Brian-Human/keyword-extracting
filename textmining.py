from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import MinMaxScaler
import preprocessingutil as pre
import jasonutil as js

class Mining :
    def __init__(self, path: str, field, num: int, yaml_path: str) :
        self.data = js.load_json(path)
        
        self.seperated_doc_list = pre.preprocess(self.data, field, num, yaml_path)[0]
        self.unseperated_doc_list = pre.preprocess(self.data, field, num, yaml_path)[1]
            
    
    def tf_idf(self) :
        tfidf_vectorizer = TfidfVectorizer(lowercase=False)
        
        tfidfv = tfidf_vectorizer.fit(self.unseperated_doc_list)
        csr_matrix = tfidfv.transform(self.unseperated_doc_list)
        
        doc_word_score = {}        
        for doc_index, doc_content in enumerate(self.unseperated_doc_list) :
            scaler = MinMaxScaler(feature_range = (0, 100))
            scaler.fit(csr_matrix[doc_index].data.reshape(-1,1))
            score = scaler.transform(csr_matrix[doc_index].data.reshape(-1,1))
            
            doc_content = [word for word in doc_content.split() if len(word) > 1]
            new_doc_content = []
            for verb in doc_content :
                if verb not in new_doc_content :
                    new_doc_content.append(verb)
            
            dic = {}
            for word_index, word in enumerate(new_doc_content) :
                dic[word] = round(score[word_index][0], 2)
                
            doc_word_score[self.data.index[doc_index]] = dic
            
        return doc_word_score
    
    
