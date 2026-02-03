# permet de tester soda sans base de données

Soda permet de vérifier une base de données ou des dataframe python (entre autre)

sqlite n'est pas disponible, duckdb demande des installation supplémentaire et le cli n'est past intuitif

Ce projet permet donc de tester en utilisant des fichiers csv qui sont charger dans un dataframe dask

[SodaCL metrics and checks](https://docs.soda.io/soda-cl/metrics-and-checks.html)

[Validity metrics](https://docs.soda.io/soda-cl/validity-metrics.html)

# installation
sous linux lancer la commande


`sudo apt update
sudo apt install git
rm -rf test_soda
git clone https://github.com/glegoff/test_soda.git
`
`.make.sh`

# test à effectuer

dans le fichier test_soda_dask.py

## pour les client
- le nombre d'email non renseigné doit etre égale à 0. 
- Les emails doivent etre dans un format valide 
- Le nombre de noms non renseigné doit être égal à 0
- Le nombre de doublons sur les emails doit être égal à 0 
- Le nombre de doublons sur les noms doit être égal à 0
- L'âge minimal des clients doit être supérieur ou égal à 18 
- L'âge maximal des clients doit être inférieur ou égal à 100 
- Les valeurs du sexe doivent être exclusivement "F" ou "H"
- La proportion de clients sans enfant (colonne enfant) doit-elle être inférieure à 50 % ? 
  - remplacer le nom par "plus de 50 % des clients doivent avoir au moins 1 enfant"

## pour les achats
-Les valeurs dans id doivent exister dans id des clients
- Le nombre d'achats doit être supérieur à 0 
- Le montant d'achat doit être renseigné et est-il entre 1 et 10
  - doit renvoyer warning entre 1 et 10 
  - doit renvoyer fail quand c'est > 10 
- Le montant d'achat maximal doit être inférieur ou égal à 500
- Le montant d'achat minimal doit-il être supérieur ou égal à 10

# lancement des tests:

`python3 test_soda_dask.py`
