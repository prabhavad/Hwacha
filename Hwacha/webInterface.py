import web
from web import form
from appControl import appControl

urls = ('/','Index',
        '/del/(\w+)' ,'Delete',
        '/add/(\w+)','Add',
        '/result','Result',

        )

app = web.application(urls,globals())
render = web.template.render('template/')


class Index(object):
    


    def GET(self):
        appObject = appControl.appController()
        sm_list = appObject. getAvailableSmList()
        all_list = ['twitter','mail','wordpress']
        return render.index(sm_list,all_list)


    def POST(self):
        appObject = appControl.appController()
        sm_list = []
        form = web.input(subject="Hwacha Message",message="None",sm_all=None,
                twitter=None, mail=None,wordpress=None )
        
        print form.mail,form.twitter,form.wordpress

        if form.sm_all:
            sm_list = appObject. getAvailableSmList()
        else:
            for i in form.mail,form.twitter,form.wordpress:
                if i :
                    sm_list.append(i)
        status = appObject.broadcastMessage(form.message,sm_list)
        print status
        return render.result(status)



class Delete(object):
    def POST(self,smName):
        smList=[]
        smList.append(smName)
        appObject = appControl.appController()
        appObject.removeSm(smList)
        raise web.seeother('/')


        
class Add(object):
    def POST(self,smName):
        smList=[]
        smList.append(smName)
        appObject = appControl.appController()
        appObject.addSm(smList)
        raise web.seeother('/')
      
class Result(object):
    def POST(self):
        raise web.seeother('/')
    


if __name__ == "__main__":
    app.run()
