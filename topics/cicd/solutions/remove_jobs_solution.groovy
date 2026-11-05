import jenkins.model.Jenkins
import hudson.model.Job

// Script Console администратора. Сначала проверьте список в режиме DRY_RUN.
def DRY_RUN = true
def marker = 'REMOVE_ME'
Jenkins.get().getAllItems(Job.class).findAll { it.name.contains(marker) }.each { job ->
    if (job.builds.any { it.isBuilding() || it.isLogUpdated() }) {
        println "SKIP running: ${job.fullName}"
    } else {
        println "${DRY_RUN ? 'WOULD DELETE' : 'DELETE'}: ${job.fullName}"
        if (!DRY_RUN) { job.delete() }
    }
}
