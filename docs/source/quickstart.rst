Démarrage rapide
================

Cette page résume les commandes principales pour utiliser l'application en
environnement local.

Activer l'environnement virtuel
-------------------------------

Sous Windows :

.. code-block:: powershell

   .\venv_lettings\Scripts\Activate.ps1

Sous Linux ou macOS :

.. code-block:: bash

   source venv_lettings/bin/activate

Lancer le serveur local
-----------------------

Depuis la racine du projet :

.. code-block:: powershell

   python manage.py runserver

L'application est accessible à l'adresse suivante :

.. code-block:: text

   http://127.0.0.1:8000/

Accéder à l'administration
--------------------------

L'interface d'administration Django est disponible à l'adresse suivante :

.. code-block:: text

   http://127.0.0.1:8000/admin/

Un compte administrateur existant est nécessaire pour s'y connecter.

Exécuter les tests
------------------

Depuis la racine du projet :

.. code-block:: powershell

   pytest

Vérifier la couverture de tests
-------------------------------

.. code-block:: powershell

   pytest --cov=. --cov-report=term-missing

Analyser le code avec flake8
----------------------------

.. code-block:: powershell

   flake8