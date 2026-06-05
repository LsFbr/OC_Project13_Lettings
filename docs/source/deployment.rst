# Déploiement et gestion de l'application

Cette page présente l'organisation générale du déploiement de l'application
OC Lettings.

Les commandes détaillées, la configuration des secrets GitHub Actions et les
procédures de dépannage sont décrites dans le README du dépôt.

## Vue d'ensemble

L'application est conteneurisée avec Docker, publiée sur Docker Hub, puis
déployée sur AWS Elastic Beanstalk.

Le déploiement repose sur trois éléments principaux :

* une image Docker contenant l'application Django ;
* un pipeline GitHub Actions chargé de valider, construire et déployer
  l'application ;
* un environnement AWS Elastic Beanstalk exécutant l'image publiée.

## Pipeline CI/CD

Le pipeline GitHub Actions est déclenché à chaque `push`.

Sur les branches de travail, il exécute les contrôles de qualité :

* installation des dépendances ;
* analyse du code avec `flake8` ;
* exécution des tests avec `pytest`.

Sur la branche `master`, si les contrôles précédents réussissent, le pipeline
exécute aussi :

* la construction de l'image Docker ;
* la publication de l'image sur Docker Hub ;
* la création d'une version Elastic Beanstalk ;
* la mise à jour de l'environnement AWS.

Cette organisation évite de déployer une version dont les tests ou le linting
échouent.

## Conteneurisation

Le fichier `Dockerfile` décrit l'environnement d'exécution de l'application.

L'image Docker permet d'exécuter l'application de manière reproductible en local,
dans le pipeline CI/CD et sur l'environnement de déploiement.

Les images publiées sur Docker Hub permettent également de tester localement la
même version que celle utilisée pour le déploiement.

## Hébergement AWS

L'application est hébergée sur AWS Elastic Beanstalk avec une plateforme Docker.

Elastic Beanstalk récupère l'image Docker publiée sur Docker Hub à partir d'un
fichier `Dockerrun.aws.json` généré pendant le pipeline.

Les fichiers statiques sont stockés dans un bucket S3 dédié lorsque la variable
`USE_S3` est activée.

## Variables d'environnement

Les variables sensibles ou propres à un environnement ne sont pas stockées dans
le code source.

En production, elles sont configurées dans l'environnement Elastic Beanstalk.

.. list-table::
:header-rows: 1
:widths: 30 70

* * Variable
  * Rôle
* * `SECRET_KEY`
  * Clé secrète Django.
* * `DEBUG`
  * Active ou désactive le mode debug.
* * `ALLOWED_HOSTS`
  * Définit les hôtes autorisés à servir l'application.
* * `USE_S3`
  * Active l'utilisation de S3 pour les fichiers statiques.
* * `AWS_STORAGE_BUCKET_NAME`
  * Nom du bucket S3 utilisé pour les fichiers statiques.
* * `AWS_S3_REGION_NAME`
  * Région AWS du bucket S3.
* * `SENTRY_DSN`
  * DSN du projet Sentry.
* * `SENTRY_ENVIRONMENT`
  * Nom de l'environnement Sentry.
* * `SENTRY_RELEASE`
  * Version applicative associée aux événements Sentry.
* * `DJANGO_LOG_LEVEL`
  * Niveau minimal des logs applicatifs.

## Supervision

Sentry est utilisé pour suivre les erreurs applicatives et les logs utiles au
diagnostic.

Pour fonctionner en production, les variables `SENTRY_DSN`,
`SENTRY_ENVIRONMENT` et `SENTRY_RELEASE` doivent être configurées dans
l'environnement de déploiement.

## Vérifications après déploiement

Après un déploiement, vérifier que :

* l'environnement Elastic Beanstalk est en état opérationnel ;
* l'URL publique de l'application est accessible ;
* les pages principales du site s'affichent correctement ;
* les fichiers statiques sont chargés ;
* l'interface d'administration conserve son apparence ;
* les erreurs applicatives remontent dans Sentry si la supervision est activée.

## Documentation opérationnelle

Le README du dépôt contient les procédures détaillées pour :

* lancer l'application avec Docker ;
* récupérer l'image depuis Docker Hub ;
* configurer les secrets GitHub Actions ;
* configurer AWS Elastic Beanstalk ;
* effectuer un déploiement manuel de secours ;
* diagnostiquer les erreurs Docker, GitHub Actions, AWS ou Sentry.
