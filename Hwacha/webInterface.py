import web
from appControl import appControl

urls = ('/index','index',
        )

app = web.application(urls,globals())
render = web.template.render('template/')


class index(object):
    
    sm_list = []
    def GET(self):
        return render.index()

    def POST(self):
        appObject = appControl.appController()
        sm_list = []
        form = web.input(subject="Hwacha Message",message="None",sm_all=None,
                sm_twitter = None, sm_mail=None,sm_wordpress=None )
        
        if form.sm_all:
            sm_list = ['twitter','mail']
        else:
            for i in form.sm_mail,form.sm_twitter,form.sm_wordpress:
                if i :
                    sm_list.append(i)

        status = appObject.broadcastMessage(form.message,sm_list)
                



if __name__ == "__main__":
    app.run()
