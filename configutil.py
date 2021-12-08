import yaml

class Config :
    def __init__(self) :
        self.config = {}

    def make_config(self, input_file_path: str, input_file_name: str, output_file_path: str, output_file_name: str, analyze_fieldname: str, remove_specialcharacter: str, remove_all_except_hangul: str, list_score_descending: str, list_word_ascending: str, df_score_descending: str, df_word_ascending: str) :

        self.config = {'path': {'input':{'file_path':input_file_path, 'file_name':input_file_name}, 'output':{'file_path':output_file_path, 'file_name':output_file_name}},
                       'analyze_field': analyze_fieldname,
                       'preprocessing_option': {1:remove_specialcharacter, 2:remove_all_except_hangul},
                       'printout_word': {'num':{0:'[:]', 'N':'[:N]'}, 'method':{'list':{1:list_score_descending, 2:list_word_ascending},'dataframe':{1:df_score_descending, 2:df_word_ascending}}}
                       }



    # Python 객체를 YAML 파일로 쓰기: with open('w') as f: yaml.dump()
    def write_config(self, out_path: str) :
        with open(out_path, 'w', encoding='utf-8') as f:
            # 출력은 읽을 수 있는 블록 스타일이어야 하므로 default_flow_style를 False로 설정
            # 한글이 깨지지 않게 unicode를 허용
            yaml.dump(self.config, f,default_flow_style=False, allow_unicode=True)

"""yaml.load는 문자열을 파이썬데이터로 바꾸어주고 yaml.dump는 파이썬데이터를 yaml형태로 바꾸어준다."""

# YAML 파일을 파싱해서 Python 객체로 읽어오기: yaml.load()
def read_config(yaml_path: str) :
    with open(yaml_path, 'r', encoding='utf-8') as f:
        config_yaml = yaml.load(f)
    return config_yaml
    






if __name__ == "__main__" :
    input_file_path = './input/2021-03-01.json'
    input_file_name = '2021-03-01.json'
    output_file_path = './output/config.yaml'
    output_file_name = 'config.yaml'

    yaml_path = './output/config.yaml'
    
    analyze_fieldname = 'doc_content'

    remove_specialcharacter = "[^a-zA-Z0-9ㄱ-ㅎ가-힣 ]"
    remove_all_except_hangul = "[ㄱ-ㅎ가-힣 ]"

    list_score_descending = "key=score, reverse=True"
    list_word_ascending = "key=word, reverse=False"
    df_score_descending = "by=[\"score\"], axis=0, ascending=False"
    df_word_ascending = "by=[\"word\"], axis=0, ascending=True"


    config = Config()

    config.make_config(input_file_path, input_file_name, output_file_path, output_file_name, analyze_fieldname, remove_specialcharacter, remove_all_except_hangul, list_score_descending, list_word_ascending, df_score_descending, df_word_ascending)
    config.write_config(output_file_path)
    #print(config.config)
    
    
    #config_yaml = read_config(yaml_path)
    #print(config_yaml)
