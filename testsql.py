from extentions import db

class Proxy(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    server = db.Column(db.Text, nullable=False)
    port = db.Column(db.Text, nullable=False)
    # connection = db.Column(db.Json, nullable=True)

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def create_proxy(proxy_info):

        proxy_server = proxy_info.get('server')
        proxy_port = proxy_info.get('port')

        exist_proxy = db.session.query(Proxy).filter(
            Proxy.server == proxy_server).filter(Proxy.port == proxy_port).first()

        if exist_proxy:
            return exist_proxy

        proxy = Proxy(server=proxy_server, port=proxy_port)

        db.session.add(proxy)
        db.session.commit()

        return proxy

