locals {
  # Учебные роли из задания, не универсальный production-набор прав.
  roles = toset([
    "roles/compute.storageAdmin",
    "roles/compute.networkAdmin",
    "roles/compute.securityAdmin"
  ])
}
resource "google_service_account" "some_member" {
  project      = var.project_id
  account_id   = "${var.env_id}-member"
  display_name = "${var.env_id} exercise member"
}
resource "google_project_iam_member" "storageAdminMaster" {
  for_each = local.roles
  project  = var.project_id
  role     = each.value
  member   = "serviceAccount:${google_service_account.some_member.email}"
}
