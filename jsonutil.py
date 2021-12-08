import pandas as pd


# 용량이 큰 json 파일을 한번에 읽어서 dataframe으로 변환하는 것은 어렵기에 generator를 사용하여 한줄씩 읽고 변환
def parse(path: str):
    file = open(path, "r")
    for l in file:
        yield eval(l)

def parse_json_to_df(path: str, changetype) -> pd.DataFrame:
    i = 0
    df_dict = {}
    for d in parse(path):
        df_dict[i] = d
        i += 1

    df = pd.DataFrame.from_dict(df_dict, orient="index")
    
    if changetype == 'str' :
        df = df.astype(str)
    
    return df


# 중복 데이터가 있는 행 제거
def drop_duplicate_row(df, column: str) :
    return df.drop_duplicates([column])

# 컬럼을 인덱스로 지정
def set_column_to_index(df, column: str):
    return df.set_index(column)


# json파일 읽어들이기
def load_json(path: str, changetype=None, doc_key="doc_id") :
    df = parse_json_to_df(path, changetype)
    
    df = drop_duplicate_row(df, doc_key)
    
    df = set_column_to_index(df, doc_key)
    
    return df


# 데이터프레임을 json파일로 쓰기
# 어떻게 될런지는 모르지만 상황에 따라서 orient를 다르게 주어야 한다.
# for문 돌려서 한 줄씩 파일에 써야할 수도 있다.