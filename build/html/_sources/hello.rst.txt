===========
Hello World
===========

Hello, this is a demo page.

*****
Bases
*****

Paragraphes
~~~~~~~~~~~

Ceci est un paragraphe. Je peux retourner à la ligne, je
serais toujours dans le même paragraphe.

Pour écrire un second paragraphe, il suffit de le séparer
du premier par une ligne vide.

Format
~~~~~~

Voici du texte en *italique*, en **gras**, et voici du ``code inline``.

Pour faire un lien inline c'est simple :
lien vers `Google <https://google.be/>`_

Listes
~~~~~~

Liste à puce :

* Ceci est une liste
* un autre élément

  * Une sous-liste
  * notez bien le saut de ligne avec la liste principale,
    ça ne marchera pas si vous l'oubliez !
    
* un dernier élément

Liste ordonnée :

1. Un
2. Deux
3. Trois

Une autre liste ordonnée :

#. Un
#. Deux
#. Trois

Citation
~~~~~~~~

FLOZz a dit :

    Ceci est une citation
   
*******  
Tableau
*******
   
+-----------+-----------+-----------+
| Heading 1 | Heading 2 | Heading 3 |
+===========+===========+===========+
| Hello     | World     |           |
+-----------+-----------+-----------+
| foo       |                       |
+-----------+          bar          |
| baz       |                       |
+-----------+-----------------------+

*****
Codes
*****

Voici comment faire un bloc que code simple ::

   Ceci est un bloc de code. Il est créé grâce aux doubles deux-points.

On peut également placer les doubles deux-points seuls si on ne veut pas
terminer sa phrase par ce symbole.

::

   Voici un autre bloc de code...

Et c'est pas fini ! On peut aussi définir un bloc de code avec une syntaxe
plus explicite, grâce à laquelle on peut indiquer à Sphinx dans quel
langage il est rédigé, ce qui lui permettra d'activer la coloration
syntaxique :

.. code-block:: python

    import numpy as np
    x = np.arange(9) # vector 0, 1, ..., 8
    
Doctest:

>>> 1 + 1
2
 
*****    
Boxes
*****

Note
~~~~
     
.. NOTE::

   Ceci est une note.
   
Warning
~~~~~~~

.. WARNING::

   Ceci est un avertissement !
   
Important
~~~~~~~~~

.. IMPORTANT::

   Ceci est important !
   
***********
Mathematics
***********

The area of a circle is :math:`A_\text{c} = (\pi/4) d^2`.

.. math::
    \alpha(t) = 1 + t
 
******  
Images
******

Voici une image :

.. figure:: python_logo.jpg

Voici un autre image avec quelques paramètres en plus :

.. figure:: python_logo.jpg
    :alt: Texte alternatif
    :target: http://python.org/
    :width: 400px
    :align: center

    Texte affiché sous l'image
   



