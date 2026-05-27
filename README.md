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

* `SENTRY_DSN` : DSN du projet Sentry.
* `SENTRY_ENVIRONMENT` : environnement courant, par exemple `development` ou `production`.
* `SENTRY_RELEASE` : version de l’application, par exemple `lettings@2.0.0`.
* `DJANGO_LOG_LEVEL` : niveau minimal des logs, par défaut `INFO`.

Exemple de configuration locale dans un fichier `.env` :

```env
SENTRY_DSN=https://examplePublicKey@o0.ingest.sentry.io/0
SENTRY_ENVIRONMENT=development
SENTRY_RELEASE=lettings@2.0.0
DJANGO_LOG_LEVEL=INFO
```

Le fichier `.env` ne doit pas être commité.

En production, ces variables doivent être renseignées directement dans l’environnement de la plateforme de déploiement.
