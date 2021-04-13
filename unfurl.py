import subprocess

from assemblyline_v4_service.common.base import ServiceBase
from assemblyline_v4_service.common.result import Result, ResultSection

class Unfurl(ServiceBase):
	def __init__(self, config=None):
		super(Unfurl, self).__init__(config)

	def start(self):
		self.log.debug("Unfurl service started")

	def stop(self):
		self.log.debug("Unfurl service ended")

	def execute(self, request):
		result = Result()
		url = request.task.metadata.get('submitted_url')

		p1 = subprocess.Popen("python3 /var/lib/assemblyline/unfurl/unfurl_cli.py \"" + url + "\"", shell=True, stdout=subprocess.PIPE)
		p1.wait()

		stdout = p1.communicate()[0].decode("utf-8")

		report = stdout.split("\n")

		i = 0
		while "[1]" not in report[i]:
			i += 1
		report = "\n".join(list(filter(None, report[i:])))

		text_section = ResultSection("Unfurl scan report")
		text_section.add_line(report)

		result.add_section(text_section)
		request.result = result