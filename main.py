#!/usr/bin/env python3
"""Point d'entrée de CAT.EXE."""

from catexe.app import main


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
