import dask.dataframe as dd
from soda.scan import Scan

# Initialisation de Soda Scan
scan = Scan()
scan.set_scan_definition_name("test")
scan.set_data_source_name("dask")

# Chargement du fichier CSV avec Dask
ddf_client = dd.read_csv("clients.csv")
ddf_achat = dd.read_csv("achats.csv")
# Ajout du DataFrame à Soda
scan.add_dask_dataframe(dataset_name="clients", dask_df=ddf_client)
scan.add_dask_dataframe(dataset_name="achats", dask_df=ddf_achat)

# Définition des règles de contrôle SodaCL
checks = """
checks for clients:
    - row_count > 0
    -
checks for achats:
    - row_count > 0
"""

scan.add_sodacl_yaml_str(checks)


# Exécution du scan
scan.execute()