# Site web d'Orange County Lettings

## Résumé

Site web d'Orange County Lettings.

## Documentation technique

La documentation technique de l'application est publiée sur Read the Docs :

https://oc-project13-lettings.readthedocs.io/fr/latest/

Le README présente les informations opérationnelles principales : installation, lancement local, Docker, déploiement et configuration CI/CD.

La documentation Read the Docs présente la documentation technique structurée : architecture, modèles de données, routes, utilisation et organisation générale du projet.

## Développement local

### Prérequis

* Compte GitHub avec accès en lecture à ce repository
* Git CLI
* SQLite3 CLI
* Interpréteur Python 3.12 ou supérieure

Dans le reste de la documentation sur le développement local, il est supposé que la commande `python` de votre OS shell exécute l'interpréteur Python ci-dessus (à moins qu'un environnement virtuel ne soit activé).

### macOS / Linux

#### Cloner le repository

* `cd /path/to/put/project/in`
* `git clone https://github.com/LsFbr/OC_Project13_Lettings.git`

#### Créer l'environnement virtuel

* `cd /path/to/OC_Project13_Lettings`
* `python -m venv venv_lettings`
* `apt-get install python3-venv` (Si l'étape précédente comporte des erreurs avec un paquet non trouvé sur Ubuntu)
* Activer l'environnement `source venv_lettings/bin/activate`
* Confirmer que la commande `python` exécute l'interpréteur Python dans l'environnement virtuel
  `which python`
* Confirmer que la version de l'interpréteur Python est la version 3.12 ou supérieure `python --version`
* Confirmer que la commande `pip` exécute l'exécutable pip dans l'environnement virtuel, `which pip`
* Pour désactiver l'environnement, `deactivate`

#### Exécuter le site

* `cd /path/to/OC_Project13_Lettings`
* `source venv_lettings/bin/activate`
* `pip install --requirement requirements.txt`
* `python manage.py runserver`
* Aller sur `http://localhost:8000` dans un navigateur.
* Confirmer que le site fonctionne et qu'il est possible de naviguer (vous devriez voir plusieurs profils et locations).

#### Linting

* `cd /path/to/OC_Project13_Lettings`
* `source venv_lettings/bin/activate`
* `flake8`

#### Tests unitaires

* `cd /path/to/OC_Project13_Lettings`
* `source venv_lettings/bin/activate`
* `pytest`

#### Base de données

* `cd /path/to/OC_Project13_Lettings`
* Ouvrir une session shell `sqlite3`
* Se connecter à la base de données `.open oc-lettings-site.sqlite3`
* Afficher les tables dans la base de données `.tables`
* Afficher les colonnes dans le tableau des profils, `pragma table_info(profiles_profile);`
* Lancer une requête sur la table des profils, `select user_id, favorite_city from
  profiles_profile where favorite_city like 'B%';`
* `.quit` pour quitter

#### Panel d'administration

* Aller sur `http://localhost:8000/admin`
* Connectez-vous avec l'utilisateur `admin`, mot de passe `Abc1234!`

### Windows

Utilisation de PowerShell, comme ci-dessus sauf :

* Pour activer l'environnement virtuel, `.\venv_lettings\Scripts\Activate.ps1`
* Remplacer `which <my-command>` par `(Get-Command <my-command>).Path`

## Variables d'environnement

L'application utilise des variables d'environnement pour séparer la configuration du code source.

Créer un fichier `.env` à la racine du projet pour l'exécution locale ou Docker.

Exemple minimal pour un lancement local :

```env
SECRET_KEY=your-local-secret-key
DEBUG=False
ALLOWED_HOSTS=localhost,127.0.0.1
DJANGO_LOG_LEVEL=INFO
```

Variables principales :

| Variable                  | Rôle                                                                            |
| ------------------------- | ------------------------------------------------------------------------------- |
| `SECRET_KEY`              | Clé secrète Django. Ne doit pas être commitée.                                  |
| `DEBUG`                   | Active ou désactive le mode debug.                                              |
| `ALLOWED_HOSTS`           | Liste des hôtes autorisés à servir l'application.                               |
| `USE_S3`                  | Active l'utilisation de S3 pour les fichiers statiques si la valeur est `True`. |
| `AWS_STORAGE_BUCKET_NAME` | Nom du bucket S3 utilisé pour les fichiers statiques.                           |
| `AWS_S3_REGION_NAME`      | Région AWS du bucket S3.                                                        |
| `SENTRY_DSN`              | DSN du projet Sentry.                                                           |
| `SENTRY_ENVIRONMENT`      | Nom de l'environnement Sentry, par exemple `development` ou `production`.       |
| `SENTRY_RELEASE`          | Version applicative associée aux événements Sentry.                             |
| `DJANGO_LOG_LEVEL`        | Niveau minimal des logs applicatifs.                                            |

Le fichier `.env` ne doit pas être commité.

En production, les variables doivent être configurées directement dans l'environnement de la plateforme de déploiement.

## Supervision avec Sentry

L'application utilise Sentry pour surveiller les erreurs d'exécution et faire remonter les logs applicatifs utiles au diagnostic.

Sentry est configuré dans `oc_lettings_site/settings.py` avec le SDK Python officiel et l'intégration Django.

Pour activer Sentry :

1. créer un compte ou se connecter à Sentry ;
2. créer un projet Sentry avec la plateforme Django ;
3. copier le DSN du projet ;
4. renseigner les variables suivantes dans l'environnement d'exécution :

```env
SENTRY_DSN=https://...
SENTRY_ENVIRONMENT=production
SENTRY_RELEASE=lettings@2.0.0
DJANGO_LOG_LEVEL=INFO
```

Le DSN ne doit pas être écrit directement dans le code source.

## Déploiement local avec Docker

Cette section décrit comment construire et exécuter l'application localement avec Docker.

### Prérequis

* Docker installé sur le poste ;
* un fichier `.env` valide à la racine du projet ;
* accès au dépôt GitHub du projet.

### Construire l'image Docker localement

Depuis la racine du projet :

```bash
docker build -t oc-lettings-site .
```

### Lancer l'application dans un conteneur

```bash
docker run --name oc-lettings-container --env-file .env -p 8000:8000 oc-lettings-site
```

L'application est ensuite accessible à l'adresse suivante :

```text
http://localhost:8000/
```

### Arrêter et supprimer le conteneur

```bash
docker stop oc-lettings-container
docker rm oc-lettings-container
```

### Commandes Docker utiles

Lister les conteneurs actifs :

```bash
docker ps
```

Lister tous les conteneurs :

```bash
docker ps -a
```

Lister les images locales :

```bash
docker images
```

Supprimer une image :

```bash
docker rmi <image_id>
```

Nettoyer les conteneurs arrêtés :

```bash
docker container prune
```

## Utilisation de l'image publiée sur Docker Hub

L'image Docker de l'application peut être récupérée depuis Docker Hub.

### Télécharger l'image

```bash
docker pull lsfbr/oc-lettings:latest
```

### Lancer l'image téléchargée depuis Docker Hub

```bash
docker run --name oc-lettings-container-from-hub --env-file .env -p 8000:8000 lsfbr/oc-lettings:latest
```

Puis ouvrir :

```text
http://localhost:8000/
```

### Publier une image Docker manuellement

Cette étape est utile uniquement si vous maintenez votre propre image Docker.

Se connecter à Docker Hub :

```bash
docker login
```

Construire une image taguée :

```bash
docker build -t <dockerhub_username>/oc-lettings:latest .
```

Publier l'image :

```bash
docker push <dockerhub_username>/oc-lettings:latest
```

## Déploiement avec le pipeline CI/CD existant

Le projet contient un pipeline GitHub Actions défini dans :

```text
.github/workflows/ci.yml
```

Le pipeline est déclenché à chaque `push`.

### Fonctionnement général

Sur toutes les branches, le pipeline exécute les contrôles de qualité :

1. installation des dépendances ;
2. linting avec `flake8` ;
3. tests avec `pytest`.

Sur la branche `master`, si les contrôles précédents réussissent, le pipeline exécute aussi :

1. construction de l'image Docker ;
2. publication de l'image sur Docker Hub ;
3. génération du fichier `Dockerrun.aws.json` ;
4. création de l'archive `deploy.zip` ;
5. envoi de l'archive vers S3 Elastic Beanstalk ;
6. création d'une nouvelle version d'application Elastic Beanstalk ;
7. mise à jour de l'environnement AWS Elastic Beanstalk.

Le déploiement complet ne se lance donc que sur `master`.

### Déclencher un déploiement

Depuis une branche de travail :

```bash
git add .
git commit -m "Update application"
git push origin <nom-de-la-branche>
```

Puis fusionner dans `master` :

```bash
git checkout master
git merge <nom-de-la-branche>
git push origin master
```

Le `push` sur `master` déclenche les jobs de construction Docker et de déploiement AWS.

### Suivre le pipeline

Dans GitHub :

```text
Repository > Actions
```

Vérifier que les jobs passent en succès.

Sur une branche autre que `master`, seul le job de linting et tests doit être exécuté.

Sur `master`, les jobs attendus sont :

```text
Linting and tests
Build and push Docker image
Deploy to AWS Elastic Beanstalk
```

### Vérifier le déploiement

Après la réussite du pipeline :

1. vérifier que l'image a été publiée sur Docker Hub ;
2. vérifier que l'environnement Elastic Beanstalk est en état `Ok` ;
3. ouvrir l'URL publique Elastic Beanstalk ;
4. vérifier que la page d'accueil s'affiche ;
5. vérifier que les pages de locations et de profils sont accessibles ;
6. vérifier que les fichiers statiques sont chargés ;
7. vérifier que les erreurs applicatives remontent dans Sentry si Sentry est configuré.

## Configurer le pipeline CI/CD avec ses propres comptes

Cette section décrit les éléments à configurer pour utiliser le pipeline avec vos propres comptes Docker Hub et AWS.

### 1. Préparer Docker Hub

Créer un compte Docker Hub, puis créer un repository pour l'application.

Exemple :

```text
<dockerhub_username>/oc-lettings
```

Créer ensuite un token d'accès Docker Hub.

Ce token sera utilisé par GitHub Actions pour publier l'image Docker.

### 2. Préparer AWS Elastic Beanstalk

Dans AWS, créer ou vérifier les ressources suivantes :

* une application Elastic Beanstalk ;
* un environnement Elastic Beanstalk utilisant la plateforme Docker ;
* un bucket S3 technique Elastic Beanstalk ;
* un bucket S3 dédié aux fichiers statiques Django ;
* un rôle EC2 Elastic Beanstalk autorisé à écrire dans le bucket S3 des fichiers statiques ;
* un utilisateur IAM dédié à GitHub Actions.

L'utilisateur IAM utilisé par GitHub Actions doit avoir les permissions nécessaires pour :

* envoyer l'archive `deploy.zip` dans le bucket S3 Elastic Beanstalk ;
* créer une version d'application Elastic Beanstalk ;
* mettre à jour l'environnement Elastic Beanstalk ;
* accéder aux ressources nécessaires au déploiement, notamment S3, Elastic Beanstalk et CloudFormation.

### 3. Configurer les secrets GitHub Actions

Dans GitHub :

```text
Repository > Settings > Secrets and variables > Actions
```

Ajouter les secrets suivants :

| Secret                  | Rôle                                                                                |
| ----------------------- | ----------------------------------------------------------------------------------- |
| `DOCKERHUB_USERNAME`    | Nom du compte Docker Hub.                                                           |
| `DOCKERHUB_TOKEN`       | Token Docker Hub utilisé pour publier l'image.                                      |
| `AWS_ACCESS_KEY_ID`     | Identifiant de la clé d'accès IAM utilisée par GitHub Actions.                      |
| `AWS_SECRET_ACCESS_KEY` | Secret de la clé d'accès IAM utilisée par GitHub Actions.                           |
| `AWS_REGION`            | Région AWS de déploiement, par exemple `eu-west-3`.                                 |
| `EB_APPLICATION_NAME`   | Nom de l'application Elastic Beanstalk.                                             |
| `EB_ENVIRONMENT_NAME`   | Nom de l'environnement Elastic Beanstalk.                                           |
| `EB_S3_BUCKET`          | Bucket S3 technique utilisé par Elastic Beanstalk pour les archives de déploiement. |

Aucune valeur sensible ne doit être écrite directement dans le code source, le README ou le fichier `ci.yml`.

### 4. Configurer les variables d'environnement Elastic Beanstalk

Dans AWS Elastic Beanstalk :

```text
Elastic Beanstalk > Environments > <environment> > Configuration > Updates, monitoring, and logging > Environment properties
```

Ajouter les variables nécessaires à l'application :

```text
SECRET_KEY
DEBUG
ALLOWED_HOSTS
USE_S3
AWS_STORAGE_BUCKET_NAME
AWS_S3_REGION_NAME
SENTRY_DSN
SENTRY_ENVIRONMENT
SENTRY_RELEASE
DJANGO_LOG_LEVEL
```

Exemple :

```env
DEBUG=False
ALLOWED_HOSTS=<url-elastic-beanstalk>
USE_S3=True
AWS_STORAGE_BUCKET_NAME=<bucket-statique>
AWS_S3_REGION_NAME=eu-west-3
SENTRY_ENVIRONMENT=production
DJANGO_LOG_LEVEL=INFO
```

`SECRET_KEY` et `SENTRY_DSN` doivent contenir de vraies valeurs propres à l'environnement. Elles ne doivent pas être commitées.

### 5. Adapter le workflow si nécessaire

Si vous utilisez un autre nom d'image Docker, un autre environnement AWS ou une autre stratégie de tag, vérifier le fichier :

```text
.github/workflows/ci.yml
```

Les éléments à adapter sont notamment :

* le nom de l'image Docker ;
* les tags publiés ;
* la région AWS ;
* le nom de l'application Elastic Beanstalk ;
* le nom de l'environnement Elastic Beanstalk ;
* le nom du bucket S3 Elastic Beanstalk.

### 6. Tester le pipeline

Avant de déployer sur `master`, tester les contrôles sur une branche de travail :

```bash
git push origin <nom-de-la-branche>
```

Vérifier dans GitHub Actions que le job de linting et tests passe.

Ensuite, fusionner sur `master` pour déclencher le déploiement complet.

## Fichiers statiques

Les fichiers statiques sont gérés différemment selon l'environnement.

### En local

Si `USE_S3` n'est pas défini ou vaut `False`, les fichiers statiques sont collectés dans :

```text
staticfiles/
```

Ils sont ensuite servis localement par WhiteNoise.

Le dossier `staticfiles/` est généré automatiquement et ne doit pas être commité.

### Sur AWS

Si `USE_S3=True`, les fichiers statiques sont envoyés dans le bucket S3 défini par :

```text
AWS_STORAGE_BUCKET_NAME
```

Le bucket S3 doit permettre la lecture publique des objets nécessaires au rendu du site.

Le rôle EC2 utilisé par Elastic Beanstalk doit avoir le droit d'écrire dans ce bucket afin que la commande suivante fonctionne au démarrage du conteneur :

```bash
python manage.py collectstatic --noinput
```

## Déploiement manuel de secours

Si le pipeline CI/CD n'est pas disponible, il est possible de déployer manuellement une image Docker déjà publiée.

Créer un fichier `Dockerrun.aws.json` à la racine du projet :

```json
{
  "AWSEBDockerrunVersion": "1",
  "Image": {
    "Name": "lsfbr/oc-lettings:latest",
    "Update": "true"
  },
  "Ports": [
    {
      "ContainerPort": 8000
    }
  ]
}
```

Si vous utilisez votre propre image Docker Hub, remplacer :

```text
lsfbr/oc-lettings:latest
```

par :

```text
<dockerhub_username>/oc-lettings:latest
```

Créer une archive contenant uniquement `Dockerrun.aws.json` à sa racine.

Sous macOS ou Linux :

```bash
zip deploy.zip Dockerrun.aws.json
```

Sous Windows PowerShell :

```powershell
Compress-Archive -Path .\Dockerrun.aws.json -DestinationPath .\deploy.zip -Force
```

Vérifier le contenu de l'archive :

```bash
tar -tf deploy.zip
```

Le résultat attendu est :

```text
Dockerrun.aws.json
```

Puis, dans AWS Elastic Beanstalk :

```text
Elastic Beanstalk > <environment> > Upload and deploy
```

Envoyer `deploy.zip`, donner une étiquette de version explicite, puis lancer le déploiement.

Après le déploiement manuel, effectuer les mêmes vérifications que pour le déploiement automatique.

## Diagnostic en cas d'échec

### Échec GitHub Actions

Si un job GitHub Actions échoue :

1. ouvrir le workflow dans l'onglet `Actions` ;
2. ouvrir le job en erreur ;
3. lire l'étape exacte qui a échoué ;
4. corriger le problème ;
5. relancer le workflow ou pousser un nouveau commit.

### Échec Docker

Vérifier notamment :

* que Docker est lancé ;
* que le fichier `.env` existe ;
* que le port `8000` n'est pas déjà utilisé ;
* que l'image existe localement ou sur Docker Hub.

Commandes utiles :

```bash
docker ps
docker ps -a
docker logs <container_id>
docker images
```

### Échec AWS Elastic Beanstalk

Vérifier dans AWS :

```text
Elastic Beanstalk > <environment> > Events
Elastic Beanstalk > <environment> > Logs
```

Causes fréquentes :

* permission IAM manquante ;
* variable d'environnement absente ;
* image Docker absente ou tag incorrect ;
* erreur pendant `collectstatic` ;
* mauvaise configuration du bucket S3 ;
* erreur applicative au démarrage du conteneur.

### Échec Sentry

Si les erreurs ne remontent pas dans Sentry, vérifier :

* que `SENTRY_DSN` est défini ;
* que `SENTRY_ENVIRONMENT` correspond à l'environnement attendu ;
* que l'application a été redémarrée après modification des variables ;
* que l'erreur testée est bien capturée par l'application.
