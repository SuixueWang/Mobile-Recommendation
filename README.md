# Mobile-Recommendation


Introduction 
-----------------------------
    
    This Project is about the Ali Mobile Recommendation Algorithm Competition.

Directory Structure
-----------------------------

	└── README.md                           # deacription

	# create table and load csv datasets into MySQL database.
	├── LoadAndQuery.sql


	# tool
	├── DownSample.py                       # under sampling
	├── ReadCSV.py                          # reading csv file fastly

	# processing functions
	├── GetDataSet.py                       # extracting features and getting datasets. 
	├── Main_model.py                       # main fuction
	├── Main_processing_offline.py          # functions like training, testing, and cross-validation for offline datasets
	├── Main_processing_online.py           # functions like training, testing, and selecting for online datasets

	# subdirectories
	├── FeatureSelect                       # extracting detail features, such as Item Feature, User Feature and Union Feature.
	├── UI_Label                            # getting sample's item (U,I)





