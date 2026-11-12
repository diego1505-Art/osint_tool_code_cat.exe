# CAT.EXE OSINT · GEOINT

Outil OSINT et GEOINT en ligne de commande (Python 3.11+, Rich). Il regroupe des modules de recherche sur des **données publiques**, à utiliser sur soi-même ou sur des cibles autorisées.

## Usage légal
- Testez l'outil sur **vous-même** ou sur des données publiques.
- Ne l'utilisez pas pour surveiller, harceler ou identifier une personne sans son accord.
- L'auteur n'est pas responsable d'un usage abusif.

## Ce que fait le code, et vers où il envoie
Chaque module interroge des services publics. Liste principale :
- **E-mail** : vérification MX/SPF/DMARC, fuites (XposedOrNot), comptes (Holehe reproduit en interne, sur une liste de sites).
- **IP / domaine** : ipwho.is, crt.sh, HackerTarget, CertSpotter, urlscan.io, web.archive.org.
- **Banque / véhicule / appareil** : openiban.com (IBAN), NHTSA vPIC (VIN), macvendors.com (MAC).
- **Entreprises** : BODACC (OpenDataSoft).
- **Anonymat** : passe par Tor (ports 9050/9150) si Tor est installé ; sinon le module le signale.

Aucune donnée n'est envoyée à l'auteur. Les résultats sont enregistrés localement dans `resultats/`.
Les clés API (Hunter, Windy) sont demandées à l'utilisateur et stockées sur sa machine uniquement.

## Installation
```
py -3.11 -m pip install -r requirements.txt
py -3.11 main.py
```
Windows : lancez `LANCER.bat`. `CREER_EXE.bat` produit un `.exe` avec PyInstaller.

## Vérifier le fichier
Le `.exe` publié a une empreinte SHA256 indiquée dans les Releases. Vérifiez-la avec :
```
certutil -hashfile CATEXE.exe SHA256
```

## Faux positifs antivirus
Les programmes Python compilés (PyInstaller) sont parfois signalés à tort par les antivirus. Le code source complet est ici : vous pouvez le lire et le compiler vous-même.

## Licence
MIT, voir `LICENSE`.

## Crédits
Les données d’exécution sont enregistrées localement dans `resultats/` et ne sont pas versionnées.

## Structure du projet

```text
main.py              # point d'entrée
catexe/app.py        # orchestration de l'application et modules
catexe/config.py     # configuration locale non versionnée
catexe/http_client.py# client HTTP partagé
catexe/__init__.py
lang/                # traductions intégrées
resultats/           # rapports locaux, ignorés par Git
cache/               # cache local, ignoré par Git
```

Les anciennes données de challenges et les résultats personnels ne font plus partie du dépôt.
