variable "project_id" {
  type        = string
  description = "Globally unique immutable Google Cloud project ID (6-30 characters)."
  validation {
    condition     = can(regex("^[a-z][a-z0-9-]{4,28}[a-z0-9]$", var.project_id))
    error_message = "Use 6-30 lowercase letters, digits or hyphens; start with a letter, end with a letter/digit."
  }
}
variable "organization_id" {
  type        = string
  default     = null
  description = "Optional numeric organization ID; null for an account without an organization."
  validation {
    condition     = var.organization_id == null ? true : can(regex("^[0-9]+$", var.organization_id))
    error_message = "Use the numeric organization ID or null."
  }
}
resource "google_project" "gcp_project" {
  name            = "DevOps Exercise"
  project_id      = var.project_id
  org_id          = var.organization_id
  deletion_policy = "PREVENT"
}
output "project_id" { value = google_project.gcp_project.project_id }
