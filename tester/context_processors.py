from django.conf import settings


def from_settings(request):
	return {
		'INSTANCE_LABEL': settings.INSTANCE_LABEL,
		'INSTANCE_COLOR': settings.INSTANCE_COLOR,
	}
