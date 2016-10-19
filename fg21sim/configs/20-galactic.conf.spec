# Configurations for "fg21sim"
# -*- mode: conf -*-
#
# Syntax: `ConfigObj`, https://github.com/DiffSK/configobj
#
# This file contains the point source configurations, which control the 
# amount of point sources of each types, and the output staffs. 

[extragalactic]

    # Extragalactic point sources
    [[pointsources]]
    # PS components to be simulated
    pscomponents=string_list(default=list())
    # Number of each type of point source
    # Star forming
    num_sf = integer(default=100)
    # Star bursting	
    num_sb = integer(default=100)
    # Radio quiet AGN	
    num_rq = integer(default=100)
    # Faranoff-Riley I	
    num_fr1 = integer(default=100)
    # Faranoff-Riley II	
    num_fr2 = integer(default=100)
    
    # Filename prefix for this component
    prefix_sf = string(default="SF")
    prefix_sb = string(default="SB")
    prefix_rq = string(default="RQ")
    prefix_fr1 = string(default="FRI")
    prefix_fr2 = string(default="FRII")
    
    # Whether save this point source catelogue to disk
    save = boolean(default=True)
    
    # Output directory to save the simulated catelogues
    output_dir = string(default="PS_tables")

    # Special parameters
    lumo_1400 = float(default=0.0)
