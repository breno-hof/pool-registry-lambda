module "lambda" {
	source					= "github.com/breno-hof/module-lambda//src?ref=1.1.0"

	is_architecture_x86_64 	= true

	lambda_name				= local.lambda_name
	
	handler_entrypoint		= local.handler_entrypoint
	runtime					= local.runtime

	source_path				= local.source_path
}