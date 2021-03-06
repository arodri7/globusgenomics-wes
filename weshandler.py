

def __service_info():
	return """
	{
		"workflow_type_versions": {		
		},
		"supported_wes_versions": [
			"1.0"
		],
		"workflow_engine_versions": {
			"Globus Genomics": "5.0.0"
		}
	}
	"""

def __get_workflows():
	return """
    {
      "workflows": []
    }
	"""

def __delete_workflow(workflow_id):
	## Delete the workflow with exception handling:

	return """
    {
      "workflow_id": workflow_id
    }
    """

def __submit_workflow(parameters, api_key):
    return "1234"
