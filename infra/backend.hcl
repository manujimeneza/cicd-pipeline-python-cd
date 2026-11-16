# infra/backend.hcl
bucket       = "tfstate-calculadora-manujimeneza"
key          = "calculadora/terraform.tfstate"
region       = "us-east-1"
use_lockfile = true