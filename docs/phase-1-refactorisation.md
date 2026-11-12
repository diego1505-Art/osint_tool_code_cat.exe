# CAT.EXE — Phase 1 : refactorisation et modularisation

## Objectif

Réduire progressivement le couplage du monolithe `catexe/app.py` sans modifier le comportement utilisateur. La stratégie est incrémentale : chaque extraction doit rester importable, testable et réversible.

## Première extraction

`catexe/core_utils.py` contient désormais les fonctions pures suivantes :

- `stamp` : horodatage de fichiers ;
- `clean_path` : nettoyage d’un chemin collé depuis un shell ;
- `haversine` : distance GPS ;
- `parse_json` : extraction tolérante d’un objet JSON.

Ces fonctions n’ont plus de dépendance à Rich, au réseau ou à l’état global de l’application.

## Structure cible

```text
catexe/
├── app.py                 # orchestration et compatibilité temporaire
├── config.py              # configuration locale
├── core_utils.py          # utilitaires purs partagés
├── diagnostics.py         # diagnostic système
├── http_client.py         # session HTTP partagée
└── modules/
    └── sources/           # adaptateurs de sources à isoler ensuite
```

## Règles pour les prochains découpages

1. Extraire d’abord les fonctions pures et les constantes.
2. Injecter les dépendances réseau, configuration et affichage au lieu de les recréer.
3. Garder les appels de menu comme façade afin de préserver l’interface actuelle.
4. Ajouter un test local avant chaque déplacement de fonctionnalité.
5. Ne jamais placer de secrets, cookies ou résultats runtime dans un module versionné.
