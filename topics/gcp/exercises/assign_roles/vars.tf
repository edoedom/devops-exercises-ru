variable "project_id" {
  type = string
}
variable "env_id" {
  type        = string
  description = "2-10 lowercase letters/digits/hyphens, starting with a letter."
  validation {
    condition     = can(regex("^[a-z][a-z0-9-]{1,9}$", var.env_id))
    error_message = "env_id must start with a lowercase letter and contain 2-10 lowercase letters/digits/hyphens."
  }
}
