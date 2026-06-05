Technologies
============

Cette page présente les principales technologies utilisées par l'application
OC Lettings.

Langage et framework
--------------------

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Technologie
     - Rôle
   * - Python
     - Langage principal de l'application.
   * - Django
     - Framework web utilisé pour structurer l'application, gérer les vues,
       les modèles, les URLs et l'interface d'administration.

Base de données
---------------

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Technologie
     - Rôle
   * - SQLite
     - Base de données utilisée pour l'environnement local.
   * - Migrations Django
     - Mécanisme de suivi de l'évolution du schéma de base de données.

Qualité, tests et supervision
-----------------------------

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Outil
     - Rôle
   * - pytest
     - Exécution des tests automatisés.
   * - pytest-django
     - Intégration de pytest avec Django.
   * - pytest-cov
     - Mesure de la couverture de tests.
   * - flake8
     - Analyse statique du code Python.
   * - Sentry
     - Suivi des erreurs et des événements applicatifs.

Déploiement et exploitation
---------------------------

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Outil ou service
     - Rôle
   * - Docker
     - Création d'une image exécutable de l'application.
   * - Docker Hub
     - Registre utilisé pour publier l'image Docker.
   * - GitHub Actions
     - Automatisation du linting, des tests, de la construction Docker et du
       déploiement.
   * - AWS Elastic Beanstalk
     - Hébergement de l'application déployée.


Documentation
-------------

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Outil
     - Rôle
   * - Sphinx
     - Génération de la documentation technique à partir de fichiers
       reStructuredText.
   * - Read the Docs
     - Publication automatique de la documentation technique.