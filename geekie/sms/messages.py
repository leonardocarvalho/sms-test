import pyramid.view
import twilio.twiml


def includeme(config):
    config.add_route("assessment save", pattern="/assessment/save")
    config.scan(__name__)


@pyramid.view.view_config(route_name="assessment save", renderer="string", request_method=["GET"])
def save_assessment(request):
    body = request.params.get("Body")
    response = twilio.twiml.Response()
    response.message("Thanks for submitting: {}. See you".format(body))
    return str(response)
