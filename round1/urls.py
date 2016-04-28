from django.conf.urls import url
from round1 import views

urlpatterns = [
	url(r'^$', views.index, name="index"),
	url(r'register$',views.register),
	url(r'login$',views.login), 
	url(r'enter$',views.enter),
    url(r'ques$',views.ques),
    url(r'logout$',views.log_out),
    url(r'timer$',views.timer), 
    url(r'first$',views.get_ques),
    url(r'result$',views.result),
    url(r'leaderboard$',views.leaderBoard),
    url(r'timeup$',views.timeup),
    url(r'update_score$',views.update_score)      
]
