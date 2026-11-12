"""Permet de lancer l'application avec ``python -m catexe``."""

from .app import main


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
