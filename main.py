import web

web.config.debug = False

urls = (
    "/", "Index",
    "/count", "Count",
    "/reset", "Reset",
)

app = web.application(urls, locals())

# Store session data in folder 'sessions' under the same directory as your app.
session = web.session.Session(app, web.session.DiskStore("sessions"), initializer={"count": 0,"visitas" : 0})

class Index:
    def GET(self):
        return "Funciona el index"

class Count:
    def GET(self):
        session.count += 1
        session.visitas += 2
        return str(session.visitas)

class Reset:
    def GET(self):
        session.kill()
        return "Reset"

if __name__ == "__main__":
    app.run()
