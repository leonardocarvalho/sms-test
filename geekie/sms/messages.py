import pyramid.view



def includeme(config):
    config.add_route("assessment save", pattern="/assessment/save")
    config.scan(__name__)


@pyramid.view.view_config(route_name="assessment save", renderer="json", request_method=["GET"])
def save_assessment(request):
    print request.params
    return dict(request.params)
