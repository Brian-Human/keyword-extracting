import re
import configutil


def preprocess(dataframe, field: str, num: int, yaml_path: str) :
    content_series = dataframe[field]
    
    config_yaml = configutil.readconfig(yaml_path)
    

    seperated_doc_list = []
    unseperated_doc_list = []
    for doc in content_series :
        sentences = re.split('[!?.]', doc)
        sentences = list(filter(None, sentences))
        
        sentence_list = []
        sentence_str = ""
        for sentence in sentences :
            if not sentence :
                continue
            
            if num == 1 :
                removespec = config_yaml['preprocessing_option'][1]
                
                sentence = re.sub(removespec, ' ', sentence)
                sentence = sentence.strip()
                
                # 문자열 변수에 다른 형이 있을 경우
                if len(sentence_str) > 0 :
                    sentence_str += " "
                    
                sentence_str += str(sentence)
                
                sentence_list.append(sentence)
                
                
            elif num == 2 :
                removeall = config_yaml['preprocessing_option'][2]
                
                sentence = re.sub(removeall, ' ', sentence)
                sentence = sentence.strip()
                
                # 문자열 변수에 다른 형이 있을 경우
                if len(sentence_str) > 0 :
                    sentence_str += " "
                    
                sentence_str += str(sentence)
                
                sentence_list.append(sentence)
                    
        
        unseperated_doc_list.append(sentence_str)    
        seperated_doc_list.append(sentence_list)
        
    return seperated_doc_list, unseperated_doc_list
    