config_file_folder = "run_configurations"

class ConfigurationLoader(object):
    def __init__(self, config_file_name):
        with open(f"{config_file_folder}/{config_file_name}", "r") as file:
            lines = [line.strip() for line in file if line.strip() and not line.startswith("#")]

        parameter_dict = {}
        for line in lines:
            parameter_key, value = line.split("=")
            parameter_dict[parameter_key] = value

        # Load processing parameter
        self.min_values = int(parameter_dict["min_values"])
        self.end_var = parameter_dict["end_var"]
        self.csv_filename = parameter_dict["csv_filename"]

        # Load Random Walk parameters
        self.num_exp = int(parameter_dict["num_exp"])
        self.num_walks = int(parameter_dict["num_walks"])
        self.num_steps = int(parameter_dict["num_steps"])
        self.p_value = float(parameter_dict["p_value"])
        self.correction = parameter_dict["correction"]

        # Load Genetic Algorithm parameters
        self.num_candidates = int(parameter_dict["num_candidates"])
        self.end_thresh = float(parameter_dict["end_thresh"])
        self.mutate_num = int(parameter_dict["mutate_num"])
        self.best_cand_num = int(parameter_dict["best_cand_num"])
        self.bad_repod_accept = int(parameter_dict["bad_repod_accept"])
        self.reg_factor = float(parameter_dict["reg_factor"])
        self.hard_stop = int(parameter_dict["hard_stop"])
