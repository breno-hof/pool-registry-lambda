locals {
	lambda_name			= "pool-registry"
	handler_entrypoint	= "lambda.lambda_handler"
	timeout				= 300
	runtime				= "python3.8"
	source_path			= "../src"
}