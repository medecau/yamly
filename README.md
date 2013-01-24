YAMLy
=====

Install
-------

    pip install yamly


Use
---

    import yamly

    conf = yamly.load(open("conf.yaml"))
    print conf


Documentation:
--------------

**load(doc)**

wraps pyyaml load() and instanciates an YAMLy object for you 


**dump(obj)**

dumps a yaml from the YAMLy object


Bugs & Co.
----------

If you find bugs or new features that are not implemented you can:

 * [Fork and implement the changes](https://github.com/medecau/yamly/fork)
 * [Fork and write a test that fails but shouldn't](https://github.com/medecau/yamly/fork)
 * [Submit an issue in github](https://github.com/medecau/yamly/issues)
