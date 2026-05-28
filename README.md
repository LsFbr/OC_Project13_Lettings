## Résumé

Site web d'Orange County Lettings

## Développement local

### Prérequis

- Compte GitHub avec accès en lecture à ce repository
- Git CLI
- SQLite3 CLI
- Interpréteur Python, version 3.6 ou supérieure

Dans le reste de la documentation sur le développement local, il est supposé que la commande `python` de votre OS shell exécute l'interpréteur Python ci-dessus (à moins qu'un environnement virtuel ne soit activé).

### macOS / Linux

#### Cloner le repository

- `cd /path/to/put/project/in`
- `git clone https://github.com/OpenClassrooms-Student-Center/Python-OC-Lettings-FR.git`

#### Créer l'environnement virtuel

- `cd /path/to/Python-OC-Lettings-FR`
- `python -m venv venv`
- `apt-get install python3-venv` (Si l'étape précédente comporte des erreurs avec un paquet non trouvé sur Ubuntu)
- Activer l'environnement `source venv/bin/activate`
- Confirmer que la commande `python` exécute l'interpréteur Python dans l'environnement virtuel
`which python`
- Confirmer que la version de l'interpréteur Python est la version 3.6 ou supérieure `python --version`
- Confirmer que la commande `pip` exécute l'exécutable pip dans l'environnement virtuel, `which pip`
- Pour désactiver l'environnement, `deactivate`

#### Exécuter le site

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pip install --requirement requirements.txt`
- `python manage.py runserver`
- Aller sur `http://localhost:8000` dans un navigateur.
- Confirmer que le site fonctionne et qu'il est possible de naviguer (vous devriez voir plusieurs profils et locations).

#### Linting

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `flake8`

#### Tests unitaires

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pytest`

#### Base de données

- `cd /path/to/Python-OC-Lettings-FR`
- Ouvrir une session shell `sqlite3`
- Se connecter à la base de données `.open oc-lettings-site.sqlite3`
- Afficher les tables dans la base de données `.tables`
- Afficher les colonnes dans le tableau des profils, `pragma table_info(oc_lettings_site_profile);`
- Lancer une requête sur la table des profils, `select user_id, favorite_city from
  oc_lettings_site_profile where favorite_city like 'B%';`
- `.quit` pour quitter

#### Panel d'administration

- Aller sur `http://localhost:8000/admin`
- Connectez-vous avec l'utilisateur `admin`, mot de passe `Abc1234!`

### Windows

Utilisation de PowerShell, comme ci-dessus sauf :

- Pour activer l'environnement virtuel, `.\venv\Scripts\Activate.ps1` 
- Remplacer `which <my-command>` par `(Get-Command <my-command>).Path`

## Mise en place de Sentry

L’application utilise Sentry pour surveiller les erreurs d’exécution et faire remonter les logs applicatifs utiles au diagnostic.

Sentry est configuré dans `oc_lettings_site/settings.py` avec le SDK Python officiel et l’intégration Django. Le DSN Sentry est lu depuis les variables d’environnement afin de ne pas stocker d’information sensible dans le code source.

### 1. Créer un projet Sentry

1. Créer un compte ou se connecter à Sentry.
2. Créer un nouveau projet.
3. Choisir `Django` comme plateforme du projet.
4. Copier le DSN fourni par Sentry.

Le DSN permet au SDK Sentry d’envoyer les événements vers le bon projet. Il ne doit jamais être écrit directement dans le code source.

### 2. Configurer les variables d’environnement

Les variables suivantes doivent être configurées en local, dans Docker ou sur la plateforme de déploiement :

* `SECRET_KEY` : clé secrète pour la sécurité de l'application.
* `DEBUG=False` : mode de développement. Par défaut `False`.
* `ALLOWED_HOSTS=localhost,127.0.0.1` : liste des hôtes autorisés. Par défaut `localhost,127.0.0.1`.
* `SENTRY_DSN` : DSN du projet Sentry.
* `SENTRY_ENVIRONMENT` : environnement courant, par exemple `development` ou `production`.
* `SENTRY_RELEASE` : version de l’application, par exemple `lettings@2.0.0`.
* `DJANGO_LOG_LEVEL` : niveau minimal des logs, par défaut `INFO`.

Exemple de configuration locale dans un fichier `.env` :



Le fichier `.env` ne doit pas être commité.

En production, ces variables doivent être renseignées directement dans l’environnement de la plateforme de déploiement.

## Déploiement

Cette section décrit le fonctionnement du déploiement, la configuration requise et les étapes à suivre pour déployer une nouvelle version de l’application.

### 1. Récapitulatif haut niveau du fonctionnement du déploiement

Le déploiement est automatisé avec GitHub Actions.

À chaque `push` sur le repository, le workflow GitHub Actions est déclenché.

Le job `lint-and-tests` est exécuté à chaque `push`, quelle que soit la branche. Il installe les dépendances, lance `flake8`, puis exécute les tests avec une couverture minimale attendue de 80 %.

Les jobs suivants ne sont exécutés que si le `push` concerne la branche `master` et si le job précédent a réussi :

1. `build-and-push-docker` : construit une image Docker de l’application, puis la publie sur Docker Hub ;
2. `deploy-to-aws` : génère un fichier `Dockerrun.aws.json`, crée une archive `deploy.zip`, l’envoie dans le bucket S3 Elastic Beanstalk, crée une nouvelle version d’application Elastic Beanstalk, puis met à jour l’environnement AWS.

Le déploiement ne démarre donc que si les tests et la construction de l’image Docker réussissent.

L’application est hébergée sur AWS Elastic Beanstalk avec la plateforme Docker. Elastic Beanstalk ne construit pas lui-même l’image Docker : il récupère l’image publiée sur Docker Hub grâce au fichier `Dockerrun.aws.json` généré par GitHub Actions.

Les fichiers statiques sont gérés différemment selon l’environnement :

* en local, ils sont collectés dans `staticfiles/` et servis par WhiteNoise ;
* sur AWS, ils sont envoyés vers un bucket S3 dédié grâce à `django-storages` lorsque `USE_S3=True`.

### 2. Configuration requise pour que le déploiement fonctionne correctement

Avant de lancer un déploiement, les éléments suivants doivent être configurés.

#### GitHub Actions

Le repository GitHub doit contenir le fichier suivant :

```text
.github/workflows/ci.yml
```

Ce fichier définit les jobs de CI/CD. Il doit contenir :

* un job de linting et de tests ;
* un job de construction et publication de l’image Docker ;
* un job de déploiement vers AWS Elastic Beanstalk ;
* des dépendances entre les jobs avec `needs`, afin que le déploiement ne soit exécuté qu’après la réussite des étapes précédentes.

Les secrets suivants doivent être configurés dans GitHub :

```text
DOCKERHUB_USERNAME
DOCKERHUB_TOKEN
AWS_ACCESS_KEY_ID
AWS_SECRET_ACCESS_KEY
AWS_REGION
EB_APPLICATION_NAME
EB_ENVIRONMENT_NAME
EB_S3_BUCKET
```

Rôle de chaque secret :

* `DOCKERHUB_USERNAME` : nom du compte Docker Hub ;
* `DOCKERHUB_TOKEN` : token Docker Hub utilisé pour publier l’image ;
* `AWS_ACCESS_KEY_ID` : identifiant de la clé d’accès IAM utilisée par GitHub Actions ;
* `AWS_SECRET_ACCESS_KEY` : secret de la clé d’accès IAM utilisée par GitHub Actions ;
* `AWS_REGION` : région AWS de déploiement, par exemple `eu-west-3` ;
* `EB_APPLICATION_NAME` : nom de l’application Elastic Beanstalk ;
* `EB_ENVIRONMENT_NAME` : nom de l’environnement Elastic Beanstalk ;
* `EB_S3_BUCKET` : bucket S3 technique utilisé par Elastic Beanstalk pour stocker les archives de déploiement.

Aucune valeur sensible ne doit être écrite directement dans le code, dans le README ou dans `ci.yml`.

#### Docker Hub

Un repository Docker Hub doit exister pour l’application.

Dans ce projet, l’image publiée par le workflow est de la forme :

```text
<DOCKERHUB_USERNAME>/oc-lettings:<tag>
```

Le workflow publie deux tags :

```text
<DOCKERHUB_USERNAME>/oc-lettings:<hash_du_commit>
<DOCKERHUB_USERNAME>/oc-lettings:latest
```

Le tag basé sur le hash du commit permet de relier une version déployée à un commit précis. Le tag `latest` permet de récupérer facilement la dernière image publiée.

#### AWS Elastic Beanstalk

AWS doit contenir :

* une application Elastic Beanstalk ;
* un environnement Elastic Beanstalk basé sur la plateforme Docker ;
* un bucket S3 technique Elastic Beanstalk, généralement nommé sous la forme `elasticbeanstalk-<region>-<account-id>` ;
* un bucket S3 dédié aux fichiers statiques Django ;
* un rôle EC2 Elastic Beanstalk autorisé à écrire dans le bucket S3 des fichiers statiques ;
* un utilisateur IAM dédié à GitHub Actions.

L’utilisateur IAM utilisé par GitHub Actions doit avoir les permissions nécessaires pour :

* envoyer `deploy.zip` dans le bucket S3 Elastic Beanstalk ;
* créer une version d’application Elastic Beanstalk ;
* mettre à jour l’environnement Elastic Beanstalk ;
* accéder aux ressources AWS utilisées par Elastic Beanstalk pendant le déploiement, notamment S3 et CloudFormation.

#### Variables d’environnement Elastic Beanstalk

Les variables suivantes doivent être définies dans l’environnement Elastic Beanstalk :

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

Exemple de configuration AWS :

```text
DEBUG=False
ALLOWED_HOSTS=oc-lettings-env.eba-tihg3myt.eu-west-3.elasticbeanstalk.com
USE_S3=True
AWS_STORAGE_BUCKET_NAME=lsfbr-oc-lettings-static
AWS_S3_REGION_NAME=eu-west-3
SENTRY_ENVIRONMENT=production
DJANGO_LOG_LEVEL=INFO
```

`SECRET_KEY` et `SENTRY_DSN` doivent contenir de vraies valeurs propres à l’environnement de déploiement. Elles ne doivent pas être commitées.

#### Fichiers statiques

Le bucket S3 dédié aux fichiers statiques doit être configuré pour permettre la lecture publique des objets situés dans le dossier `static/`.

Le rôle EC2 utilisé par Elastic Beanstalk doit avoir le droit d’écrire dans ce bucket afin que la commande suivante, exécutée au démarrage du conteneur, puisse envoyer les fichiers statiques vers S3 :

```bash
python manage.py collectstatic --noinput
```

En local, si `USE_S3` n’est pas défini, les fichiers statiques sont collectés dans `staticfiles/` et servis par WhiteNoise. Le dossier `staticfiles/` est généré automatiquement et ne doit pas être commité.

### 3. Étapes nécessaires pour effectuer le déploiement

#### Étape 1 — Vérifier l’état du projet localement

Avant de déployer, vérifier que le projet fonctionne localement :

```bash
python manage.py check
flake8
pytest --cov --cov-fail-under=80
```

Corriger les erreurs éventuelles avant de continuer.

#### Étape 2 — Vérifier les fichiers à committer

Avant le commit, vérifier l’état Git :

```bash
git status
```

Les fichiers générés ne doivent pas être commités, notamment :

```text
.env
staticfiles/
deploy.zip
```

Le fichier `.env` doit rester local. Les secrets doivent être configurés dans GitHub Actions ou dans Elastic Beanstalk selon leur usage.

#### Étape 3 — Pousser les modifications sur GitHub

Créer un commit puis pousser les modifications. Le job de linting et de tests se lance sur tous les `push` :

```bash
git add .
git commit -m "Update application"
git push
```

Le `push` déclenche automatiquement le workflow GitHub Actions.

Pour déclencher la conteneurisation et le déploiement, les modifications doivent ensuite être présentes sur la branche `master`. En pratique, il faut fusionner la branche de travail dans `master`, puis pousser `master` sur GitHub :

```bash
git checkout master
git merge <nom-de-la-branche-de-travail>
git push origin master
```

Seul un `push` sur `master` déclenche les jobs `build-and-push-docker` et `deploy-to-aws`.

#### Étape 4 — Suivre le workflow GitHub Actions

Dans GitHub :

```text
Repository > Actions > workflow CI
```

Sur une branche autre que `master`, vérifier que seul le job suivant passe en succès :

```text
Linting and tests
```

Sur la branche `master`, vérifier que les trois jobs passent en succès :

```text
Linting and tests
Build and push Docker image
Deploy to AWS Elastic Beanstalk
```

Si un job échoue :

1. ouvrir le job en erreur ;
2. lire l’étape exacte qui a échoué ;
3. corriger le problème ;
4. relancer le workflow ou pousser un nouveau commit.

#### Étape 5 — Vérifier l’image Docker publiée

Après la réussite du job `build-and-push-docker`, vérifier sur Docker Hub qu’une nouvelle image a été publiée.

Il est aussi possible de tester l’image localement :

```bash
docker pull lsfbr/oc-lettings:latest
docker run --name oc-lettings-container --env-file .env -p 8000:8000 lsfbr/oc-lettings:latest
```

Puis ouvrir :

```text
http://localhost:8000/
```

Le fichier `.env` local doit contenir au minimum :

```env
SECRET_KEY=your-local-secret-key
DEBUG=False
ALLOWED_HOSTS=localhost,127.0.0.1
```

En local, ne pas définir `USE_S3=True` sauf si des identifiants AWS locaux sont configurés. Sans `USE_S3`, les fichiers statiques sont servis localement par WhiteNoise après `collectstatic`.

#### Étape 6 — Vérifier le déploiement AWS

Après la réussite du job `deploy-to-aws`, ouvrir la console AWS Elastic Beanstalk :

```text
Elastic Beanstalk > Applications > oc-lettings > oc-lettings-env
```

Vérifier que :

* l’environnement est en état `Ok` ;
* une nouvelle version d’application a été créée ;
* l’URL publique Elastic Beanstalk est accessible ;
* la page d’accueil s’affiche correctement ;
* les fichiers CSS et images sont bien chargés ;
* l’interface d’administration reste correctement stylée.

Vérifier également le bucket S3 des fichiers statiques :

```text
S3 > lsfbr-oc-lettings-static > static/
```

Le dossier `static/` doit contenir les fichiers CSS, JavaScript, images et fichiers d’administration Django collectés par `collectstatic`.

#### Étape 7 — En cas d’échec du déploiement

Si le job GitHub Actions échoue pendant le déploiement AWS, consulter d’abord les logs du job `deploy-to-aws`.

Si GitHub Actions indique une erreur AWS, vérifier ensuite dans AWS :

```text
Elastic Beanstalk > oc-lettings-env > Events
Elastic Beanstalk > oc-lettings-env > Logs
```

Les erreurs les plus probables sont :

* permission IAM manquante pour l’utilisateur GitHub Actions ;
* variable d’environnement manquante dans Elastic Beanstalk ;
* image Docker absente ou tag incorrect sur Docker Hub ;
* erreur lors de `collectstatic` ;
* mauvaise configuration du bucket S3 des fichiers statiques.

#### Étape 8 — Déploiement manuel de secours

Si le déploiement automatique n’est pas disponible, il est possible de déployer manuellement une image Docker déjà publiée.

Créer un fichier `Dockerrun.aws.json` pointant vers l’image Docker à déployer :

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

Créer ensuite une archive contenant uniquement `Dockerrun.aws.json` à sa racine.

Sous macOS ou Linux :

```bash
zip deploy.zip Dockerrun.aws.json
```

Sous Windows PowerShell :

```powershell
Compress-Archive -Path .\Dockerrun.aws.json -DestinationPath .\deploy.zip -Force
```

Vérifier le contenu de l’archive :

```bash
tar -tf deploy.zip
```

Le résultat attendu est :

```text
Dockerrun.aws.json
```

Puis, dans AWS Elastic Beanstalk :

```text
Elastic Beanstalk > oc-lettings-env > Upload and deploy
```

Envoyer `deploy.zip`, donner une étiquette de version explicite, puis lancer le déploiement.

Après le déploiement manuel, effectuer les mêmes vérifications que pour le déploiement automatique.


## Docker
commandes utiles :
- `docker build -t oc-lettings-site .`
- `docker run --name oc-lettings-container-from-hub --env-file .env -p 8000:8000 lsfbr/oc-lettings:latest`
- `docker push lsfbr/oc-lettings:latest`
- `docker pull lsfbr/oc-lettings:latest`
- `docker start <container_id>`
- `docker restart <container_id>`
- `docker stop <container_id>`
- `docker ps`
- `docker ps -a`
- `docker rm <container_id>`
- `docker rmi <image_id>`
- `docker images`
- `docker container prune`
