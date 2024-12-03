# RunRamenScripts
Scripts to easily run the ramen package

Link to RAMEN repo: https://github.com/mcgilldinglab/RAMEN

## Steps

### Setup environment

```
conda activate env
```

```
pip install git+https://github.com/mcgilldinglab/RAMEN.git@development
```

## RAMEN

### Prepare configurations
Make a copy of ```run_configurations/run_config_template.txt``` and update the values to the ones that you want to use. 
Types must follow the current values in the template. Update only after the = sign. Lines with # are ignored. 
The new file needs to be in run_configurations.

### Run
```
python3 run_ramen.py config_filename save_filename var_ref_filename random_walk_only
```

```config_filename```: file name of the config file done in the previous step. Only include the name of the file, not the path.

```save_filename```: file path that RAMEN output will write to in a json format.

```var_ref_filename```: file to which the variable discretization references will be saved to.

```random_walk_only```: parameter to decide if we only run random_walk or the whole workflow. Positive Values are {True, true, 1}
Negative Values are {False, false, 0}
