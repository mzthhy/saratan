from validation.pipeline.validation_task import PredictorTask
import config as miccai_config

import numpy as np

class vnetPredictor(PredictorTask):


	def run(self, volumes):
		print len(volumes)
		print volumes[0].shape
		print volumes[1].shape
		print volumes[2].shape
		return [np.random.random((5,5)) , np.random.random((6,6))]
	def save(self, directory):
		print "Saving myPredictor to ",directory