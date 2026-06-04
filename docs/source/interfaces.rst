Routes et vues
==============

L'application OC Lettings expose des interfaces web Django.

Les routes sont définies dans les fichiers ``urls.py`` du projet principal et des
applications ``lettings`` et ``profiles``. Chaque route associe une URL à une vue
chargée de traiter la requête et de retourner une page HTML.

Routes principales
------------------

.. list-table::
   :header-rows: 1
   :widths: 25 30 45

   * - URL
     - Vue
     - Description
   * - ``/``
     - ``oc_lettings_site.views.index``
     - Page d'accueil du site.
   * - ``/lettings/``
     - ``lettings.views.index``
     - Liste des locations disponibles.
   * - ``/lettings/<letting_id>/``
     - ``lettings.views.letting``
     - Page de détail d'une location.
   * - ``/profiles/``
     - ``profiles.views.index``
     - Liste des profils utilisateurs.
   * - ``/profiles/<username>/``
     - ``profiles.views.profile``
     - Page de détail d'un profil utilisateur.
   * - ``/admin/``
     - Administration Django
     - Interface d'administration du site.

Organisation des routes
-----------------------

Les routes globales sont définies dans ``oc_lettings_site``.
Les routes liées aux locations sont définies dans ``lettings``.
Les routes liées aux profils sont définies dans ``profiles``.

Les URLs des applications sont incluses dans la configuration principale du
projet avec ``include()``. Les espaces de noms permettent ensuite de référencer
les routes par application.