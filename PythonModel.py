import calliope
import pandas as pd
import subprocess
import os
import webbrowser
import shlex

# We increase logging verbosity
calliope.set_log_verbosity('INFO', include_solver_output= True)

#%%RUN Model
# Define and build the model
model_path = "/Users/hiddegrootes/Library/Mobile Documents/com~apple~CloudDocs/03_TU DELFT/Jaar 7/Q4_MSc Thesis/02_Methods/05_Energy Modelling(Calliope)/03_UitgeestNoord_ModelMap/model.yaml"
model = calliope.Model(model_path)
model.build()
model.solve()

# Ensure the output folder exists
output_folder = "/Users/hiddegrootes/Library/Mobile Documents/com~apple~CloudDocs/03_TU DELFT/Jaar 7/Q4_MSc Thesis/02_Methods/05_Energy Modelling(Calliope)/04_Results_files"
os.makedirs(output_folder, exist_ok=True)

# Save the results to a NetCDF file
output_file = os.path.join(output_folder, "UitgeestNoord_results.nc")
model.to_netcdf(output_file)

# Run cview command to launch the web interface
cview_command = f'cview "{output_file}" --port 8001'
subprocess.run(cview_command, shell=True)

# Open the URL in Safari
webbrowser.get('safari').open('http://localhost:8001')
#%%RUN scenario='Current_scenario'

# Build and solve the model
model = calliope.Model("/Users/hiddegrootes/Library/Mobile Documents/com~apple~CloudDocs/03_TU DELFT/Jaar 7/Q4_MSc Thesis/02_Methods/05_Energy Modelling(Calliope)/03_UitgeestNoord_ModelMap/model.yaml", scenario='Current_scenario')
model.build()
model.solve()

# Ensure the new output folder exists
output_folder = "/Users/hiddegrootes/Library/Mobile Documents/com~apple~CloudDocs/03_TU DELFT/Jaar 7/Q4_MSc Thesis/02_Methods/05_Energy Modelling(Calliope)/04_results_files"
os.makedirs(output_folder, exist_ok=True)

# Save the results to a NetCDF file in the new folder
output_file = os.path.join(output_folder, "UitgeestNoord_results_Current_Scenario.nc")
model.to_netcdf(output_file)

# Use shlex.quote to safely quote the file path
quoted_output_file = shlex.quote(output_file)
cview_command = f"cview {quoted_output_file} --port 8000"
subprocess.run(cview_command, shell=True)

# Open the URL in Safari
webbrowser.get('safari').open('http://localhost:8000')
#%%RUN scenario='Solution_mix_1'
model = calliope.Model("/Users/hiddegrootes/Library/Mobile Documents/com~apple~CloudDocs/03_TU DELFT/Jaar 7/Q4_MSc Thesis/02_Methods/05_Energy Modelling(Calliope)/03_UitgeestNoord_ModelMap/model.yaml", scenario='Solution_mix_1')

# Build and solve the model for Solution_mix_1
model.build()
model.solve()

# Ensure the new output folder exists
output_folder = "/Users/hiddegrootes/Library/Mobile Documents/com~apple~CloudDocs/03_TU DELFT/Jaar 7/Q4_MSc Thesis/02_Methods/05_Energy Modelling(Calliope)/04_results_files"
os.makedirs(output_folder, exist_ok=True)

# Save the results to a NetCDF file in the new folder for Solution_mix_1
output_file = os.path.join(output_folder, "UitgeestNoord_results_Solution_mix_1.nc")
model.to_netcdf(output_file)

# Use shlex.quote to safely quote the file path
quoted_output_file = shlex.quote(output_file)
cview_command = f"cview {quoted_output_file} --port 8010"
subprocess.run(cview_command, shell=True)

# Open the URL in Safari
webbrowser.get('safari').open('http://localhost:8010')
#%%RUN scenario='Solution_mix_2'
model = calliope.Model("/Users/hiddegrootes/Library/Mobile Documents/com~apple~CloudDocs/03_TU DELFT/Jaar 7/Q4_MSc Thesis/02_Methods/05_Energy Modelling(Calliope)/03_UitgeestNoord_ModelMap/model.yaml", scenario='Solution_mix_2')
model.build()
model.solve()

# Save the results to a NetCDF file
output_file = "UitgeestNoord_results_Solution_mix_2.nc"
model.to_netcdf(output_file)

# Run cview command to launch the web interface
cview_command = f"cview {output_file} --port 8022"
subprocess.run(cview_command, shell=True)
#%%RUN scenario='Solution_mix_3_A'
model = calliope.Model("/Users/hiddegrootes/Library/Mobile Documents/com~apple~CloudDocs/03_TU DELFT/Jaar 7/Q4_MSc Thesis/02_Methods/05_Energy Modelling(Calliope)/03_UitgeestNoord_ModelMap/model.yaml", scenario='Solution_mix_3_A')
model.build()
model.solve()

# Save the results to a NetCDF file
output_file = "UitgeestNoord_results_Solution_mix_3A.nc"
model.to_netcdf(output_file)

# Run cview command to launch the web interface
cview_command = f"cview {output_file} --port 8030"
subprocess.run(cview_command, shell=True)

#%%RUN scenario='Solution_mix_3_B'
model = calliope.Model("/Users/hiddegrootes/Library/Mobile Documents/com~apple~CloudDocs/03_TU DELFT/Jaar 7/Q4_MSc Thesis/02_Methods/05_Energy Modelling(Calliope)/03_UitgeestNoord_ModelMap/model.yaml", scenario='Solution_mix_3_B')
model.build()
model.solve()

# Save the results to a NetCDF file
output_file = "UitgeestNoord_results_Solution_mix_3B.nc"
model.to_netcdf(output_file)

# Run cview command to launch the web interface
cview_command = f"cview {output_file} --port 8031"
subprocess.run(cview_command, shell=True)

 #%%RUN scenario='Cost_storage_cap_S1'
# Define and build the model
model = calliope.Model("/Users/hiddegrootes/Library/Mobile Documents/com~apple~CloudDocs/03_TU DELFT/Jaar 7/Q4_MSc Thesis/02_Methods/05_Energy Modelling(Calliope)/03_UitgeestNoord_ModelMap/model.yaml", scenario='Cost_storage_cap_S1')
model.build()
model.solve()

# Save the results to a NetCDF file
output_file = "UitgeestNoord_results_Cost_storage_cap_S1.nc"
model.to_netcdf(output_file)

# Run cview command to launch the web interface
cview_command = f'cview "{output_file}" --port 8190'
subprocess.run(cview_command, shell=True)

#%%RUN scenario='Cost_storage_cap_S2'
# Define and build the model
model = calliope.Model("/Users/hiddegrootes/Library/Mobile Documents/com~apple~CloudDocs/03_TU DELFT/Jaar 7/Q4_MSc Thesis/02_Methods/05_Energy Modelling(Calliope)/03_UitgeestNoord_ModelMap/model.yaml", scenario='Cost_storage_cap_S2')
model.build()
model.solve()

# Save the results to a NetCDF file
output_file = "UitgeestNoord_results_Cost_storage_cap_S2.nc"
model.to_netcdf(output_file)

# Run cview command to launch the web interface
cview_command = f'cview "{output_file}" --port 8200'
subprocess.run(cview_command, shell=True)

#%%RUN scenario='Cost_storage_cap_S3'
# Define and build the model
model = calliope.Model("/Users/hiddegrootes/Library/Mobile Documents/com~apple~CloudDocs/03_TU DELFT/Jaar 7/Q4_MSc Thesis/02_Methods/05_Energy Modelling(Calliope)/03_UitgeestNoord_ModelMap/model.yaml", scenario='Cost_storage_cap_S3')
model.build()
model.solve()

# Save the results to a NetCDF file
output_file = "UitgeestNoord_results_Cost_storage_cap_S3.nc"
model.to_netcdf(output_file)

# Run cview command to launch the web interface
cview_command = f'cview "{output_file}" --port 8210'
subprocess.run(cview_command, shell=True)

#%%RUN scenario='Cost_storage_cap_S3_300'
# Define and build the model
model = calliope.Model("/Users/hiddegrootes/Library/Mobile Documents/com~apple~CloudDocs/03_TU DELFT/Jaar 7/Q4_MSc Thesis/02_Methods/05_Energy Modelling(Calliope)/03_UitgeestNoord_ModelMap/model.yaml", scenario='Cost_storage_cap_S3_300')
model.build()
model.solve()

# Save the results to a NetCDF file
output_file = "UitgeestNoord_results_Cost_storage_cap_S3_300.nc"
model.to_netcdf(output_file)

# Run cview command to launch the web interface
cview_command = f'cview "{output_file}" --port 8211'
subprocess.run(cview_command, shell=True)

#%%RUN scenario='Cost_storage_cap_S4'
# Define and build the model
model = calliope.Model("/Users/hiddegrootes/Library/Mobile Documents/com~apple~CloudDocs/03_TU DELFT/Jaar 7/Q4_MSc Thesis/02_Methods/05_Energy Modelling(Calliope)/03_UitgeestNoord_ModelMap/model.yaml", scenario='Cost_storage_cap_S4')
model.build()
model.solve()

# Save the results to a NetCDF file
output_file = "UitgeestNoord_results_Cost_storage_cap_S4.nc"
model.to_netcdf(output_file)

# Run cview command to launch the web interface
cview_command = f'cview "{output_file}" --port 8212'
subprocess.run(cview_command, shell=True)


#%%RUN scenario='Battery_limit_S1'
model = calliope.Model("/Users/hiddegrootes/Library/Mobile Documents/com~apple~CloudDocs/03_TU DELFT/Jaar 7/Q4_MSc Thesis/02_Methods/05_Energy Modelling(Calliope)/03_UitgeestNoord_ModelMap/model.yaml", scenario='Battery_limit_S1')
model.build()
model.solve()

# Save the results to a NetCDF file
output_file = "UitgeestNoord_results_Battery_limit_S1.nc"
model.to_netcdf(output_file)

# Run cview command to launch the web interface
cview_command = f"cview {output_file} --port 8160"
subprocess.run(cview_command, shell=True)

#%%RUN scenario='Battery_limit_S2'
model = calliope.Model("/Users/hiddegrootes/Library/Mobile Documents/com~apple~CloudDocs/03_TU DELFT/Jaar 7/Q4_MSc Thesis/02_Methods/05_Energy Modelling(Calliope)/03_UitgeestNoord_ModelMap/model.yaml", scenario='Battery_limit_S2')
model.build()
model.solve()

# Save the results to a NetCDF file
output_file = "UitgeestNoord_results_Battery_limit_S2.nc"
model.to_netcdf(output_file)

# Run cview command to launch the web interface
cview_command = f"cview {output_file} --port 8170"
subprocess.run(cview_command, shell=True)

#%%RUN scenario='Battery_limit_S3'
model = calliope.Model("/Users/hiddegrootes/Library/Mobile Documents/com~apple~CloudDocs/03_TU DELFT/Jaar 7/Q4_MSc Thesis/02_Methods/05_Energy Modelling(Calliope)/03_UitgeestNoord_ModelMap/model.yaml", scenario='Battery_limit_S3')
model.build()
model.solve()

# Save the results to a NetCDF file
output_file = "UitgeestNoord_results_Battery_limit_S3.nc"
model.to_netcdf(output_file)

# Run cview command to launch the web interface
cview_command = f"cview {output_file} --port 8180"
subprocess.run(cview_command, shell=True)

#%%RUN scenario='Battery_limit_S4'
model = calliope.Model("/Users/hiddegrootes/Library/Mobile Documents/com~apple~CloudDocs/03_TU DELFT/Jaar 7/Q4_MSc Thesis/02_Methods/05_Energy Modelling(Calliope)/03_UitgeestNoord_ModelMap/model.yaml", scenario='Battery_limit_S4')
model.build()
model.solve()

# Save the results to a NetCDF file
output_file = "UitgeestNoord_results_Battery_limit_S4.nc"
model.to_netcdf(output_file)

# Run cview command to launch the web interface
cview_command = f"cview {output_file} --port 8180"
subprocess.run(cview_command, shell=True)

#%%RUN scenario='Expansion_demand_1_25x'
model = calliope.Model("/Users/hiddegrootes/Library/Mobile Documents/com~apple~CloudDocs/03_TU DELFT/Jaar 7/Q4_MSc Thesis/02_Methods/05_Energy Modelling(Calliope)/03_UitgeestNoord_ModelMap/model.yaml", scenario='Expansion_demand_1_25x')
model.build()
model.solve()

# Save the results to a NetCDF file
output_file = "UitgeestNoord_results_Expansion_demand_1_25x.nc"
model.to_netcdf(output_file)

# Run cview command to launch the web interface
cview_command = f"cview {output_file} --port 8050"
subprocess.run(cview_command, shell=True)

#%%RUN scenario='Expansion_demand_1_5x'
model = calliope.Model("/Users/hiddegrootes/Library/Mobile Documents/com~apple~CloudDocs/03_TU DELFT/Jaar 7/Q4_MSc Thesis/02_Methods/05_Energy Modelling(Calliope)/03_UitgeestNoord_ModelMap/model.yaml", scenario='Expansion_demand_1_5x')
model.build()
model.solve()

# Save the results to a NetCDF file
output_file = "UitgeestNoord_results_Expansion_demand_1_5x.nc"
model.to_netcdf(output_file)

# Run cview command to launch the web interface
cview_command = f"cview {output_file} --port 8060"
subprocess.run(cview_command, shell=True)

#%%RUN scenario='Expansion_demand_1_75x'
model = calliope.Model("/Users/hiddegrootes/Library/Mobile Documents/com~apple~CloudDocs/03_TU DELFT/Jaar 7/Q4_MSc Thesis/02_Methods/05_Energy Modelling(Calliope)/03_UitgeestNoord_ModelMap/model.yaml", scenario='Expansion_demand_1_75x')
model.build()
model.solve()

# Save the results to a NetCDF file
output_file = "UitgeestNoord_results_Expansion_demand_1_75x.nc"
model.to_netcdf(output_file)

# Run cview command to launch the web interface
cview_command = f"cview {output_file} --port 8070"
subprocess.run(cview_command, shell=True)

#%%RUN scenario='PV_capacity_25'
model = calliope.Model("/Users/hiddegrootes/Library/Mobile Documents/com~apple~CloudDocs/03_TU DELFT/Jaar 7/Q4_MSc Thesis/02_Methods/05_Energy Modelling(Calliope)/03_UitgeestNoord_ModelMap/model.yaml", scenario='PV_capacity_25')
model.build()
model.solve()

# Save the results to a NetCDF file
output_file = "UitgeestNoord_results_PV_capacity_25.nc"
model.to_netcdf(output_file)

# Run cview command to launch the web interface
cview_command = f"cview {output_file} --port 8090"
subprocess.run(cview_command, shell=True)

#%%RUN scenario='PV_capacity_50'
model = calliope.Model("/Users/hiddegrootes/Library/Mobile Documents/com~apple~CloudDocs/03_TU DELFT/Jaar 7/Q4_MSc Thesis/02_Methods/05_Energy Modelling(Calliope)/03_UitgeestNoord_ModelMap/model.yaml", scenario='PV_capacity_50')
model.build()
model.solve()

# Save the results to a NetCDF file
output_file = "UitgeestNoord_results_PV_capacity_50.nc"
model.to_netcdf(output_file)

# Run cview command to launch the web interface
cview_command = f"cview {output_file} --port 8080"
subprocess.run(cview_command, shell=True)

#%%RUN scenario='PV_capacity_75'
model = calliope.Model("/Users/hiddegrootes/Library/Mobile Documents/com~apple~CloudDocs/03_TU DELFT/Jaar 7/Q4_MSc Thesis/02_Methods/05_Energy Modelling(Calliope)/03_UitgeestNoord_ModelMap/model.yaml", scenario='PV_capacity_75')
model.build()
model.solve()

# Save the results to a NetCDF file
output_file = "UitgeestNoord_results_PV_capacity_75.nc"
model.to_netcdf(output_file)

# Run cview command to launch the web interface
cview_command = f"cview {output_file} --port 8090"
subprocess.run(cview_command, shell=True)

#%%RUN scenario='Low_cost_0_5x'
model = calliope.Model("/Users/hiddegrootes/Library/Mobile Documents/com~apple~CloudDocs/03_TU DELFT/Jaar 7/Q4_MSc Thesis/02_Methods/05_Energy Modelling(Calliope)/03_UitgeestNoord_ModelMap/model.yaml", scenario='Low_cost_0_5x')
model.build()
model.solve()

# Save the results to a NetCDF file
output_file = "UitgeestNoord_results_Low_cost_0_5x.nc"
model.to_netcdf(output_file)

# Run cview command to launch the web interface
cview_command = f"cview {output_file} --port 8100"
subprocess.run(cview_command, shell=True)

#%%RUN scenario='Low_cost_0_7x'
model = calliope.Model("/Users/hiddegrootes/Library/Mobile Documents/com~apple~CloudDocs/03_TU DELFT/Jaar 7/Q4_MSc Thesis/02_Methods/05_Energy Modelling(Calliope)/03_UitgeestNoord_ModelMap/model.yaml", scenario='Low_cost_0_7x')
model.build()
model.solve()

# Save the results to a NetCDF file
output_file = "UitgeestNoord_results_Low_cost_0_7x.nc"
model.to_netcdf(output_file)

# Run cview command to launch the web interface
cview_command = f"cview {output_file} --port 8110"
subprocess.run(cview_command, shell=True)

#%%RUN scenario='Low_cost_0_9x'
model = calliope.Model("/Users/hiddegrootes/Library/Mobile Documents/com~apple~CloudDocs/03_TU DELFT/Jaar 7/Q4_MSc Thesis/02_Methods/05_Energy Modelling(Calliope)/03_UitgeestNoord_ModelMap/model.yaml", scenario='Low_cost_0_9x')
model.build()
model.solve()

# Save the results to a NetCDF file
output_file = "UitgeestNoord_results_Low_cost_0_9x.nc"
model.to_netcdf(output_file)

# Run cview command to launch the web interface
cview_command = f"cview {output_file} --port 8120"
subprocess.run(cview_command, shell=True)

#%%RUN scenario='High_cost_1_5x'
model = calliope.Model("/Users/hiddegrootes/Library/Mobile Documents/com~apple~CloudDocs/03_TU DELFT/Jaar 7/Q4_MSc Thesis/02_Methods/05_Energy Modelling(Calliope)/03_UitgeestNoord_ModelMap/model.yaml", scenario='High_cost_1_5x')
model.build()
model.solve()

# Save the results to a NetCDF file
output_file = "UitgeestNoord_results_High_cost_1_5x.nc"
model.to_netcdf(output_file)

# Run cview command to launch the web interface
cview_command = f"cview {output_file} --port 8130"
subprocess.run(cview_command, shell=True)

#%%RUN scenario='High_cost_2_0x'
model = calliope.Model("/Users/hiddegrootes/Library/Mobile Documents/com~apple~CloudDocs/03_TU DELFT/Jaar 7/Q4_MSc Thesis/02_Methods/05_Energy Modelling(Calliope)/03_UitgeestNoord_ModelMap/model.yaml", scenario='High_cost_2_0x')
model.build()
model.solve()

# Save the results to a NetCDF file
output_file = "UitgeestNoord_results_High_cost_2_0x.nc"
model.to_netcdf(output_file)

# Run cview command to launch the web interface
cview_command = f"cview {output_file} --port 8140"
subprocess.run(cview_command, shell=True)

#%%RUN scenario='High_cost_2_5x'
model = calliope.Model("/Users/hiddegrootes/Library/Mobile Documents/com~apple~CloudDocs/03_TU DELFT/Jaar 7/Q4_MSc Thesis/02_Methods/05_Energy Modelling(Calliope)/03_UitgeestNoord_ModelMap/model.yaml", scenario='High_cost_2_5x')
model.build()
model.solve()

# Save the results to a NetCDF file
output_file = "UitgeestNoord_results_High_cost_2_5x.nc"
model.to_netcdf(output_file)

# Run cview command to launch the web interface
cview_command = f"cview {output_file} --port 8150"
subprocess.run(cview_command, shell=True)

#%%RUN scenario='export_for_revenue_negativeprice_installed'
model = calliope.Model("/Users/hiddegrootes/Library/Mobile Documents/com~apple~CloudDocs/03_TU DELFT/Jaar 7/Q4_MSc Thesis/02_Methods/05_Energy Modelling(Calliope)/03_UitgeestNoord_ModelMap/model.yaml", scenario='export_for_revenue_negativeprice')
model.build()
model.solve()

# Save the results to a NetCDF file
output_file = "UitgeestNoord_results_export_for_revenue_negativeprice_installed.nc"
model.to_netcdf(output_file)

# Run cview command to launch the web interface
cview_command = f"cview {output_file} --port 8220"
subprocess.run(cview_command, shell=True)

#%%RUN scenario='Cost_storage_cap_S1_nogrid_sink'
# Define and build the model
model = calliope.Model("/Users/hiddegrootes/Library/Mobile Documents/com~apple~CloudDocs/03_TU DELFT/Jaar 7/Q4_MSc Thesis/02_Methods/05_Energy Modelling(Calliope)/03_UitgeestNoord_ModelMap/model.yaml", scenario='Cost_storage_cap_S1_nogrid_sink')
model.build()
model.solve()

# Save the results to a NetCDF file
output_file = "UitgeestNoord_results_Cost_storage_cap_S1_nogridSink.nc"
model.to_netcdf(output_file)

# Run cview command to launch the web interface
cview_command = f'cview "{output_file}" --port 8300'
subprocess.run(cview_command, shell=True)

#%%RUN scenario='Cost_storage_cap_S2_nogrid_sink'
# Define and build the model
model = calliope.Model("/Users/hiddegrootes/Library/Mobile Documents/com~apple~CloudDocs/03_TU DELFT/Jaar 7/Q4_MSc Thesis/02_Methods/05_Energy Modelling(Calliope)/03_UitgeestNoord_ModelMap/model.yaml", scenario='Cost_storage_cap_S2_nogrid_sink')
model.build()
model.solve()

# Save the results to a NetCDF file
output_file = "UitgeestNoord_results_Cost_storage_cap_S2_nogrid_sink.nc"
model.to_netcdf(output_file)

# Run cview command to launch the web interface
cview_command = f'cview "{output_file}" --port 8310'
subprocess.run(cview_command, shell=True)

#%%RUN scenario='Cost_storage_cap_S3_nogrid_sink'
# Define and build the model
model = calliope.Model("/Users/hiddegrootes/Library/Mobile Documents/com~apple~CloudDocs/03_TU DELFT/Jaar 7/Q4_MSc Thesis/02_Methods/05_Energy Modelling(Calliope)/03_UitgeestNoord_ModelMap/model.yaml", scenario='Cost_storage_cap_S3_nogrid_sink')
model.build()
model.solve()

# Save the results to a NetCDF file
output_file = "UitgeestNoord_results_Cost_storage_cap_S3_nogrid_sink.nc"
model.to_netcdf(output_file)

# Run cview command to launch the web interface
cview_command = f'cview "{output_file}" --port 8320'
subprocess.run(cview_command, shell=True)

#%%RUN scenario='Cost_storage_cap_S3_300_nogrid_sink'
# Define and build the model
model = calliope.Model("/Users/hiddegrootes/Library/Mobile Documents/com~apple~CloudDocs/03_TU DELFT/Jaar 7/Q4_MSc Thesis/02_Methods/05_Energy Modelling(Calliope)/03_UitgeestNoord_ModelMap/model.yaml", scenario='Cost_storage_cap_S3_300_nogrid_sink')
model.build()
model.solve()

# Save the results to a NetCDF file
output_file = "UitgeestNoord_results_Cost_storage_cap_S3_300_nogrid_sink.nc"
model.to_netcdf(output_file)

# Run cview command to launch the web interface
cview_command = f'cview "{output_file}" --port 8320'
subprocess.run(cview_command, shell=True)

#%%RUN scenario='Cost_storage_cap_S4_nogrid_sink'
# Define and build the model
model = calliope.Model("/Users/hiddegrootes/Library/Mobile Documents/com~apple~CloudDocs/03_TU DELFT/Jaar 7/Q4_MSc Thesis/02_Methods/05_Energy Modelling(Calliope)/03_UitgeestNoord_ModelMap/model.yaml", scenario='Cost_storage_cap_S4_nogrid_sink')
model.build()
model.solve()

# Save the results to a NetCDF file
output_file = "UitgeestNoord_results_Cost_storage_cap_S4_nogrid_sink.nc"
model.to_netcdf(output_file)

# Run cview command to launch the web interface
cview_command = f'cview "{output_file}" --port 8320'
subprocess.run(cview_command, shell=True)

#%%RUN scenario='Battery_limit_S1_nogrid_sink'
model = calliope.Model("/Users/hiddegrootes/Library/Mobile Documents/com~apple~CloudDocs/03_TU DELFT/Jaar 7/Q4_MSc Thesis/02_Methods/05_Energy Modelling(Calliope)/03_UitgeestNoord_ModelMap/model.yaml", scenario='Battery_limit_S1_nogrid_sink')
model.build()
model.solve()

# Save the results to a NetCDF file
output_file = "UitgeestNoord_results_Battery_limit_S1_nogrid_sink.nc"
model.to_netcdf(output_file)

# Run cview command to launch the web interface
cview_command = f"cview {output_file} --port 8330"
subprocess.run(cview_command, shell=True)

#%%RUN scenario='Battery_limit_S2_nogrid_sink'
model = calliope.Model("/Users/hiddegrootes/Library/Mobile Documents/com~apple~CloudDocs/03_TU DELFT/Jaar 7/Q4_MSc Thesis/02_Methods/05_Energy Modelling(Calliope)/03_UitgeestNoord_ModelMap/model.yaml", scenario='Battery_limit_S2_nogrid_sink')
model.build()
model.solve()

# Save the results to a NetCDF file
output_file = "UitgeestNoord_results_Battery_limit_S2_nogrid_sink.nc"
model.to_netcdf(output_file)

# Run cview command to launch the web interface
cview_command = f"cview {output_file} --port 8340"
subprocess.run(cview_command, shell=True)

#%%RUN scenario='Battery_limit_S3_nogrid_sink'
model = calliope.Model("/Users/hiddegrootes/Library/Mobile Documents/com~apple~CloudDocs/03_TU DELFT/Jaar 7/Q4_MSc Thesis/02_Methods/05_Energy Modelling(Calliope)/03_UitgeestNoord_ModelMap/model.yaml", scenario='Battery_limit_S3_nogrid_sink')
model.build()
model.solve()

# Save the results to a NetCDF file
output_file = "UitgeestNoord_results_Battery_limit_S3_nogrid_sink.nc"
model.to_netcdf(output_file)

# Run cview command to launch the web interface
cview_command = f"cview {output_file} --port 8350"
subprocess.run(cview_command, shell=True)

#%%RUN scenario='Battery_limit_S4_nogrid_sink'
model = calliope.Model("/Users/hiddegrootes/Library/Mobile Documents/com~apple~CloudDocs/03_TU DELFT/Jaar 7/Q4_MSc Thesis/02_Methods/05_Energy Modelling(Calliope)/03_UitgeestNoord_ModelMap/model.yaml", scenario='Battery_limit_S4_nogrid_sink')
model.build()
model.solve()

# Save the results to a NetCDF file
output_file = "UitgeestNoord_results_Battery_limit_S4_nogrid_sink.nc"
model.to_netcdf(output_file)

# Run cview command to launch the web interface
cview_command = f"cview {output_file} --port 8350"
subprocess.run(cview_command, shell=True)

#%%RUN scenario='Expansion_demand_1_25x_nogrid_sink'
model = calliope.Model("/Users/hiddegrootes/Library/Mobile Documents/com~apple~CloudDocs/03_TU DELFT/Jaar 7/Q4_MSc Thesis/02_Methods/05_Energy Modelling(Calliope)/03_UitgeestNoord_ModelMap/model.yaml", scenario='Expansion_demand_1_25x_nogrid_sink')
model.build()
model.solve()

# Save the results to a NetCDF file
output_file = "UitgeestNoord_results_Expansion_demand_1_25x_nogrid_sink.nc"
model.to_netcdf(output_file)

# Run cview command to launch the web interface
cview_command = f"cview {output_file} --port 8360"
subprocess.run(cview_command, shell=True)

#%%RUN scenario='Expansion_demand_1_5x_nogrid_sink'
model = calliope.Model("/Users/hiddegrootes/Library/Mobile Documents/com~apple~CloudDocs/03_TU DELFT/Jaar 7/Q4_MSc Thesis/02_Methods/05_Energy Modelling(Calliope)/03_UitgeestNoord_ModelMap/model.yaml", scenario='Expansion_demand_1_5x_nogrid_sink')
model.build()
model.solve()

# Save the results to a NetCDF file
output_file = "UitgeestNoord_results_Expansion_demand_1_5x_nogrid_sink.nc"
model.to_netcdf(output_file)

# Run cview command to launch the web interface
cview_command = f"cview {output_file} --port 8370"
subprocess.run(cview_command, shell=True)

#%%RUN scenario='Expansion_demand_1_75x_nogrid_sink'
model = calliope.Model("/Users/hiddegrootes/Library/Mobile Documents/com~apple~CloudDocs/03_TU DELFT/Jaar 7/Q4_MSc Thesis/02_Methods/05_Energy Modelling(Calliope)/03_UitgeestNoord_ModelMap/model.yaml", scenario='Expansion_demand_1_75x_nogrid_sink')
model.build()
model.solve()

# Save the results to a NetCDF file
output_file = "UitgeestNoord_results_Expansion_demand_1_75x_nogrid_sink.nc"
model.to_netcdf(output_file)

# Run cview command to launch the web interface
cview_command = f"cview {output_file} --port 8380"
subprocess.run(cview_command, shell=True)

  #%%RUN scenario='PV_capacity_25_nogrid_sink'
model = calliope.Model("/Users/hiddegrootes/Library/Mobile Documents/com~apple~CloudDocs/03_TU DELFT/Jaar 7/Q4_MSc Thesis/02_Methods/05_Energy Modelling(Calliope)/03_UitgeestNoord_ModelMap/model.yaml", scenario='PV_capacity_25_nogrid_sink')
model.build()
model.solve()

# Save the results to a NetCDF file
output_file = "UitgeestNoord_results_PV_capacity_25_nogrid_sink.nc"
model.to_netcdf(output_file)

# Run cview command to launch the web interface
cview_command = f"cview {output_file} --port 8390"
subprocess.run(cview_command, shell=True)

#%%RUN scenario='PV_capacity_50_nogrid_sink'
model = calliope.Model("/Users/hiddegrootes/Library/Mobile Documents/com~apple~CloudDocs/03_TU DELFT/Jaar 7/Q4_MSc Thesis/02_Methods/05_Energy Modelling(Calliope)/03_UitgeestNoord_ModelMap/model.yaml", scenario='PV_capacity_50_nogrid_sink')
model.build()
model.solve()

# Save the results to a NetCDF file
output_file = "UitgeestNoord_results_PV_capacity_50_nogrid_sink.nc"
model.to_netcdf(output_file)

# Run cview command to launch the web interface
cview_command = f"cview {output_file} --port 8400"
subprocess.run(cview_command, shell=True)

#%%RUN scenario='PV_capacity_75_nogrid_sink'
model = calliope.Model("/Users/hiddegrootes/Library/Mobile Documents/com~apple~CloudDocs/03_TU DELFT/Jaar 7/Q4_MSc Thesis/02_Methods/05_Energy Modelling(Calliope)/03_UitgeestNoord_ModelMap/model.yaml", scenario='PV_capacity_75_nogrid_sink')
model.build()
model.solve()

# Save the results to a NetCDF file
output_file = "UitgeestNoord_results_PV_capacity_75_nogrid_sink.nc"
model.to_netcdf(output_file)

# Run cview command to launch the web interface
cview_command = f"cview {output_file} --port 8410"
subprocess.run(cview_command, shell=True)

#%%RUN scenario='Low_cost_0_5x_nogrid_sink'
model = calliope.Model("/Users/hiddegrootes/Library/Mobile Documents/com~apple~CloudDocs/03_TU DELFT/Jaar 7/Q4_MSc Thesis/02_Methods/05_Energy Modelling(Calliope)/03_UitgeestNoord_ModelMap/model.yaml", scenario='Low_cost_0_5x_nogrid_sink')
model.build()
model.solve()

# Save the results to a NetCDF file
output_file = "UitgeestNoord_results_Low_cost_0_5x_nogrid_sink.nc"
model.to_netcdf(output_file)

# Run cview command to launch the web interface
cview_command = f"cview {output_file} --port 8420"
subprocess.run(cview_command, shell=True)

#%%RUN scenario='Low_cost_0_7x_nogrid_sink'
model = calliope.Model("/Users/hiddegrootes/Library/Mobile Documents/com~apple~CloudDocs/03_TU DELFT/Jaar 7/Q4_MSc Thesis/02_Methods/05_Energy Modelling(Calliope)/03_UitgeestNoord_ModelMap/model.yaml", scenario='Low_cost_0_7x_nogrid_sink')
model.build()
model.solve()

# Save the results to a NetCDF file
output_file = "UitgeestNoord_results_Low_cost_0_7x_nogrid_sink.nc"
model.to_netcdf(output_file)

# Run cview command to launch the web interface
cview_command = f"cview {output_file} --port 8430"
subprocess.run(cview_command, shell=True)

#%%RUN scenario='Low_cost_0_9x_nogrid_sink'
model = calliope.Model("/Users/hiddegrootes/Library/Mobile Documents/com~apple~CloudDocs/03_TU DELFT/Jaar 7/Q4_MSc Thesis/02_Methods/05_Energy Modelling(Calliope)/03_UitgeestNoord_ModelMap/model.yaml", scenario='Low_cost_0_9x_nogrid_sink')
model.build()
model.solve()

# Save the results to a NetCDF file
output_file = "UitgeestNoord_results_Low_cost_0_9x_nogrid_sink.nc"
model.to_netcdf(output_file)

# Run cview command to launch the web interface
cview_command = f"cview {output_file} --port 8440"
subprocess.run(cview_command, shell=True)

#%%RUN scenario='High_cost_1_5x_nogrid_sink'
model = calliope.Model("/Users/hiddegrootes/Library/Mobile Documents/com~apple~CloudDocs/03_TU DELFT/Jaar 7/Q4_MSc Thesis/02_Methods/05_Energy Modelling(Calliope)/03_UitgeestNoord_ModelMap/model.yaml", scenario='High_cost_1_5x_nogrid_sink')
model.build()
model.solve()

# Save the results to a NetCDF file
output_file = "UitgeestNoord_results_High_cost_1_1x_nogrid_sink.nc"
model.to_netcdf(output_file)

# Run cview command to launch the web interface
cview_command = f"cview {output_file} --port 8450"
subprocess.run(cview_command, shell=True)

#%%RUN scenario='High_cost_2_0x_nogrid_sink'
model = calliope.Model("/Users/hiddegrootes/Library/Mobile Documents/com~apple~CloudDocs/03_TU DELFT/Jaar 7/Q4_MSc Thesis/02_Methods/05_Energy Modelling(Calliope)/03_UitgeestNoord_ModelMap/model.yaml", scenario='High_cost_2_0x_nogrid_sink')
model.build()
model.solve()

# Save the results to a NetCDF file
output_file = "UitgeestNoord_results_High_cost_2_0x_nogrid_sink.nc"
model.to_netcdf(output_file)

# Run cview command to launch the web interface
cview_command = f"cview {output_file} --port 8460"
subprocess.run(cview_command, shell=True)

#%%RUN scenario='High_cost_2_5x_nogrid_sink'
model = calliope.Model("/Users/hiddegrootes/Library/Mobile Documents/com~apple~CloudDocs/03_TU DELFT/Jaar 7/Q4_MSc Thesis/02_Methods/05_Energy Modelling(Calliope)/03_UitgeestNoord_ModelMap/model.yaml", scenario='High_cost_2_5x_nogrid_sink')
model.build()
model.solve()

# Save the results to a NetCDF file
output_file = "UitgeestNoord_results_High_cost_2_5x_nogrid_sink.nc"
model.to_netcdf(output_file)

# Run cview command to launch the web interface
cview_command = f"cview {output_file} --port 8470"
subprocess.run(cview_command, shell=True)