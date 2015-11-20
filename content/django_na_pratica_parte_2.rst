Django na prática - Testes
#############################################

:date: 2015-12-01 00:00
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
Vamos adicionar nosso primeiro teste de exemplo:

Altere o arquivo ``tests.py`` para ficar assim:


.. code-block:: python

    import unittest


    class HelloWorldTestCase(unittest.TestCase):
        # definição do nosso primeiro teste
        # as funções de teste devem começar com `test_`
        def test_hello_world(self):
            self.assertEqual(2, 2)

No nosso primeiro teste, estamos garantido que 2 é igual a 2, `oh really?!`.

Executando novamente os testes, somos informados que um teste foi executado com sucesso:


.. code-block:: bash

    $ python -m unittest tests.py

    ----------------------------------------------------------------------
    Ran 1 tests in 0.000s

    OK

Certo, agora vamos testar nossa view!

=============
Teste de view
=============

Nossa view é bem simples, o que vamos testar? O princípio de um teste é garantir que o código funcione
de acordo com o que esperamos, então, vamos testar se a view retorna nosso.

Nossa view é uma função que recebe uma requisição e retorna uma resposta, nosso plano de testes
para nossa primeira view, ficou assim:

    1. Testar se a view retorna um ``http status code`` a igual 200
    2. Testar se a view retorna "Django na prática - Hello World!"
