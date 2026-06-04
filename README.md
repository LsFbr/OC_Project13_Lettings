# Site web d'Orange County Lettings

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

## Détection, journalisation et analyse des erreurs

Le projet intègre Sentry pour la détection, la journalisation et l’analyse des erreurs applicatives.

L’application utilise le module standard Python `logging` pour produire des logs, et Sentry pour centraliser les erreurs et faciliter leur diagnostic.

### Mise en place d’un nouvel environnement

1. Créer un compte Sentry ou se connecter à Sentry.
2. Créer un nouveau projet de type Django.
3. Récupérer le DSN du projet.
4. Ajouter les variables d’environnement nécessaires :

```env
SENTRY_DSN=https://examplePublicKey@o0.ingest.sentry.io/0
SENTRY_ENVIRONMENT=production
SENTRY_RELEASE=lettings@2.0.0
DJANGO_LOG_LEVEL=INFO
```

5. Redémarrer l’application.

### Configuration actuelle

Le projet utilise les paramètres suivants :

* Sentry est activé uniquement si `SENTRY_DSN` est défini ;
* `SENTRY_ENVIRONMENT` permet d’identifier l’environnement courant ;
* `SENTRY_RELEASE` permet d’identifier la version de l’application ;
* `DJANGO_LOG_LEVEL` définit le niveau minimal des logs ;
* `send_default_pii=False` limite l’envoi automatique de données personnelles ;
* `include_local_variables=False` évite l’envoi des variables locales dans les événements Sentry.

### Désactivation

Pour désactiver Sentry sur un environnement donné, supprimer ou vider la variable d’environnement :

```env
SENTRY_DSN=
```

### Recommandations de sécurité

* ne jamais versionner le fichier `.env` ;
* ne jamais écrire le DSN directement dans le code source ;
* ne jamais journaliser de secrets, mots de passe, tokens ou clés privées ;
* configurer les variables d’environnement séparément pour chaque environnement.

## Déploiement

Le projet utilise une pipeline CI/CD basée sur GitHub Actions.

À chaque `push` sur le repository :

1. analyse du code avec Flake8 ;
2. exécution des tests avec pytest ;
3. vérification de la couverture de test minimale de 80 %.

À chaque `push` sur la branche principale (`master`), si les tests réussissent :

4. construction d’une image Docker ;
5. publication de l’image sur Docker Hub avec deux tags :

   * `latest` ;
   * le hash du commit ;
6. déploiement de l’image sur AWS Elastic Beanstalk.

L’image Docker est utilisée pour :

* l’exécution locale via Docker ;
* le déploiement sur AWS Elastic Beanstalk.

### Pré-requis

#### Environnement local

* Docker ;
* Git ;
* fichier `.env` local configuré.

#### GitHub Actions

Les secrets suivants doivent être configurés dans GitHub Actions :

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

Ces secrets sont utilisés par la pipeline CI/CD :

* `DOCKERHUB_USERNAME` : nom du compte Docker Hub ;
* `DOCKERHUB_TOKEN` : token Docker Hub utilisé pour publier l’image ;
* `AWS_ACCESS_KEY_ID` : identifiant de la clé d’accès IAM utilisée par GitHub Actions ;
* `AWS_SECRET_ACCESS_KEY` : clé secrète IAM utilisée par GitHub Actions ;
* `AWS_REGION` : région AWS utilisée pour le déploiement ;
* `EB_APPLICATION_NAME` : nom de l’application Elastic Beanstalk ;
* `EB_ENVIRONMENT_NAME` : nom de l’environnement Elastic Beanstalk ;
* `EB_S3_BUCKET` : bucket S3 technique utilisé par Elastic Beanstalk.

#### Déploiement AWS

* Compte AWS ;
* accès à la console web AWS ;
* application Elastic Beanstalk ;
* environnement Elastic Beanstalk basé sur Docker ;
* bucket S3 dédié aux fichiers statiques ;
* utilisateur IAM dédié à GitHub Actions ;
* permissions IAM permettant à GitHub Actions de déployer sur Elastic Beanstalk.

### Déploiement local avec Docker

Vérifier dans Docker Hub que l’image Docker est bien disponible publiquement.

Récupérer la dernière image publiée :

```bash
docker pull <DOCKERHUB_USERNAME>/oc-lettings:latest
```

Lancer l’application :

```bash
docker run --name oc-lettings-container --env-file .env -p 8000:8000 <DOCKERHUB_USERNAME>/oc-lettings:latest
```

Accéder à l’application :

```text
http://localhost:8000/
```

Le fichier `.env` local doit contenir au minimum :

```env
SECRET_KEY=<CLE-SECRETE-APPLICATION-DJANGO>
DEBUG=False
ALLOWED_HOSTS=localhost,127.0.0.1
```

En local, ne pas définir `USE_S3=True` sauf si des identifiants AWS locaux sont configurés.

Si l’image locale n’est pas à jour, exécuter :

```bash
docker rmi <DOCKERHUB_USERNAME>/oc-lettings:latest
docker pull <DOCKERHUB_USERNAME>/oc-lettings:latest
```

### Déploiement sur AWS Elastic Beanstalk

#### Étape 1 : création de l’application

1. Se connecter à la console AWS.
2. Aller dans `Elastic Beanstalk`.
3. Créer une nouvelle application.
4. Nommer l’application, par exemple `oc-lettings`.

#### Étape 2 : création de l’environnement

1. Créer un nouvel environnement.
2. Choisir :

   * `Niveau d’environnement` : `Environnement serveur web` ;
   * `Plateforme` : `Docker`.
3. Valider la création de l’environnement.

#### Étape 3 : création de l’utilisateur IAM pour GitHub Actions

1. Aller dans `IAM`.
2. Créer un utilisateur dédié à GitHub Actions, par exemple `github-actions-deploy`.
3. Ne pas donner d’accès console à cet utilisateur.
4. Créer une clé d’accès pour cet utilisateur.
5. Copier les valeurs :

   * `AWS_ACCESS_KEY_ID` ;
   * `AWS_SECRET_ACCESS_KEY`.
6. Ajouter ces valeurs dans les secrets GitHub Actions du repository.

#### Étape 4 : permissions IAM

Créer ou attacher à l’utilisateur IAM `github-actions-deploy` une politique permettant à GitHub Actions de :

* envoyer l’archive de déploiement dans le bucket S3 Elastic Beanstalk ;
* créer une nouvelle version d’application Elastic Beanstalk ;
* mettre à jour l’environnement Elastic Beanstalk ;
* accéder aux ressources AWS nécessaires au déploiement, notamment :

  * `Elastic Beanstalk` ;
  * `S3` ;
  * `CloudFormation` ;
  * `EC2` ;
  * `Auto Scaling`.

#### Étape 5 : secrets GitHub Actions

Dans le repository GitHub, aller dans :

```text
Settings > Secrets and variables > Actions
```

Ajouter les secrets suivants :

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

Aucune valeur sensible ne doit être écrite directement dans le code, dans le README ou dans le fichier `.github/workflows/ci.yml`.

#### Étape 6 : configuration des fichiers statiques

1. Créer un bucket S3 dédié aux fichiers statiques.
2. Autoriser la lecture publique des fichiers contenus dans le dossier `static/`.
3. Donner au rôle EC2 Elastic Beanstalk les permissions nécessaires pour écrire dans ce bucket.
4. Configurer Django avec `USE_S3=True`.

#### Étape 7 : configuration des variables d’environnement

Dans l’environnement Elastic Beanstalk, ajouter les propriétés suivantes :

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
ALLOWED_HOSTS=oc-lettings-env.eba-tihg3myt.eu-west-3.elasticbeanstalk.com
USE_S3=True
AWS_STORAGE_BUCKET_NAME=oc-lettings-static
AWS_S3_REGION_NAME=eu-west-3
SENTRY_ENVIRONMENT=production
DJANGO_LOG_LEVEL=INFO
```

`SECRET_KEY` et `SENTRY_DSN` doivent être renseignées avec de vraies valeurs propres à l’environnement de production.

#### Étape 8 : lancement du déploiement

Le déploiement complet est déclenché par un `push` sur la branche `master`.

Exemple :

```bash
git checkout master
git merge develop
git push origin master
```

GitHub Actions exécute alors :

1. les tests et le linting ;
2. la construction de l’image Docker ;
3. la publication sur Docker Hub ;
4. le déploiement sur Elastic Beanstalk.

#### Étape 9 : vérification du déploiement

Après le succès de la pipeline CI/CD :

1. aller dans `GitHub > Actions` ;
2. vérifier que les jobs suivants sont en succès :

   * `lint-and-tests` ;
   * `build-and-push-docker` ;
   * `deploy-to-aws` ;
3. aller dans `AWS > Elastic Beanstalk` ;
4. ouvrir l’environnement `oc-lettings-env` ;
5. vérifier que l’environnement est en état `Ok` ;
6. ouvrir l’URL publique de l’application ;
7. vérifier que le site est accessible et correctement stylé.

Vérifier également que les fichiers statiques sont présents dans le bucket S3 dédié :

```text
S3 > oc-lettings-static > static/
```

### Déploiement manuel de secours

Si la pipeline CI/CD n’est pas disponible, créer un fichier `Dockerrun.aws.json` :

```json
{
  "AWSEBDockerrunVersion": "1",
  "Image": {
    "Name": "<DOCKERHUB_USERNAME>/oc-lettings:latest",
    "Update": "true"
  },
  "Ports": [
    {
      "ContainerPort": 8000
    }
  ]
}
```

Créer une archive contenant uniquement ce fichier à sa racine :

```bash
zip deploy.zip Dockerrun.aws.json
```

Sous Windows PowerShell :

```powershell
Compress-Archive -Path .\Dockerrun.aws.json -DestinationPath .\deploy.zip -Force
```

Envoyer ensuite `deploy.zip` depuis la console Elastic Beanstalk avec l’action de chargement et déploiement d’une nouvelle version.
