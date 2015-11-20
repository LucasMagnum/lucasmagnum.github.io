Django na prática - Templates
#############################################

:date: 2015-11-20 22:00
:tags: python, django, django-na-pratica
:category: Python
:slug: django-na-pratica-aula-03
:author: Lucas Magnum
:email:  lucasmagnumlopes@gmail.com
:github: lucasmagnum
:linkedin: lucasmagnum


Esse é o terceiro post do **django na prática** onde você aprenderá tudo que precisa para criar um sistema web :D

Estamos utilizando a versão 1.8 do Django com Python 3!

Para a parte 2 `clique aqui <http://pythonclub.com.br/django-na-pratica-aula-01.html>`_.


===========
Hello world
===========

No post anterior aprendemos a como criar nossa primeira view, ela está retornando
um texto puro, o ideal seria servir algum conteúdo HTML.

Dentro do diretório onde se encontra o ``helloworld.py``, vamos criar uma pasta
chamada ``templates`` e uma arquivo ``index.html`` com o seguinte conteúdo:

.. code-block:: html

    <html>
        <head>
            <title>Django na prática</title>
        </head>
        <body>
            <h1> Hello World! </h1>
        </body>
    </html>

Nossa estrutura ficou assim:

.. code-block:: bash

    $ tree .
    .
    ├── helloworld.py
    ├── templates
    │   └── index.html
    └── tests.py

    1 directory, 3 files



