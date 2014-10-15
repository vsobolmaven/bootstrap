from fanstatic import Library, Resource

library = Library('twitter_bootstrap', 'resources')

twitter_bootstrap = Resource(library, 'bootstrap.css')
twitter_bootstrap_responsive = Resource(library, 'bootstrap-responsive.css')
twitter_bootstrap_wide = Resource(library, 'bootstrap-wide.css', depends=[twitter_bootstrap])
