Architecture
============

L'application OC Lettings est organisée autour d'un projet Django principal et
de deux applications métier.

Organisation du projet
----------------------

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Élément
     - Rôle
   * - ``oc_lettings_site``
     - Projet Django principal. Il contient la configuration globale, les URLs
       racines et les pages communes.
   * - ``lettings``
     - Application dédiée aux locations et aux adresses.
   * - ``profiles``
     - Application dédiée aux profils utilisateurs.

Séparation des responsabilités
------------------------------

La logique liée aux locations est regroupée dans ``lettings``.
La logique liée aux profils utilisateurs est regroupée dans ``profiles``.

Cette organisation limite le couplage entre les domaines fonctionnels et facilite
la maintenance de l'application.

Routage
-------

Les routes globales sont définies dans ``oc_lettings_site``.
Les routes propres aux locations et aux profils sont déclarées dans leurs
applications respectives, puis incluses dans la configuration principale.

Django permet d'inclure les routes d'une application avec ``include()`` et
d'utiliser des espaces de noms pour organiser les URLs par application.