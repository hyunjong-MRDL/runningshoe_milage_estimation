from pathlib import Path

def load_data(filepath, datatype="processed"):
    # datatype: "raw" or "processed"
    data_list = []
    data_dir = filepath / datatype
    if not data_dir.exists():
        data_dir.touch()
    
    for item in data_dir.iterdir():
        data_list.append(item)

    return data_list

if __name__ == "__main__":
    cwd = Path.cwd()
    data_root = cwd / r"data"
    if not data_root.exists():
        data_root.touch()

    """ 데이터 제대로 불러오는 것 확인 """
    raw_data = load_data(data_root, "raw")  # raw data
    processed_data = load_data(data_root)   # processed data

    print(len(raw_data), len(processed_data))