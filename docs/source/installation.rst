Installation
============

Cette page décrit l'installation locale de l'application OC Lettings.

Prérequis
---------

Les éléments suivants doivent être disponibles sur le poste de développement :

* Python 3.12 ;
* Git ;
* un accès au dépôt GitHub du projet ;
* un environnement virtuel Python ;
* SQLite, utilisé comme base de données locale.

Cloner le dépôt
---------------

Depuis le dossier de travail souhaité :

.. code-block:: powershell

   git clone https://github.com/LsFbr/OC_Project13_Lettings.git
   cd OC_Project13_Lettings

Créer et activer l'environnement virtuel
----------------------------------------

Sous Windows :

.. code-block:: powershell

   python -m venv venv_lettings
   .\venv_lettings\Scripts\Activate.ps1

Sous Linux ou macOS :

.. code-block:: bash

   python -m venv venv_lettings
   source venv_lettings/bin/activate

Installer les dépendances
-------------------------

Une fois l'environnement virtuel activé :

.. code-block:: powershell

   pip install -r requirements.txt

Configurer les variables d'environnement
----------------------------------------

Créer un fichier ``.env`` à la racine du projet à partir du modèle
``.env_template``.

Variables principales :

.. list-table::
   :header-rows: 1
   :widths: 25 25 50

   * - Variable
     - Exemple
     - Description
   * - ``SECRET_KEY``
     - ``django-secret-key``
     - Clé secrète utilisée par Django. Cette valeur doit rester confidentielle.
   * - ``DEBUG``
     - ``True`` ou ``False``
     - Active ou désactive le mode debug de Django.
   * - ``ALLOWED_HOSTS``
     - ``localhost,127.0.0.1``
     - Liste des hôtes autorisés à servir l'application.
   * - ``SENTRY_DSN``
     - ``https://...``
     - DSN du projet Sentry. Peut rester vide en développement local si Sentry n'est pas utilisé.
   * - ``SENTRY_ENVIRONMENT``
     - ``development``
     - Nom de l'environnement Sentry.
   * - ``SENTRY_RELEASE``
     - ``lettings@2.0.0``
     - Version applicative associée aux événements Sentry.
   * - ``DJANGO_LOG_LEVEL``
     - ``INFO``
     - Niveau de journalisation utilisé par l'application.

Lancer le serveur de développement
----------------------------------

Démarrer l'application en local :

.. code-block:: powershell

   python manage.py runserver

L'application est ensuite accessible dans le navigateur à l'adresse suivante :

.. code-block:: text

   http://127.0.0.1:8000/

L'espace administrateur est accessible à l'adresse suivante :

.. code-block:: text

   http://127.0.0.1:8000/admin/
