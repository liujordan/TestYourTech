import traceback
class ActionBase(object):
	def __init__(self, *args, **kwargs):
		pass
	def _setup(self):
		pass
	def _execute(self):
		pass
	def _cleanup(self):
		pass
		
	def run(self):
		try:
			self._setup()
			result = self._execute()
			self._cleanup()
		except:
			result = False
			traceback.print_exc()
		return result