Base de données et modèles
==========================

L'application utilise une base de données SQLite pour l'environnement local.
Le fichier ``oc-lettings-site.sqlite3`` est inclus dans le dépôt avec les
données nécessaires au fonctionnement de l'application.

Modèles de données
------------------

Django utilise des modèles Python pour décrire la structure des données :
chaque modèle représente généralement une table, et chaque attribut correspond
à un champ de base de données. Les relations entre modèles sont également
définies dans ces classes.

``Address``
~~~~~~~~~~~

Modèle de l'application ``lettings`` représentant l'adresse d'une location.

.. list-table::
   :header-rows: 1
   :widths: 30 30 40

   * - Champ
     - Type
     - Description
   * - ``number``
     - ``PositiveIntegerField``
     - Numéro de rue.
   * - ``street``
     - ``CharField``
     - Nom de rue.
   * - ``city``
     - ``CharField``
     - Ville.
   * - ``state``
     - ``CharField``
     - État américain.
   * - ``zip_code``
     - ``PositiveIntegerField``
     - Code postal.
   * - ``country_iso_code``
     - ``CharField``
     - Code pays ISO.

``Letting``
~~~~~~~~~~~

Modèle de l'application ``lettings`` représentant une location affichée sur le site.

.. list-table::
   :header-rows: 1
   :widths: 30 30 40

   * - Champ
     - Type
     - Description
   * - ``title``
     - ``CharField``
     - Titre de la location.
   * - ``address``
     - ``OneToOneField``
     - Adresse associée à la location.

``Profile``
~~~~~~~~~~~

Modèle de l'application ``profiles`` représentant les informations publiques
associées à un utilisateur Django.

.. list-table::
   :header-rows: 1
   :widths: 30 30 40

   * - Champ
     - Type
     - Description
   * - ``user``
     - ``OneToOneField``
     - Utilisateur Django associé au profil.
   * - ``favorite_city``
     - ``CharField``
     - Ville favorite affichée sur la page du profil.

Relations principales
---------------------

Les relations ``Letting`` → ``Address`` et ``Profile`` → ``User`` sont définies
avec ``OneToOneField``. Ce type de relation associe une instance d'un modèle à
une seule instance d'un autre modèle.