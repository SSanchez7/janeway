__copyright__ = "Copyright 2017 Birkbeck, University of London"
__author__ = "Martin Paul Eve & Andy Byers"
__license__ = "AGPL v3"
__maintainer__ = "Birkbeck Centre for Technology and Publishing"


from django.conf.urls import url

from repository import views

urlpatterns = [
    url(r'^dashboard/$',
        views.repository_dashboard,
        name='repository_dashboard'),

    url(r'^dashboard/(?P<preprint_id>\d+)/$',
        views.repository_author_article,
        name='repository_author_article'),

    url(r'^about/$',
        views.repository_about,
        name='repository_about'),

    url(r'^search/$',
        views.preprints_search,
        name='preprints_search'),

    url(r'^search/(?P<search_term>.*)/$',
        views.preprints_search,
        name='preprints_search_with_term'),

    url(r'^view/(?P<preprint_id>\d+)/$',
        views.repository_preprint,
        name='repository_preprint'),

    url(r'^view/(?P<article_id>\d+)/pdf/$',
        views.preprints_pdf,
        name='preprints_pdf'),

    url(r'^list/$',
        views.repository_list,
        name='repository_list'),

    url(r'^list/(?P<subject_slug>[-\w]+)/$',
        views.repository_list,
        name='preprints_list_subject'),

    url(r'^editors/$',
        views.preprints_editors,
        name='preprints_editors'),

    url(r'^submit/start/$',
        views.repository_submit,
        name='repository_submit'),

    url(r'^submit/(?P<preprint_id>\d+)/$',
        views.repository_submit,
        name='repository_submit_with_id'),

    url(r'^submit/(?P<preprint_id>\d+)/authors/$',
        views.repository_authors,
        name='repository_authors'),

    url(r'^submit/(?P<preprint_id>\d+)/authors/delete/(?P<redirect_string>[-\w]+)/$',
        views.preprints_delete_author,
        name='preprints_delete_author'),

    url(r'^submit/(?P<preprint_id>\d+)/authors/order/$',
        views.preprints_author_order,
        name='preprints_author_order'),

    url(r'^submit/(?P<preprint_id>\d+)/files/$',
        views.repository_files,
        name='repository_files'),

    url(r'^submit/(?P<preprint_id>\d+)/review/$',
        views.repository_review,
        name='repository_review'),

    url(r'^manager/$',
        views.preprints_manager,
        name='preprints_manager'),

    url(r'^manager/(?P<preprint_id>\d+)/$',
        views.repository_manager_article,
        name='repository_manager_article'),

    url(r'^manager/(?P<preprint_id>\d+)/edit/$',
        views.repository_edit_metadata,
        name='repository_edit_metadata'),

    url(r'^manager/(?P<preprint_id>\d+)/download/(?P<file_id>\d+)/$',
        views.repository_download_file,
        name='repository_download_file'),

    url(r'^manager/(?P<preprint_id>\d+)/notification/$',
        views.repository_notification,
        name='repository_notification'),

    url(r'^manager/(?P<preprint_id>\d+)/log/$',
        views.repository_preprint_log,
        name='repository_preprint_log'),

    url(r'^manager/(?P<preprint_id>\d+)/comments/$',
        views.repository_comments,
        name='repository_comments'),

    url(r'^manager/subjects/$',
        views.repository_subjects,
        name='repository_subjects'),
    url(r'^manager/subjects/delete/$',
        views.repository_delete_subject,
        name='repository_delete_subject'),

    url(r'^manager/subjects/(?P<subject_id>\d+)/$',
        views.repository_subjects,
        name='repository_subjects_with_id'),

    url(r'^manager/rejected/$',
        views.repository_rejected_submissions,
        name='repository_rejected_submissions'),

    url(r'^manager/orphans/$',
        views.orphaned_preprints,
        name='preprints_orphaned_preprints'),

    url(r'^manager/versions/$',
        views.version_queue,
        name='version_queue'),

    url(r'^wizard/$',
        views.repository_wizard,
        name='repository_wizard'),

    url(r'^wizard/repository/(?P<short_name>[-\w]+)/step/(?P<step>\d+)/$',
        views.repository_wizard,
        name='repository_wizard_with_id'),
]
