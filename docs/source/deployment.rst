Déploiement et gestion de l'application
=======================================

Cette page décrit l'organisation générale du déploiement de l'application
OC Lettings.

Principe général
----------------

L'application est conteneurisée avec Docker, puis déployée sur AWS Elastic
Beanstalk.

Le pipeline CI/CD automatise les principales étapes :

* vérification du code ;
* exécution des tests ;
* construction de l'image Docker ;
* publication de l'image ;
* déploiement sur l'environnement AWS Elastic Beanstalk.

Conteneurisation Docker
-----------------------

Le fichier ``Dockerfile`` décrit l'environnement d'exécution de l'application.

Il permet de construire une image Docker contenant l'application Django et ses
dépendances.

Exemple de construction locale :

.. code-block:: powershell

   docker build -t oc-lettings-site .

Exemple d'exécution locale avec Docker :

.. code-block:: powershell

   docker run -p 8000:8000 --env-file .env oc-lettings-site

L'application est alors accessible à l'adresse suivante :

.. code-block:: text

   http://127.0.0.1:8000/

Pipeline CI/CD
--------------

Le pipeline GitHub Actions automatise la validation et le déploiement de
l'application.

Il exécute notamment :

* le linting ;
* les tests automatisés ;
* la construction de l'image Docker ;
* la publication de l'image sur Docker Hub ;
* le déploiement sur AWS Elastic Beanstalk.

Déploiement AWS Elastic Beanstalk
---------------------------------

L'environnement AWS Elastic Beanstalk héberge l'application conteneurisée.

Les variables d'environnement nécessaires au fonctionnement de l'application sont
définies dans la configuration de l'environnement Elastic Beanstalk.

Variables d'environnement
-------------------------

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Variable
     - Rôle
   * - ``SECRET_KEY``
     - Clé secrète Django utilisée par l'application.
   * - ``DEBUG``
     - Active ou désactive le mode debug.
   * - ``ALLOWED_HOSTS``
     - Définit les hôtes autorisés à servir l'application.
   * - ``SENTRY_DSN``
     - Permet l'envoi des erreurs applicatives vers Sentry.
   * - ``SENTRY_ENVIRONMENT``
     - Identifie l'environnement d'exécution dans Sentry.
   * - ``SENTRY_RELEASE``
     - Identifie la version applicative associée aux événements Sentry.
   * - ``DJANGO_LOG_LEVEL``
     - Définit le niveau de journalisation de l'application.

Documentation
-------------

La documentation technique est générée avec Sphinx et publiée sur Read the Docs.

À chaque modification poussée sur la branche suivie par Read the Docs, un nouveau
build de documentation est lancé automatiquement.

Les étapes détaillées de configuration du déploiement, des secrets GitHub Actions
et des accès AWS sont décrites dans le README du dépôt.