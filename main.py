import configutil
import textmining as tm

# 설정 파일 불러오기
yaml_path = './config/config.yaml'
config_yaml = configutil.readconfig(yaml_path)

# 설정 파일에 있는 json파일 경로
path = config_yaml['path']['input']['file_path']

# 설정 파일에 있는 분석할 필드   // doc_content
field = config_yaml['analyze_field']

# 1을 넣으면 특수문자가 제거된 데이터로 다루는 것, Mining인스턴스 생성
rem_spechr = tm.Mining(path, field, 1, yaml_path)

# 2를 넣으면 한글 이외에 모두 제거된 데이터로 다루는 것, Mining인스턴스 생성
rem_all = tm.Mining(path, field, 2, yaml_path)

# 단어 중요도 dict 생성
rem_spechr_dict = rem_spechr.tf_idf()
print(rem_spechr_dict)

rem_all_dict = rem_all.tf_idf()
print(rem_all_dict)



























