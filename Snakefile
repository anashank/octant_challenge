configfile: "config.yaml"

rule all:
    input: expand("{plot_filename}", plot_filename = config['plot_filename'])


rule join_data:
	input: 
		setup = expand("{setup}", setup = config['setup_filename']),
		data = expand("{data}", data = config['data_filename'])
	output: 
		expand("{jd}", jd = config['joined_data_filename'])
	shell:
		"python join.py --setup {input.setup} --data {input.data}"


rule get_outliers:
	input: 
		expand("{jd}", jd = config['joined_data_filename'])
	output: 
		expand("{qc}", qc = config['qc_filename'])
	shell:
		"python outlier.py"

rule fit_model:
	input: 
		expand("{qc}", qc = config['qc_filename'])
	output: 
		expand("{mf}", mf = config['model_filename'])
	shell:
		"python model.py"


rule generate_plot:
	input: 
		expand("{mf}", mf = config['model_filename'])
	output: 
		expand("{pf}", pf = config['plot_filename'])
	shell:
		"python plot.py"

        

