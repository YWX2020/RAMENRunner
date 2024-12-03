import sys
from util.json_helper import save_to_json

from configurator.configuration_loader import ConfigurationLoader
from ramen.Ramen import Ramen
from util.ressource_profiler import measure_performance
from util.pickler import pickle_object

VAR_REF_PREFIX = "var_refs/"

@measure_performance()
def get_ramen_structure(config_filename, save_json_filename, save_var_ref_name, random_walk_only):
    config_loader = ConfigurationLoader(config_filename)
    ramen_bowl = Ramen(config_loader.csv_filename, config_loader.end_var, config_loader.min_values)
    ramen_bowl.random_walk(
        config_loader.num_exp,
        config_loader.num_walks,
        config_loader.num_steps,
        config_loader.p_value,
        config_loader.correction)

    if not random_walk_only:
        ramen_bowl.genetic_algorithm(
            config_loader.num_candidates,
            config_loader.end_thresh,
            config_loader.mutate_num,
            config_loader.best_cand_num,
            config_loader.bad_repod_accept,
            config_loader.reg_factor,
            config_loader.hard_stop)

    save_to_json(save_json_filename, ramen_bowl.export_ramen_as_dict())
    pickle_object(ramen_bowl.var_ref, VAR_REF_PREFIX + save_var_ref_name)

def parse_str_to_bool(string):
    if string.lower() in ("true", "1"):
        return True
    elif string.lower() in ("false", "0"):
        return False
    else:
        raise ValueError(f"Valid values are: true, 1, false, 0 - Input value is {string}")


if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python run_ramen.py <config_filename> <save_json_filename> <var_ref_filename> <random_walk_only>")
        sys.exit(1)

    config_name = sys.argv[1]
    save_name = sys.argv[2]
    var_ref_filename = sys.argv[3]
    rw_only_bool = parse_str_to_bool(sys.argv[4])

    get_ramen_structure(config_name, save_name, var_ref_filename, rw_only_bool)
