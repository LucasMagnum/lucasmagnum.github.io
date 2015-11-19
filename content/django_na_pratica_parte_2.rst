Django na prática - Testes
#############################################

:date: 2015-11-19 21:55
:tags: python, django, django-na-pratica
:category: Python
:slug: django-na-pratica-aula-02
:author: Lucas Magnum
:email:  lucasmagnumlopes@gmail.com
:github: lucasmagnum
:linkedin: lucasmagnum


Esse é o segundo post do **django na prática** onde você aprenderá tudo que precisa para criar um sistema web :D

Estamos utilizando a versão 1.8 do Django com Python 3!

Para a parte 1, `clique aqui <http://pythonclub.com.br/django-na-pratica-aula-01.html>`_.


===============
Por que testar?
===============

Bug sempre irão existir, é bom se acostumar com isso. Testar nossa aplicação desde o inicio
nos ajuda a mitigar a quantidade de defeitos que irão existir no nosso sistema.

Vamos criar um arquivo chamado ``tests.py`` dentro do diretório da nossa aplicação.

Nossa estrutura fica assim:

.. code-block:: bash

    .
    ├── helloworld.py
    └── tests.py

    0 directories, 2 files

================
Hello World Test
================

Para iniciar nossos testes vamos utilizar a biblioteca padrão do python ``unittest``.

Nosso arquivo de teste ficou assim:

.. code-block:: python

    # importação do módulo unittest
    import unittest


    # definição da nossa classe de teste
    class HelloWorldTestCase(unittest.TestCase):
        pass

Executamos os testes assim:

.. code-block:: bash

    $ python -m unittest tests.py

    ----------------------------------------------------------------------
    Ran 0 tests in 0.000s

    OK

Recebemos o feedback que nenhum teste foi executado, isso porquê não adicionamos nenhuma função de teste na nossa classe ainda.


