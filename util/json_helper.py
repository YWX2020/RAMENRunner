import json

RESULT_PATH = "run_results"

def save_to_json(json_file_name, ramen_result_dict):
    with open(f"{RESULT_PATH}/{json_file_name}", "w") as file:
        json.dump(ramen_result_dict, file, indent=4)
