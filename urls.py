from django.conf.urls import patterns, url


urlpatterns = patterns('',

    url(r'^edition/$', 'lp_football_results.views.edition'),
    url(r'^sample/$', 'lp_football_results.views.sample'),
    url(r'^validate_config/$', 'lp_football_results.views.validate_config'),
    url(r'^meta.json$', 'lp_football_results.views.meta_json'),
    url(r'^icon.png$', 'lp_football_results.views.icon'),
    
)




