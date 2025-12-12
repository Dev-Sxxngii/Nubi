from dotenv import find_dotenv, load_dotenv
from dotenv import dotenv_values

# 환경 변수 로드
def load_env():
    env_path = find_dotenv()
    load_dotenv(env_path)    

# 데이터 타입 변환(if numeric: str → int)
def convert_data_type_str_to_int(value: str):
    return int(value) if value.isnumeric() else value
    
# 딕셔너리 값 변환(dict value: str → int)    
def convert_dict_values_str_to_int(env_dict: dict):
    for key in env_dict:
        env_dict[key] = convert_data_type_str_to_int(env_dict[key])
    return env_dict

# env 분류    
def split_env_by_category(category_name: str):
    config = dotenv_values(".env")
    categorized_env = {
        key: value for key, value in config.items() if category_name in key # 딕셔너리 컴프리헨션
    }
    processed_env = convert_dict_values_str_to_int(categorized_env)
    return processed_env


 