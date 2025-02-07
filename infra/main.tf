data "archive_file" "this" {
  type 						= "zip"

  source_dir 				= "${local.source_path}"
  output_path 				= "${local.output_path}.zip"
}

resource "aws_s3_bucket" "this" {
	bucket					= "${local.lambda_name}-lambda-bucket"
}

resource "aws_s3_object" "this" {
  bucket 					= aws_s3_bucket.this.id

  key    					= "${local.lambda_name}.zip"
  source 					= data.archive_file.this.output_path

  etag 						= filemd5(data.archive_file.this.output_path)
}

resource "aws_iam_role" "this" {
	name					= "${local.lambda_name}-lambda-role"

	assume_role_policy		= jsonencode({
		Version 			= "2012-10-17"
		Statement 			= [{
			Action 			= "sts:AssumeRole"
			Effect 			= "Allow"
			Principal 		= {
				Service 	= "lambda.amazonaws.com"
			}
		}]
  	})
}

resource "aws_iam_role_policy_attachment" "lambda_policy" {
  role       				= aws_iam_role.this.name
  policy_arn 				= "arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole"
}

module "lambda" {
	source					= "../../module-lambda/src"

	is_architecture_x86_64 	= true

	lambda_name				= local.lambda_name
	role_arn				= aws_iam_role.this.arn
	
	handler_entrypoint		= local.handler_entrypoint
	runtime					= local.runtime

  	source_code_hash 		= data.archive_file.this.output_base64sha256

	s3_bucket				= aws_s3_bucket.this.bucket
	s3_key					= aws_s3_object.this.key
}