import jenkins.model.Jenkins
import hudson.model.Job

// Для регулярной очистки предпочтительнее buildDiscarder(logRotator(daysToKeepStr: '14')).
// Одноразовая очистка через Script Console: сначала DRY_RUN, без прямого удаления файлов.
def DRY_RUN = true
def cutoff = System.currentTimeMillis() - 14L * 24 * 60 * 60 * 1000
Jenkins.get().getAllItems(Job.class).each { job ->
    job.builds.toList().each { build ->
        if (build.timeInMillis < cutoff && !build.isBuilding() &&
                !build.isLogUpdated() && !build.isKeepLog()) {
            println "${DRY_RUN ? 'WOULD DELETE' : 'DELETE'}: ${build.fullDisplayName}"
            if (!DRY_RUN) { build.delete() }
        }
    }
}
