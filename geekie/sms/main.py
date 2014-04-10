import pyramid.config


def main(global_config, **settings):
    config = pyramid.config.Configurator(settings=settings)
    config.include("geekie.sms.messages")
    return config.make_wsgi_app()
